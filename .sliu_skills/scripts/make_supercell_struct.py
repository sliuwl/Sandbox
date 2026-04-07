#!/usr/bin/env python3
"""Create a supercell from a VASP structure and export QE-ready structure text."""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
from ase.io import read, write


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Create a supercell from a VASP file and write both a VASP file "
            "and a QE-style struct.in file."
        )
    )
    parser.add_argument(
        "input_vasp",
        nargs="?",
        default="qe.vasp",
        help="Input VASP structure file (default: qe.vasp).",
    )
    parser.add_argument(
        "-r",
        "--repeat",
        nargs=3,
        type=int,
        default=[1, 1, 2],
        metavar=("NX", "NY", "NZ"),
        help="Supercell repetition along a, b, c (default: 1 1 2).",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="Output VASP filename (default: <input_stem>_<NX>x<NY>x<NZ>.vasp).",
    )
    parser.add_argument(
        "--struct-output",
        type=Path,
        default=Path("struct.in"),
        help="Output QE structure filename (default: struct.in).",
    )
    return parser.parse_args()


def default_vasp_name(input_path: Path, repeat: tuple[int, int, int]) -> Path:
    nx, ny, nz = repeat
    return input_path.with_name(f"{input_path.stem}_{nx}x{ny}x{nz}.vasp")


def sort_atoms(atoms, species_order):
    scaled = atoms.get_scaled_positions(wrap=True)
    symbol_rank = np.array([species_order[sym] for sym in atoms.get_chemical_symbols()])
    order = np.lexsort((scaled[:, 2], scaled[:, 1], scaled[:, 0], symbol_rank))
    ordered = atoms[order]
    ordered.set_cell(atoms.get_cell())
    ordered.set_pbc(atoms.get_pbc())
    ordered.wrap()
    return ordered


def write_struct_in(atoms, output_path: Path) -> None:
    cell = atoms.get_cell()
    scaled = atoms.get_scaled_positions(wrap=True)
    symbols = atoms.get_chemical_symbols()

    lines = ["CELL_PARAMETERS (angstrom)"]
    for vector in cell:
        lines.append(f"{vector[0]:16.8f} {vector[1]:16.8f} {vector[2]:16.8f}")

    lines.append("")
    lines.append("ATOMIC_POSITIONS (crystal)")
    for symbol, pos in zip(symbols, scaled):
        lines.append(f"{symbol:2s} {pos[0]:16.8f} {pos[1]:16.8f} {pos[2]:16.8f}")

    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    args = parse_args()

    input_path = Path(args.input_vasp).expanduser().resolve()
    repeat = tuple(args.repeat)
    vasp_output = (
        args.output.expanduser()
        if args.output
        else default_vasp_name(input_path, repeat)
    )
    struct_output = args.struct_output.expanduser()

    atoms = read(input_path)
    species_order = {
        symbol: index for index, symbol in enumerate(dict.fromkeys(atoms.get_chemical_symbols()))
    }
    supercell = atoms.repeat(repeat)
    supercell.wrap()
    supercell = sort_atoms(supercell, species_order)

    write(vasp_output, supercell, format="vasp", direct=True, sort=False, vasp5=True)
    write_struct_in(supercell, struct_output)

    print(f"Input: {input_path.name}")
    print(f"Repeat: {repeat[0]}x{repeat[1]}x{repeat[2]}")
    print(f"Wrote VASP: {vasp_output}")
    print(f"Wrote QE structure: {struct_output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
