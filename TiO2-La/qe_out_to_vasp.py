#!/usr/bin/env python3
"""Read a Quantum ESPRESSO output file with ASE and write the final structure as VASP."""

from __future__ import annotations

import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Read the last structure from a Quantum ESPRESSO output and export it "
            "as a VASP POSCAR-style file ending in .vasp."
        )
    )
    parser.add_argument("qe_output", help="Path to the Quantum ESPRESSO output file, e.g. qe.out")
    parser.add_argument(
        "-o",
        "--output",
        help="Output filename. If omitted, the script uses the input basename with a .vasp suffix.",
    )
    return parser.parse_args()


def ensure_vasp_suffix(path: Path) -> Path:
    return path if path.suffix == ".vasp" else path.with_suffix(".vasp")


def main() -> None:
    args = parse_args()

    qe_output = Path(args.qe_output).expanduser().resolve()
    if not qe_output.is_file():
        raise FileNotFoundError(f"QE output file not found: {qe_output}")

    output = Path(args.output) if args.output else qe_output.with_suffix(".vasp")
    output = ensure_vasp_suffix(output.expanduser())

    from ase.io import read, write

    # Use the last image in the QE output, which is the relaxed structure after the final SCF.
    atoms = read(qe_output, format="espresso-out", index=-1)
    atoms.wrap()

    write(output, atoms, format="vasp", direct=True, vasp5=True, sort=False)
    print(f"Wrote {output}")


if __name__ == "__main__":
    main()
