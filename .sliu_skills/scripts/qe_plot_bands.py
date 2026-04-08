#!/usr/bin/env python3
"""Plot a Quantum ESPRESSO band structure from a `pw.x` bands output file."""

from __future__ import annotations

import argparse
import math
import os
import re
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

try:
    import numpy as np
    import numpy.linalg as la
except ImportError as exc:
    raise SystemExit(
        "numpy is required. Install it in the same Python environment used to "
        "run this script, for example:\n"
        "  python -m pip install numpy"
    ) from exc

try:
    default_mpl_dir = Path.home() / ".matplotlib"
    if "MPLCONFIGDIR" not in os.environ:
        if not default_mpl_dir.exists() or not os.access(default_mpl_dir, os.W_OK):
            fallback_mpl_dir = Path(tempfile.gettempdir()) / f"matplotlib-{os.getuid()}"
            fallback_mpl_dir.mkdir(parents=True, exist_ok=True)
            os.environ["MPLCONFIGDIR"] = str(fallback_mpl_dir)

    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
except ImportError as exc:
    raise SystemExit(
        "matplotlib is required. Install it in the same Python environment used "
        "to run this script, for example:\n"
        "  python -m pip install matplotlib"
    ) from exc


BOHR_TO_ANG = 0.529177
FIGURE_WIDTH = 4.0
FIGURE_HEIGHT = FIGURE_WIDTH * 0.618
LABEL_ANGLE_THRESHOLD = 52.0
DISCONTINUITY_THRESHOLD = 0.2

plt.rcParams.update({"figure.figsize": (FIGURE_WIDTH, FIGURE_HEIGHT)})

ALAT_RE = re.compile(r"lattice parameter \(alat\)\s*=\s*([-\d.]+)\s+a\.u\.", re.I)
ELECTRONS_RE = re.compile(r"number of electrons\s*=\s*([-\d.]+)", re.I)
K_HEADER_RE = re.compile(r"^\s*k\s*=.*bands \(ev\):\s*$")
FLOAT_RE = re.compile(r"[-+]?\d+\.\d+")


@dataclass
class BandData:
    special_positions: list[float]
    kline: list[float]
    bands: list[list[float]]


@dataclass
class ParsedArgs:
    output: Path
    klabels: Path | None
    name: str
    raw: bool
    plot: bool
    nspin: int
    n_up: int | None
    n_dn: int | None
    emin: float
    emax: float
    estep: float
    fermi_mode: int
    fermi_user: float | None


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Read a Quantum ESPRESSO `bands` output file, export raw band data, "
            "and save band-structure figures."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  python3 qe_plot_bands.py -o bands.out -k klabel -e 4 4 2 -n pbe -fe 1 -r\n"
            "  python3 qe_plot_bands.py -o bands.out -k klabel -e 4 4 2 -n spin "
            "-fe 1 -s 2 -ne 182 180\n"
        ),
    )
    parser.add_argument(
        "-o",
        "--output",
        required=True,
        help="Output file from `pw.x` with `calculation = 'bands'`.",
    )
    parser.add_argument(
        "-k",
        "--klabels",
        help="Text file containing one high-symmetry label per special point.",
    )
    parser.add_argument(
        "-n",
        "-f",
        "--name",
        default="pbe",
        help="Tag appended to the generated figure and raw-data filenames.",
    )
    parser.add_argument(
        "-r",
        "--raw",
        action="store_true",
        help="Export raw band-data files for external plotting.",
    )
    parser.add_argument(
        "-p",
        "--plot",
        action="store_true",
        help="Compatibility flag. Plotting is enabled by default.",
    )
    parser.add_argument(
        "--no-plot",
        action="store_true",
        help="Skip figure generation and only parse/export the data.",
    )
    parser.add_argument(
        "-s",
        "--nspin",
        type=int,
        choices=[1, 2, 4],
        default=1,
        help="1: non-polarized, 2: spin-polarized, 4: noncollinear.",
    )
    parser.add_argument(
        "-ne",
        nargs=2,
        type=int,
        metavar=("NUP", "NDN"),
        help="Number of up/down electrons, only for nspin = 2.",
    )
    parser.add_argument(
        "-e",
        nargs=3,
        type=float,
        metavar=("EMIN", "EMAX", "ESTEP"),
        default=[4.0, 4.0, 2.0],
        help=(
            "Energy range relative to Ef: [energy_below_Ef] [energy_above_Ef] "
            "[energy_step]. Use positive values."
        ),
    )
    parser.add_argument(
        "-fe",
        nargs="+",
        default=["1"],
        metavar=("MODE", "VALUE"),
        help=(
            "Fermi energy setting: 1 -> (VBM + CBM)/2, 2 -> VBM, "
            "3 -> user-provided Fermi energy in eV."
        ),
    )
    return parser


def parse_cli(argv: list[str]) -> ParsedArgs:
    args = build_parser().parse_args(argv)

    output = Path(args.output).expanduser()
    if not output.is_file():
        raise SystemExit(f"QE output file not found: {output}")

    klabels = Path(args.klabels).expanduser() if args.klabels else None
    if klabels is not None and not klabels.is_file():
        raise SystemExit(f"k-label file not found: {klabels}")

    fermi_tokens = args.fe
    try:
        fermi_mode = int(fermi_tokens[0])
    except ValueError as exc:
        raise SystemExit(f"Invalid -fe mode: {fermi_tokens[0]}") from exc

    fermi_user = None
    if fermi_mode in (1, 2):
        if len(fermi_tokens) != 1:
            raise SystemExit(f"-fe {fermi_mode} does not take extra values.")
    elif fermi_mode == 3:
        if len(fermi_tokens) != 2:
            raise SystemExit("-fe 3 requires a user-supplied Fermi energy in eV.")
        fermi_user = float(fermi_tokens[1])
    else:
        raise SystemExit("Only -fe 1, -fe 2, and -fe 3 are supported.")

    n_up = n_dn = None
    if args.ne is not None:
        n_up, n_dn = args.ne
    if args.nspin != 2 and args.ne is not None:
        raise SystemExit("-ne can only be used when -s 2.")

    emin, emax, estep = args.e
    if emin <= 0 or emax <= 0 or estep <= 0:
        raise SystemExit("-e expects positive values: below above step.")

    return ParsedArgs(
        output=output,
        klabels=klabels,
        name=args.name,
        raw=args.raw,
        plot=not args.no_plot,
        nspin=args.nspin,
        n_up=n_up,
        n_dn=n_dn,
        emin=emin,
        emax=emax,
        estep=estep,
        fermi_mode=fermi_mode,
        fermi_user=fermi_user,
    )


def extract_scalar(text: str, pattern: re.Pattern[str], label: str) -> float:
    match = pattern.search(text)
    if not match:
        raise SystemExit(f"Could not find {label} in the QE output file.")
    return float(match.group(1))


def parse_k_header(line: str) -> tuple[str, str, str] | None:
    if not K_HEADER_RE.match(line):
        return None

    values = FLOAT_RE.findall(line)
    if len(values) < 3:
        raise SystemExit(f"Could not parse k-point coordinates from header: {line.strip()}")

    return values[0], values[1], values[2]


def read_bands(output_path: Path) -> tuple[list[list[object]], str]:
    text = output_path.read_text(encoding="utf-8", errors="replace")
    alat = extract_scalar(text, ALAT_RE, "lattice parameter")
    factor = 2.0 * math.pi / (alat * BOHR_TO_ANG)

    lines = text.splitlines()
    raw_blocks: list[tuple[str, str, str, list[float]]] = []
    i = 0
    while i < len(lines):
        k_header = parse_k_header(lines[i])
        if k_header is None:
            i += 1
            continue

        kx, ky, kz = k_header
        i += 1
        energies: list[float] = []
        while i < len(lines):
            line = lines[i]
            stripped = line.strip()
            if parse_k_header(line) is not None:
                break
            if stripped.startswith("Writing all") or stripped.startswith("JOB DONE") or stripped.startswith("This run was"):
                break
            values = [float(value) for value in FLOAT_RE.findall(line)]
            if values:
                energies.extend(values)
            elif energies and stripped:
                break
            i += 1

        if not energies:
            continue
        raw_blocks.append((kx, ky, kz, energies))

    if not raw_blocks:
        raise SystemExit("No `k = ... bands (ev):` blocks were found in the QE output.")

    kpoints: list[list[object]] = []
    expected_nbands = None
    for kx, ky, kz, energies in raw_blocks:
        if expected_nbands is None:
            expected_nbands = len(energies)
        elif len(energies) != expected_nbands:
            raise SystemExit(
                "Inconsistent number of bands detected while parsing the QE output."
            )
        kvector = np.array([float(kx) * factor, float(ky) * factor, float(kz) * factor])
        kpoints.append([kvector, energies])

    if not kpoints:
        raise SystemExit("Band parsing failed: no k-points with eigenvalues were collected.")

    return kpoints, text


def angle_degrees(v1: np.ndarray, v2: np.ndarray) -> float:
    cosang = np.dot(v1, v2)
    sinang = la.norm(np.cross(v1, v2))
    return np.degrees(np.arctan2(sinang, cosang))


def create_plot_array(
    kpoints: list[list[object]],
    nspin: int,
    raw: bool,
    output_dir: Path,
) -> BandData:
    kline = [0.0]
    special_positions = [kline[0]]
    kdiff = np.zeros(3, dtype=float)

    first_energies = kpoints[0][1]
    bands = [[first_energies[i]] for i in range(len(first_energies))]
    nkpts = len(kpoints)
    nkpts_for_labels = nkpts if nspin in (1, 4) else int(nkpts / 2)

    for ikpt in range(1, nkpts_for_labels):
        previous_diff = kdiff
        kdiff = kpoints[ikpt][0] - kpoints[ikpt - 1][0]
        angle = 0.0 if ikpt == 1 else angle_degrees(previous_diff, kdiff)
        kdiff_length = math.sqrt(np.vdot(kdiff, kdiff))

        if angle > LABEL_ANGLE_THRESHOLD and kdiff_length < DISCONTINUITY_THRESHOLD:
            special_positions.append(kline[ikpt - 1])

        if kdiff_length > DISCONTINUITY_THRESHOLD:
            kline.append(kline[ikpt - 1])
        else:
            kline.append(kline[ikpt - 1] + kdiff_length)

    for ikpt in range(1, nkpts):
        for iband, _ in enumerate(bands):
            bands[iband].append(kpoints[ikpt][1][iband])

    special_positions.append(kline[-1])
    if raw:
        np.savetxt(output_dir / "xklabel.dat", special_positions)

    return BandData(special_positions=special_positions, kline=kline, bands=bands)


def load_klabels(klabel_path: Path | None, expected: int) -> list[str]:
    if klabel_path is None:
        return [""] * expected

    labels = [line.strip() for line in klabel_path.read_text(encoding="utf-8").splitlines()]
    if len(labels) != expected:
        print(
            f"Warning: expected {expected} k-point labels but found {len(labels)} in {klabel_path}.",
            file=sys.stderr,
        )
        if len(labels) < expected:
            labels.extend([""] * (expected - len(labels)))
        else:
            labels = labels[:expected]
    return labels


def get_total_electrons(output_text: str) -> int:
    return int(round(extract_scalar(output_text, ELECTRONS_RE, "number of electrons")))


def determine_fermi(
    band_data: BandData,
    total_electrons: int,
    nspin: int,
    fermi_mode: int,
    fermi_user: float | None,
    n_up: int | None,
    n_dn: int | None,
) -> tuple[float, str]:
    bands = band_data.bands
    nkpts = len(bands[0])

    if nspin in (1, 4):
        vband = total_electrons if nspin == 4 else int(total_electrons / 2)
        if fermi_mode == 1:
            fermi = (max(bands[vband - 1]) + min(bands[vband])) * 0.5
        elif fermi_mode == 2:
            fermi = max(bands[vband - 1])
        else:
            assert fermi_user is not None
            fermi = fermi_user

        bandgap = min(bands[vband]) - max(bands[vband - 1])
        summary = f"Band gap = {bandgap:.6f} eV"
        return fermi, summary

    if n_up is None or n_dn is None:
        n_up = int(total_electrons / 2)
        n_dn = total_electrons - n_up
    elif (n_up + n_dn) != total_electrons:
        print(
            f"Warning: supplied spin electron counts ({n_up} + {n_dn}) do not match "
            f"the total electron count ({total_electrons}).",
            file=sys.stderr,
        )

    half = int(nkpts / 2)
    if fermi_mode == 1:
        fermi = (
            max(max(bands[n_up - 1][:half]), max(bands[n_dn - 1][half:]))
            + min(min(bands[n_up][:half]), min(bands[n_dn][half:]))
        ) * 0.5
    elif fermi_mode == 2:
        fermi = max(max(bands[n_up - 1][:half]), max(bands[n_dn - 1][half:]))
    else:
        assert fermi_user is not None
        fermi = fermi_user

    bandgap_up = min(bands[n_up][:half]) - max(bands[n_up - 1][:half])
    bandgap_dn = min(bands[n_dn][half:]) - max(bands[n_dn - 1][half:])
    bandgap = min(min(bands[n_up][:half]), min(bands[n_dn][half:])) - max(
        max(bands[n_up - 1][:half]), max(bands[n_dn - 1][half:])
    )
    summary = (
        f"Up band gap = {bandgap_up:.6f} eV, "
        f"Down band gap = {bandgap_dn:.6f} eV, "
        f"Band gap = {bandgap:.6f} eV"
    )
    return fermi, summary


def export_raw_data(
    band_data: BandData,
    fermi: float,
    nspin: int,
    name: str,
    output_dir: Path,
) -> None:
    bands = band_data.bands
    kline = band_data.kline
    nkpts = len(bands[0])

    if nspin in (1, 4):
        with (output_dir / f"{name}_bands.dat").open("w", encoding="utf-8") as handle:
            for band in bands:
                for xcoord, energy in zip(kline, band):
                    print(xcoord, energy - fermi, file=handle)
                handle.write("\n")
        return

    half = int(nkpts / 2)
    with (output_dir / f"{name}_bands_up.dat").open("w", encoding="utf-8") as handle:
        for band in bands:
            for xcoord, energy in zip(kline[:half], band[:half]):
                print(xcoord, energy - fermi, file=handle)
            handle.write("\n")

    with (output_dir / f"{name}_bands_dn.dat").open("w", encoding="utf-8") as handle:
        for band in bands:
            for xcoord, energy in zip(kline[:half], band[half:]):
                print(xcoord, energy - fermi, file=handle)
            handle.write("\n")


def decorate_axis(
    axis,
    band_data: BandData,
    labels: list[str],
    emin: float,
    emax: float,
    estep: float,
) -> None:
    axis.vlines(
        band_data.special_positions,
        -emin,
        emax,
        color="k",
        linewidth=0.7,
    )
    axis.plot(
        [band_data.special_positions[0], band_data.special_positions[-1]],
        [0, 0],
        "--",
        color="gray",
        linewidth=0.5,
    )
    axis.set_xlim([band_data.kline[0], band_data.kline[-1]])
    axis.set_ylim([-emin, emax])
    axis.set_xticks(band_data.special_positions)
    axis.set_xticklabels(labels)
    axis.set_ylabel(r"$E$ (eV)")
    axis.set_yticks(np.arange(-emin, emax + 0.0001, estep))


def plot_band_structure(
    band_data: BandData,
    fermi: float,
    labels: list[str],
    output_path: Path,
    name: str,
    emin: float,
    emax: float,
    estep: float,
    nspin: int,
) -> None:
    bands = band_data.bands
    kline = band_data.kline
    nkpts = len(bands[0])

    fig, ax = plt.subplots()
    axes = [ax]

    if nspin in (1, 4):
        for band in bands:
            ax.plot(kline, [energy - fermi for energy in band], "-", color="k", linewidth=1)
    else:
        half = int(nkpts / 2)
        fig_up, ax_up = plt.subplots()
        fig_dn, ax_dn = plt.subplots()
        axes.extend([ax_up, ax_dn])

        for band in bands:
            up = [energy - fermi for energy in band[:half]]
            dn = [energy - fermi for energy in band[half:]]
            ax.plot(kline[:half], up, "-", color="r", linewidth=1)
            ax.plot(kline[:half], dn, "-", color="b", linewidth=1)
            ax_up.plot(kline[:half], up, "-", color="r", linewidth=1)
            ax_dn.plot(kline[:half], dn, "-", color="b", linewidth=1)

    for axis in axes:
        decorate_axis(axis, band_data, labels, emin, emax, estep)

    fig.tight_layout(pad=0.2)
    base = output_path.parent / f"{output_path.name}_{name}"
    fig.savefig(f"{base}.png")
    fig.savefig(f"{base}.eps")

    if nspin == 2:
        fig_up.tight_layout(pad=0.2)
        fig_dn.tight_layout(pad=0.2)
        fig_up.savefig(f"{output_path.parent / f'{output_path.name}_up_{name}'}.png")
        fig_up.savefig(f"{output_path.parent / f'{output_path.name}_up_{name}'}.eps")
        fig_dn.savefig(f"{output_path.parent / f'{output_path.name}_dn_{name}'}.png")
        fig_dn.savefig(f"{output_path.parent / f'{output_path.name}_dn_{name}'}.eps")


def main(argv: list[str] | None = None) -> int:
    config = parse_cli(argv or sys.argv[1:])
    kpoints, output_text = read_bands(config.output)
    band_data = create_plot_array(kpoints, config.nspin, config.raw, config.output.parent)
    total_electrons = get_total_electrons(output_text)
    fermi, gap_summary = determine_fermi(
        band_data,
        total_electrons,
        config.nspin,
        config.fermi_mode,
        config.fermi_user,
        config.n_up,
        config.n_dn,
    )
    labels = load_klabels(config.klabels, len(band_data.special_positions))

    print(f"Parsed QE output: {config.output}")
    print(f"Number of electrons: {total_electrons}")
    print(f"Number of k-points: {len(kpoints)}")
    print(f"Number of bands: {len(band_data.bands)}")
    print(f"Fermi energy setting: {config.fermi_mode}")
    print(f"Fermi energy: {fermi:.6f} eV")
    print(gap_summary)

    if config.raw:
        export_raw_data(band_data, fermi, config.nspin, config.name, config.output.parent)

    if config.plot:
        plot_band_structure(
            band_data,
            fermi,
            labels,
            config.output,
            config.name,
            config.emin,
            config.emax,
            config.estep,
            config.nspin,
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
