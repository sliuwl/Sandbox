#!/usr/bin/env python3
"""Format fatband data from Quantum ESPRESSO projwfc.x output.

This script parses:
1. projwfc.out   - atomic state information (element, orbital, atom number)
2. fatband.projwfc_up/down - raw projection weights

And writes formatted data files for easier plotting.

USAGE:
    python3 qe_format_fatbands.py [--input PROJWFC] [--proj PROJ_FILE] [--output OUTPUT]

OUTPUT FILES:
    <output>.npy      - Projection data (shape: nlorbs x nks x nbands)
    <output>.projs    - Auto-generated projection definitions
    <output>.summary  - Human-readable summary of available states
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

try:
    import numpy as np
except ImportError as exc:
    raise SystemExit(
        "numpy is required. Install it in the same Python environment used to "
        "run this script, for example:\n"
        "  python3 -m pip install numpy"
    ) from exc


L_TO_ORBITAL = {0: "s", 1: "p", 2: "d", 3: "f", 4: "g"}

# Pattern to match: "state #   1: atom   1 (Ti ), wfc  1 (l=0 m= 1)"
STATE_RE = re.compile(
    r"state #\s*(\d+):\s*atom\s*(\d+)\s*\(([A-Za-z]+)\s*\),.*?l=(\d+)",
    re.S,
)

COLORS = [
    "tab:red",
    "tab:blue",
    "tab:green",
    "tab:orange",
    "tab:purple",
    "tab:brown",
    "tab:pink",
    "tab:gray",
    "tab:olive",
    "tab:cyan",
]


def parse_projwfc_out(projwfc_out_file: str | Path) -> list[dict]:
    """Parse projwfc.out to extract atomic state information."""
    projwfc_out_file = Path(projwfc_out_file)
    if not projwfc_out_file.is_file():
        raise SystemExit(f"ERROR: projwfc output not found: {projwfc_out_file}")

    print(f"Parsing {projwfc_out_file}...")
    content = projwfc_out_file.read_text(encoding="utf-8", errors="replace")

    states = []
    for match in STATE_RE.finditer(content):
        state_num = int(match.group(1))
        atom_num = int(match.group(2))
        element = match.group(3).strip()
        l = int(match.group(4))
        orbital = L_TO_ORBITAL.get(l, f"l{l}")
        states.append(
            {
                "state_num": state_num,
                "atom_num": atom_num,
                "element": element,
                "orbital": orbital,
                "l": l,
            }
        )

    if not states:
        raise SystemExit("ERROR: no atomic states found in projwfc output")

    print(f"Found {len(states)} atomic states")
    return states


def parse_fatband_proj(proj_file: str | Path) -> tuple[int, int, int, np.ndarray]:
    """Parse fatband.projwfc_up/down to extract projection data."""
    proj_file = Path(proj_file)
    if not proj_file.is_file():
        raise SystemExit(f"ERROR: projection file not found: {proj_file}")

    print(f"Parsing {proj_file}...")
    lines = proj_file.read_text(encoding="utf-8", errors="replace").splitlines()

    # Find the line with nlorbs, nkstot, nbnd.
    nlorbs = nks = nbands = None
    for i, line in enumerate(lines):
        parts = line.split()
        if len(parts) == 3:
            try:
                a, b, c = int(parts[0]), int(parts[1]), int(parts[2])
                # Heuristic ranges for nlorbs, nks, nbands.
                if 5 < a < 500 and 10 < b < 5000 and 5 < c < 500:
                    nlorbs, nks, nbands = a, b, c
                    param_line = i + 1
                    print(
                        f"Found parameters at line {param_line}: "
                        f"nlorbs={nlorbs}, nks={nks}, nbands={nbands}"
                    )
                    break
            except ValueError:
                continue

    if nlorbs is None:
        raise SystemExit("ERROR: could not find nlorbs, nks, nbands parameters")

    projections = np.zeros([nlorbs, nks, nbands], dtype=np.float64)

    # The spin-flags line sits between the parameter line and the first state header.
    current_line = param_line + 1

    for istate in range(nlorbs):
        if current_line >= len(lines):
            break
        current_line += 1  # skip state info header line

        for ik in range(nks):
            for ib in range(nbands):
                if current_line >= len(lines):
                    break
                parts = lines[current_line].split()
                if len(parts) >= 3:
                    try:
                        projections[istate, ik, ib] = float(parts[2])
                    except (ValueError, IndexError):
                        pass
                current_line += 1

    print(f"Loaded projection data: shape = {projections.shape}")
    print(f"  Non-zero values: {np.count_nonzero(projections)}")
    print(f"  Max value: {projections.max():.4f}")
    return nlorbs, nks, nbands, projections


def generate_projs_file(states: list[dict], output_file: str | Path) -> dict:
    """Generate a .projs file listing available element-orbital combinations."""
    groups: dict[str, list[int]] = {}
    for s in states:
        key = f"{s['element']} {s['orbital']}"
        groups.setdefault(key, []).append(s["state_num"])

    output_file = Path(output_file)
    with output_file.open("w", encoding="utf-8") as handle:
        handle.write(f"{len(groups)}\n")
        for i, (key, state_nums) in enumerate(groups.items()):
            color = COLORS[i % len(COLORS)]
            handle.write(f"{key} tab:{color.split(':')[1]}\n")

    print(f"\nGenerated projs file: {output_file}")
    print("Available projections:")
    for key, state_nums in groups.items():
        print(f"  {key}: states {state_nums}")
    return groups


def print_and_save_summary(
    states: list[dict], proj_file: str | Path, output_base: str | Path
) -> dict:
    """Print and save a human-readable summary of available states."""
    output_base = Path(output_base)

    elements: dict[str, dict] = {}
    for s in states:
        elem = s["element"]
        entry = elements.setdefault(
            elem, {"orbitals": set(), "atoms": set(), "states": []}
        )
        entry["orbitals"].add(s["orbital"])
        entry["atoms"].add(s["atom_num"])
        entry["states"].append(s["state_num"])

    lines = []
    lines.append("=" * 60)
    lines.append("FATBANDS DATA SUMMARY")
    lines.append("=" * 60)
    lines.append("")
    lines.append(f"Generated from: {proj_file}")
    lines.append("Output files:")
    lines.append(f"  - {output_base}.npy       : Projection data (NumPy array)")
    lines.append(f"  - {output_base}.projs    : Projection definitions")
    lines.append(f"  - {output_base}.summary : This file")
    lines.append("")
    lines.append("-" * 60)
    lines.append("NUMPY FILE STRUCTURE (.npy)")
    lines.append("-" * 60)
    lines.append("")
    lines.append("The projection data is stored as a 3D NumPy array with shape:")
    lines.append("  (nlorbs, nks, nbands)")
    lines.append("")
    lines.append("Where:")
    lines.append("  - nlorbs  : Number of atomic orbitals (projected states)")
    lines.append("  - nks     : Number of k-points along the band path")
    lines.append("  - nbands  : Number of electronic bands")
    lines.append("")
    lines.append("Values represent the projection weight (0 to 1) of each band")
    lines.append("at each k-point onto each atomic orbital.")
    lines.append("")
    lines.append("IMPORTANT: Indexing note")
    lines.append("  - State numbers shown below are 1-based (matching projwfc.out)")
    lines.append("  - When using in Python/NumPy, SUBTRACT 1 for 0-based indexing")
    lines.append("")
    lines.append("Usage in Python:")
    lines.append("  import numpy as np")
    lines.append(f"  proj = np.load('{output_base}.npy')")
    lines.append("  # proj[state-1, kpoint-1, band-1] gives weight")
    lines.append("")
    lines.append("Example: Get Ti d states (states 6-10 in 1-based = indices 5-9 in 0-based):")
    lines.append("  ti_d_0based = [5, 6, 7, 8, 9]  # subtract 1 from state numbers")
    lines.append("  weight = proj[ti_d_0based, :, :].sum(axis=0)  # sum over states")
    lines.append("")
    lines.append("-" * 60)
    lines.append("AVAILABLE ATOMIC STATES")
    lines.append("-" * 60)
    lines.append("")
    lines.append("NOTE: By default, selecting an element/orbital (e.g., 'O p') includes")
    lines.append("ALL atoms of that type. To select specific atoms, use the format:")
    lines.append("  Ti d 1       # only atom 1")
    lines.append("  Pb d 1,2     # atoms 1 and 2")
    lines.append("")
    lines.append("The projs file format is:")
    lines.append("  <num_projections>")
    lines.append("  <element> <orbital> [<atom_numbers>] <color>")
    lines.append("")
    lines.append("Examples:")
    lines.append("  # All Ti d orbitals:")
    lines.append("  1")
    lines.append("  Ti d tab:red")
    lines.append("")
    lines.append("  # Only Ti atom 1 d orbitals:")
    lines.append("  1")
    lines.append("  Ti d 1 tab:red")
    lines.append("")
    lines.append("  # Combined: Ti d (all) + O p (only atom 3):")
    lines.append("  2")
    lines.append("  Ti d tab:red")
    lines.append("  O p 3 tab:blue")

    for elem in sorted(elements.keys()):
        data = elements[elem]
        lines.append(f"\n{elem}:")
        lines.append(f"  Orbitals: {', '.join(sorted(data['orbitals']))}")
        lines.append(f"  Atoms: {sorted(data['atoms'])}")
        lines.append(f"  State numbers: {data['states']}")

    lines.append("")
    lines.append("-" * 60)
    lines.append("HOW TO USE WITH qe_plot_fatbands.py")
    lines.append("-" * 60)
    lines.append("")
    lines.append("1. Create a projection file (plot.projs) with format:")
    lines.append("   <num_projections>")
    lines.append("   <element> <orbital> <color>")
    lines.append("")
    lines.append("   Example:")
    lines.append("   2")
    lines.append("   Ti d tab:red")
    lines.append("   Pb d tab:blue")
    lines.append("")
    lines.append("2. Run qe_plot_fatbands.py with fatband options:")
    lines.append("   python3 qe_plot_fatbands.py -o bands.out \\")
    lines.append("       --fatband \\")
    lines.append("       --proj plot.projs \\")
    lines.append(f"       --proj-data {output_base}.npy \\")
    lines.append("       -e 5 5 2")
    lines.append("")

    summary_text = "\n".join(lines)
    print(summary_text)

    summary_file = output_base.with_suffix(".summary")
    summary_file.write_text(summary_text, encoding="utf-8")
    print(f"\nSaved summary to: {summary_file}")
    return elements


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Format fatband data from QE projwfc.x output.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Example:\n"
            "  python3 qe_format_fatbands.py -i projwfc.out -p fatband.projwfc_up -o fatband_formatted"
        ),
    )
    parser.add_argument(
        "-i",
        "--input",
        default="projwfc.out",
        help="projwfc.x output file (default: projwfc.out)",
    )
    parser.add_argument(
        "-p",
        "--proj",
        default="fatband.projwfc_up",
        help="Raw projection file (default: fatband.projwfc_up)",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="fatband_formatted",
        help="Output base name (default: fatband_formatted)",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Print detailed diagnostics",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    input_path = Path(args.input).expanduser().resolve()
    proj_path = Path(args.proj).expanduser().resolve()

    # Default output next to the projwfc output unless an absolute path is given.
    output_base = Path(args.output)
    if not output_base.is_absolute():
        output_base = input_path.parent / output_base

    states = parse_projwfc_out(input_path)
    print_and_save_summary(states, proj_path, output_base)
    groups = generate_projs_file(states, output_base.with_suffix(".projs"))

    nlorbs, nks, nbands, projections = parse_fatband_proj(proj_path)
    if projections is None:
        return 1

    np.save(output_base.with_suffix(".npy"), projections)
    print(f"\nSaved projection data to: {output_base}.npy")
    print(f"  Shape: {projections.shape} (nlorbs, nks, nbands)")
    print(f"  Size: {projections.nbytes / 1024:.1f} KB")

    print("\n" + "=" * 60)
    print("NEXT STEPS")
    print("=" * 60)
    print("1. Inspect the generated .summary and .projs files.")
    print("2. Customize the .projs file if needed.")
    print("3. Plot fatbands with qe_plot_fatbands.py, for example:")
    print(
        f"python3 qe_plot_fatbands.py -o bands.out --fatband "
        f"--proj {output_base}.projs --proj-data {output_base}.npy -e 5 5 2"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
