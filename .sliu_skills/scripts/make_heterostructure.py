#!/usr/bin/env python3
"""Create heterostructure / superlattice by stacking 2D materials.

Usage:
    make_heterostructure.py <bottom> <top> [options]

Options:
    -o, --output FILE        Output file (default: heterostructure.vasp)
    -n, --nlayers N          Number of unit cells of top layer (default: 1)
    -g, --gap ANG            Gap between layers in Angstrom (default: 3.0)
    -r, --ref REF            Reference for ab lattice: first, last, or average (default: first)
    -b, --bottom-term ATOM   Bottom termination: O or Ti (for oxides)
    -t, --top-term ATOM      Top termination: O or Ti (for oxides)

Examples:
    # Simple: Ca2F2 + TiO2 (TiO2 2 unit cells)
    make_heterostructure.py Ca2F2.vasp TiO2.cif -o sandwich.vasp

    # O-terminated TiO2 at both interfaces
    make_heterostructure.py Ca2F2.vasp TiO2.cif --bottom-term O --top-term O -n 2 -o sandwich.vasp
"""

import argparse
import sys
from pathlib import Path

import numpy as np
from ase.io import read, write
from ase import Atoms


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create heterostructure by stacking 2D materials")
    parser.add_argument('bottom', type=Path, help='Bottom layer (2D material)')
    parser.add_argument('top', type=Path, help='Top layer')
    parser.add_argument('-o', '--output', type=Path, default=Path('heterostructure.vasp'),
                        help='Output file')
    parser.add_argument('-n', '--nlayers', type=int, default=1,
                        help='Number of unit cells of top layer in c direction')
    parser.add_argument('-g', '--gap', type=float, default=3.0,
                        help='Gap between layers (Angstrom)')
    parser.add_argument('-r', '--ref', choices=['first', 'last', 'average'], default='first',
                        help='Reference for ab lattice')
    parser.add_argument('-b', '--bottom-term', choices=['O', 'Ti', 'auto'], default='auto',
                        help='Bottom termination of top layer')
    parser.add_argument('-t', '--top-term', choices=['O', 'Ti', 'auto'], default='auto',
                        help='Top termination of top layer')
    return parser.parse_args()


def flip_termination(atoms, term_atom):
    """Flip the structure to switch termination.

    For TiO2: original has Ti at one end, O at the other.
    To flip: reverse the atom order in c direction.
    """
    # Get positions sorted by z
    pos = atoms.positions.copy()
    symbols = list(atoms.get_chemical_symbols())

    # Get unique z levels (ordering by position)
    z_sorted = sorted([(p[2], i) for i, p in enumerate(pos)])

    # Reconstruct: reverse the order (flip upside down)
    reversed_indices = [i for z, i in reversed(z_sorted)]

    new_pos = np.array([pos[i] for i in reversed_indices])
    new_sym = [symbols[i] for i in reversed_indices]

    # Now shift so it starts at 0
    z_min = new_pos[:, 2].min()
    new_pos[:, 2] = new_pos[:, 2] - z_min

    # Create new atoms
    new_atoms = Atoms(symbols=new_sym, positions=new_pos, cell=atoms.cell, pbc=True)

    return new_atoms


def check_termination(atoms):
    """Check what element is at each end of the layer."""
    symbols = atoms.get_chemical_symbols()
    pos = atoms.positions

    # Bottom: lowest z atoms
    z_sorted = sorted(enumerate(pos[:, 2]), key=lambda x: x[1])
    bottom_indices = [i for i, z in z_sorted[:4]]  # First few atoms
    bottom_term = symbols[bottom_indices[0]]

    # Top: highest z atoms
    top_indices = [i for i, z in z_sorted[-4:]]
    top_term = symbols[top_indices[0]]

    return bottom_term, top_term


def main():
    args = parse_args()

    # Read structures
    bot = read(args.bottom)
    top = read(args.top)

    print(f"Bottom: {args.bottom.name} ({len(bot)} atoms)")
    print(f"  a={bot.cell[0,0]:.3f}, b={bot.cell[1,1]:.3f}, c={bot.cell[2,2]:.3f}")
    print(f"Top: {args.top.name} ({len(top)} atoms)")
    print(f"  a={top.cell[0,0]:.3f}, b={top.cell[1,1]:.3f}, c={top.cell[2,2]:.3f}")

    # Check original top layer termination
    bot_term_top, top_term_top = check_termination(top)
    print(f"\nTop layer termination: bottom={bot_term_top}, top={top_term_top}")

    # Apply terminations
    if args.bottom_term != 'auto' and args.bottom_term != bot_term_top:
        print(f"Flipping to get {args.bottom_term} at bottom...")
        top = flip_termination(top, args.bottom_term)
        bot_term_top, top_term_top = check_termination(top)
        print(f"  After flip: bottom={bot_term_top}, top={top_term_top}")

    if args.top_term != 'auto' and args.top_term != top_term_top:
        print(f"Flipping to get {args.top_term} at top...")
        top = flip_termination(top, args.top_term)
        bot_term_top, top_term_top = check_termination(top)
        print(f"  After flip: bottom={bot_term_top}, top={top_term_top}")

    # Get reference ab lattice
    if args.ref == 'first':
        a_ref, b_ref = bot.cell[0, 0], bot.cell[1, 1]
    elif args.ref == 'last':
        a_ref, b_ref = top.cell[0, 0], top.cell[1, 1]
    else:  # average
        a_ref = (bot.cell[0, 0] + top.cell[0, 0]) / 2
        b_ref = (bot.cell[1, 1] + top.cell[1, 1]) / 2

    print(f"\nUsing ab lattice: a={a_ref:.3f}, b={b_ref:.3f}")

    # Scale top to match
    top_scaled = top.copy()
    top_scaled.set_cell([a_ref, b_ref, top.cell[2, 2]], scale_atoms=True)

    # Repeat top in c if requested
    if args.nlayers > 1:
        top_scaled = top_scaled.repeat((1, 1, args.nlayers))

    c_top = top_scaled.cell[2, 2]
    print(f"Top layer thickness: {c_top:.3f} Å ({args.nlayers} unit cells)")

    # Verify final termination after repeat
    bot_t, top_t = check_termination(top_scaled)
    print(f"Final termination: bottom={bot_t}, top={top_t}")

    # Prepare bottom layer - shift to start at z=0
    bot_pos = bot.positions.copy()
    bot_z_min = bot_pos[:, 2].min()
    bot_pos[:, 2] = bot_pos[:, 2] - bot_z_min

    # Prepare top layer - shift to start after gap
    top_pos = top_scaled.positions.copy()
    top_z_min = top_pos[:, 2].min()
    top_pos[:, 2] = top_pos[:, 2] - top_z_min + args.gap

    # Prepare top-most bottom layer - shift to top
    top_bot_pos = bot.positions.copy()
    top_bot_z_min = top_bot_pos[:, 2].min()
    top_bot_pos[:, 2] = top_bot_pos[:, 2] - top_bot_z_min  # Shift to 0
    top_bot_pos[:, 2] = top_bot_pos[:, 2] + args.gap + c_top + args.gap

    # Total c
    c_total = top_bot_pos[:, 2].max() + 2.0

    print(f"Gap between layers: {args.gap} Å")
    print(f"Total cell c: {c_total:.3f} Å")

    # Combine
    all_symbols = list(bot.get_chemical_symbols()) + list(top_scaled.get_chemical_symbols()) + list(bot.get_chemical_symbols())
    all_positions = np.vstack([bot_pos, top_pos, top_bot_pos])

    # Scale to cell
    all_positions[:, 2] = all_positions[:, 2] / all_positions[:, 2].max() * c_total

    # Create atoms
    heterostructure = Atoms(
        symbols=all_symbols,
        positions=all_positions,
        cell=[a_ref, b_ref, c_total],
        pbc=True
    )

    from collections import Counter
    comp = Counter(all_symbols)
    print(f"\nTotal: {len(heterostructure)} atoms")
    print(f"Composition: {dict(comp)}")

    # Save
    write(args.output, heterostructure)
    print(f"\nSaved: {args.output}")


if __name__ == '__main__':
    sys.exit(main())