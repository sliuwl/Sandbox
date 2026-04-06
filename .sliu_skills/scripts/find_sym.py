#!/usr/bin/env python3
"""Analyze symmetry for structure files and write symmetrized outputs.

Supports VASP POSCAR/CONTCAR, CIF, and other formats supported by pymatgen.
The input file may have any name as long as the content follows a supported format.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from pymatgen.core import Structure
from pymatgen.io.cif import CifWriter
from pymatgen.io.vasp.inputs import Poscar
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer


DEFAULT_SYMPREC = 0.005
DEFAULT_ANGLE_TOLERANCE = 5.0
OUTPUT_DECIMAL_PLACES = 8


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description=(
            "Read a POSCAR-format structure, analyze its symmetry, and write "
            "symmetrized outputs in VASP, CIF, and Quantum ESPRESSO template "
            "formats."
        )
    )
    parser.add_argument(
        "input_file",
        type=Path,
        help="Path to a structure file (CIF, POSCAR, CONTCAR, etc.). The file name can be arbitrary.",
    )
    parser.add_argument(
        "-s",
        "--symprec",
        type=float,
        default=DEFAULT_SYMPREC,
        help=f"Distance tolerance used for symmetry finding (default: {DEFAULT_SYMPREC}).",
    )
    parser.add_argument(
        "-a",
        "--angle-tolerance",
        type=float,
        default=DEFAULT_ANGLE_TOLERANCE,
        help=(
            "Angle tolerance in degrees used for symmetry finding "
            f"(default: {DEFAULT_ANGLE_TOLERANCE})."
        ),
    )
    parser.add_argument(
        "-k",
        "--structure-kind",
        choices=("conventional", "refined", "primitive"),
        default="conventional",
        help=(
            "Type of symmetrized structure to write. "
            "The default matches the original script."
        ),
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        type=Path,
        default=None,
        help="Directory for output files. Defaults to the input file directory.",
    )
    parser.add_argument(
        "-p",
        "--prefix",
        default=None,
        help="Custom prefix for output files. Defaults to the input file stem.",
    )
    parser.add_argument(
        "--qe-coordinates",
        choices=("crystal", "angstrom"),
        default="crystal",
        help="Coordinate style for the Quantum ESPRESSO structure file (default: crystal).",
    )
    parser.add_argument(
        "--skip-cif",
        action="store_true",
        help="Do not write the symmetrized CIF file.",
    )
    parser.add_argument(
        "--skip-report",
        action="store_true",
        help="Do not write the text symmetry summary.",
    )
    return parser.parse_args()


def sanitize_label(text: str) -> str:
    """Return a filesystem-safe label derived from a symmetry symbol."""
    safe_text = re.sub(r"[^A-Za-z0-9._-]+", "-", text.strip())
    return safe_text.strip("-") or "unknown"


def get_reduced_formula(structure) -> str:
    """Return a readable reduced formula, preferring IUPAC ordering when available."""
    composition = structure.composition
    try:
        return composition.get_reduced_formula_and_factor(iupac_ordering=True)[0]
    except TypeError:
        return composition.reduced_formula


def read_structure(input_file: Path):
    """Read a structure file in any supported format (POSCAR, CIF, etc.).

    Automatically detects format based on file extension and content.
    """
    # Try pymatgen's auto-detection first (works for CIF, POSCAR, and many others)
    try:
        return Structure.from_file(str(input_file))
    except Exception:
        pass

    # Fallback: try POSCAR explicitly (for files without proper extension)
    try:
        return Poscar.from_file(str(input_file)).structure
    except Exception as exc:
        raise SystemExit(
            f"Failed to read structure from '{input_file}': {exc}\n"
            f"Supported formats: CIF, POSCAR, CONTCAR, and other pymatgen-supported formats"
        ) from exc


def get_symmetrized_structure(analyzer: SpacegroupAnalyzer, structure_kind: str):
    """Return the requested symmetrized structure."""
    if structure_kind == "conventional":
        return analyzer.get_conventional_standard_structure()
    if structure_kind == "refined":
        return analyzer.get_refined_structure()
    if structure_kind == "primitive":
        return analyzer.get_primitive_standard_structure()
    raise ValueError(f"Unsupported structure kind: {structure_kind}")


def build_output_root(
    input_file: Path,
    prefix: str | None,
    output_dir: Path,
    structure_kind: str,
    space_group_number: int,
    space_group_symbol: str,
) -> Path:
    """Build a descriptive base name shared by all generated files."""
    base_name = prefix or input_file.stem
    space_group_tag = sanitize_label(space_group_symbol)
    file_stem = (
        f"{base_name}_symmetrized_{structure_kind}_"
        f"sg{space_group_number:03d}_{space_group_tag}"
    )
    return output_dir / file_stem


def format_qe_site_line(site, coordinate_mode: str) -> str:
    """Format one atomic site line for the Quantum ESPRESSO structure file."""
    species = getattr(site.specie, "symbol", site.species_string)
    coordinates = site.frac_coords if coordinate_mode == "crystal" else site.coords
    return f"{species:<4} " + " ".join(
        f"{value:>14.{OUTPUT_DECIMAL_PLACES}f}" for value in coordinates
    )


def write_qe_structure_file(structure, output_file: Path, coordinate_mode: str) -> None:
    """Write a QE-friendly structure snippet."""
    lines = ["CELL_PARAMETERS (angstrom)"]
    for lattice_vector in structure.lattice.matrix:
        lines.append(
            " ".join(f"{value:>14.{OUTPUT_DECIMAL_PLACES}f}" for value in lattice_vector)
        )

    lines.append("")
    lines.append(f"ATOMIC_POSITIONS ({coordinate_mode})")
    for site in structure:
        lines.append(format_qe_site_line(site, coordinate_mode))

    output_file.write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_symmetry_report(
    input_file: Path,
    analyzer: SpacegroupAnalyzer,
    input_structure,
    symmetrized_structure,
    args: argparse.Namespace,
    written_files: list[Path],
) -> str:
    """Create a readable text summary of the symmetry analysis."""
    lines = [
        "Symmetry analysis summary",
        "=" * 25,
        f"Input file: {input_file}",
        f"Reduced formula: {get_reduced_formula(input_structure)}",
        f"Input sites: {len(input_structure)}",
        f"Output sites: {len(symmetrized_structure)}",
        f"Symmetry tolerance (symprec): {args.symprec}",
        f"Angle tolerance: {args.angle_tolerance}",
        f"Requested output structure: {args.structure_kind}",
        f"Space group symbol: {analyzer.get_space_group_symbol()}",
        f"Space group number: {analyzer.get_space_group_number()}",
        f"Crystal system: {analyzer.get_crystal_system()}",
        f"Lattice type: {analyzer.get_lattice_type()}",
        f"Point group: {analyzer.get_point_group_symbol()}",
        "",
        "Generated files:",
    ]
    lines.extend(f"- {path}" for path in written_files)
    return "\n".join(lines) + "\n"


def main() -> int:
    """Run the symmetry analysis workflow."""
    args = parse_args()
    input_file = args.input_file.expanduser().resolve()

    if not input_file.is_file():
        raise SystemExit(f"Input file does not exist: {input_file}")

    output_dir = (args.output_dir or input_file.parent).expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    input_structure = read_structure(input_file)
    analyzer = SpacegroupAnalyzer(
        input_structure,
        symprec=args.symprec,
        angle_tolerance=args.angle_tolerance,
    )

    symmetrized_structure = get_symmetrized_structure(analyzer, args.structure_kind)
    space_group_symbol = analyzer.get_space_group_symbol()
    space_group_number = analyzer.get_space_group_number()

    output_root = build_output_root(
        input_file=input_file,
        prefix=args.prefix,
        output_dir=output_dir,
        structure_kind=args.structure_kind,
        space_group_number=space_group_number,
        space_group_symbol=space_group_symbol,
    )

    comment = (
        f"{get_reduced_formula(symmetrized_structure)} | "
        f"{args.structure_kind} | {space_group_symbol} ({space_group_number})"
    )

    poscar_file = output_root.with_suffix(".vasp")
    poscar_text = Poscar(symmetrized_structure, comment=comment).get_string(
        significant_figures=OUTPUT_DECIMAL_PLACES
    )
    poscar_file.write_text(poscar_text + "\n", encoding="utf-8")

    written_files = [poscar_file]

    if not args.skip_cif:
        cif_file = output_root.with_suffix(".cif")
        CifWriter(
            symmetrized_structure,
            significant_figures=OUTPUT_DECIMAL_PLACES,
        ).write_file(str(cif_file))
        written_files.append(cif_file)

    qe_file = output_dir / f"{output_root.name}.struc.in"
    write_qe_structure_file(symmetrized_structure, qe_file, args.qe_coordinates)
    written_files.append(qe_file)

    if not args.skip_report:
        report_file = output_root.with_suffix(".symmetry.txt")
        written_files.append(report_file)

    report_text = build_symmetry_report(
        input_file=input_file,
        analyzer=analyzer,
        input_structure=input_structure,
        symmetrized_structure=symmetrized_structure,
        args=args,
        written_files=written_files,
    )

    if not args.skip_report:
        report_file.write_text(report_text, encoding="utf-8")

    # Keep the terminal output concise but informative for scripting and manual use.
    print(report_text, end="")

    return 0


if __name__ == "__main__":
    sys.exit(main())
