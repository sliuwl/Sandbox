#!/usr/bin/env python3
"""Create a doped supercell by replacing atoms with dopants.

Usage:
    make_doped_supercell.py <input> <dopant> <n_dopants> [options]

Arguments:
    input              Input structure file (CIF, POSCAR, etc.)
    dopant             Dopant element symbol (e.g., La, Nb, Fe)
    n_dopants         Number of atoms to replace with dopant

Options:
    -r, --repeat REPEAT    Supercell repetition (e.g., "2 2 1" or "2 1 1")
    -o, --output FILE      Output file (default: doped_supercell.vasp)
    -s, --site SITE        Site to replace: first, last, random (default: first)
    -k, --kpoints K P O   K-points (default: 6 6 6)
    -e, --ecutwfc E        Plane-wave cutoff in Ry (default: 50)
    --generate-qe          Generate QE vc-relax.in file

Examples:
    # Create 2x2x1 anatase supercell with 1 La dopant
    make_doped_supercell.py anatase.cif La 1 -r "2 2 1" -o La_anatase.vasp

    # Create 2x1x1 rutile supercell with 2 Nb dopants
    make_doped_supercell.py rutile.cif Nb 2 -r "2 1 1" -o Nb_rutile.vasp

    # Generate QE input files
    make_doped_supercell.py anatase.cif La 1 --generate-qe
"""

import argparse
import random
import sys
from pathlib import Path

from ase.io import read, write
from ase import Atoms


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create doped supercell and optionally generate QE input"
    )
    parser.add_argument("input", type=Path, help="Input structure file")
    parser.add_argument("dopant", help="Dopant element symbol")
    parser.add_argument("n_dopants", type=int, help="Number of atoms to replace")
    parser.add_argument("-r", "--repeat", default="1 1 1",
                        help="Supercell repetition (e.g., '2 2 1')")
    parser.add_argument("-o", "--output", type=Path, default=Path("doped_supercell.vasp"),
                        help="Output file")
    parser.add_argument("-s", "--site", choices=["first", "last", "random"],
                        default="first", help="Which sites to replace")
    parser.add_argument("-k", "--kpoints", nargs=3, type=int, default=[6, 6, 6],
                        help="K-points grid (default: 6 6 6)")
    parser.add_argument("-e", "--ecutwfc", type=float, default=50.0,
                        help="Plane-wave cutoff in Ry (default: 50)")
    parser.add_argument("--generate-qe", action="store_true",
                        help="Generate QE vc-relax.in file")
    return parser.parse_args()


def get_host_indices(atoms: Atoms, site: str, n: int) -> list[int]:
    """Get indices of atoms to replace (Ti by default, or first cation)."""
    # Get all Ti indices, or if no Ti, take first n non-dopant atoms
    symbols = atoms.get_chemical_symbols()
    ti_indices = [i for i, s in enumerate(symbols) if s != 'O']

    if not ti_indices:
        ti_indices = list(range(len(atoms)))

    if site == "first":
        return ti_indices[:n]
    elif site == "last":
        return ti_indices[-n:]
    else:  # random
        return random.sample(ti_indices, n)


def generate_qe_input(atoms: Atoms, dopant: str, args: argparse.Namespace) -> str:
    """Generate QE vc-relax.in content."""
    # Get unique elements and their masses
    symbols = list(set(atoms.get_chemical_symbols()))
    symbols.sort()  # Consistent ordering

    # Masses (common dopants)
    mass_map = {
        "La": 138.905, "Nb": 92.906, "Fe": 55.845, "V": 50.942,
        "Cr": 51.996, "Mn": 54.938, "Co": 58.933, "Ni": 58.693,
        "Cu": 63.546, "Zn": 65.38, "Sr": 87.62, "Ba": 137.327,
    }
    default_mass = 47.867  # Ti default

    # Build ATOMIC_SPECIES
    species_lines = []
    for sym in symbols:
        mass = mass_map.get(sym, default_mass)
        uspp = f"{sym.lower()}_pbesol_v1.uspp.F.UPF"
        species_lines.append(f"{sym:2s} {mass:8.3f} {uspp}")

    prefix = f"{dopant.lower()}_{args.output.stem.split('_')[0]}"
    kpts = f"{args.kpoints[0]} {args.kpoints[1]} {args.kpoints[2]}"

    # Get cell parameters
    cell = atoms.get_cell()
    cell_lines = []
    for i in range(3):
        cell_lines.append(
            f"{cell[i,0]:16.12f} {cell[i,1]:16.12f} {cell[i,2]:16.12f}"
        )

    # Get fractional positions
    scaled = atoms.get_scaled_positions()
    pos_lines = []
    for sym, pos in zip(atoms.get_chemical_symbols(), scaled):
        pos_lines.append(f"{sym:2s} {pos[0]:16.12f} {pos[1]:16.12f} {pos[2]:16.12f}")

    qe_input = f"""&CONTROL
  calculation    = 'vc-relax',
  prefix         = '{prefix}',
  pseudo_dir     = './psps',
  outdir         = './tmp/',
  tstress        = .true.,
  tprnfor        = .true.,
  etot_conv_thr  = 1.0d-5,
  forc_conv_thr  = 1.0d-4,
  nstep          = 100
/

&SYSTEM
  nosym          = .true.
  ibrav          = 0,
  nat            = {len(atoms)},
  ntyp           = {len(symbols)},
  ecutwfc        = {args.ecutwfc}.0,
  ecutrho        = {args.ecutwfc * 5}.0,
  occupations    = 'smearing',
  smearing       = 'mv',
  degauss        = 0.001
/

&ELECTRONS
  mixing_beta    = 0.5,
  conv_thr       = 1.0d-8
/

&IONS
  upscale        = 100.D0
/

&CELL
  cell_dynamics  = 'bfgs',
  press_conv_thr = 0.5d0,
  cell_dofree    = 'all'
/

ATOMIC_SPECIES
{chr(10).join(species_lines)}

K_POINTS {{automatic}}
{kpts} 0 0 0

CELL_PARAMETERS (angstrom)
{chr(10).join(cell_lines)}

ATOMIC_POSITIONS (crystal)
{chr(10).join(pos_lines)}
"""
    return qe_input


def main() -> int:
    args = parse_args()

    # Read structure
    if not args.input.exists():
        print(f"Error: Input file not found: {args.input}")
        return 1

    atoms = read(args.input)
    print(f"Loaded: {args.input.name} ({len(atoms)} atoms)")
    print(f"  Composition: {atoms.get_chemical_formula()}")
    print(f"  Cell: {atoms.cell.cellpar()[:3]}")

    # Create supercell
    repeat = [int(x) for x in args.repeat.split()]
    if repeat != [1, 1, 1]:
        atoms = atoms.repeat(repeat)
        print(f"Supercell ({args.repeat}): {len(atoms)} atoms")

    # Replace atoms with dopant
    indices = get_host_indices(atoms, args.site, args.n_dopants)
    symbols = list(atoms.get_chemical_symbols())
    for i in indices:
        symbols[i] = args.dopant
    atoms.set_chemical_symbols(symbols)

    print(f"Replaced {args.n_dopants} atom(s) with {args.dopant}")
    print(f"  Composition: {atoms.get_chemical_formula()}")

    # Save VASP
    write(args.output, atoms)
    print(f"Saved: {args.output}")

    # Generate QE input if requested
    if args.generate_qe:
        qe_file = args.output.with_suffix(".vasp").with_name(
            args.output.stem + "_vc-relax.in"
        )
        qe_content = generate_qe_input(atoms, args.dopant, args)
        qe_file.write_text(qe_content)
        print(f"Saved: {qe_file}")

    return 0


if __name__ == "__main__":
    sys.exit(main())