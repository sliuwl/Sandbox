#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Merge all non-anion species into a single cation in a VASP POSCAR."
    )
    p.add_argument("--input", required=True, help="Input POSCAR/VASP file.")
    p.add_argument(
        "--output",
        default=None,
        help="Output POSCAR path (default: <stem>_merged.vasp).",
    )
    p.add_argument(
        "--anion",
        default="O",
        help="Anion symbol to keep separate (default: O).",
    )
    p.add_argument(
        "--cation",
        default="Ti",
        help="Cation symbol to use for merged species (default: Ti).",
    )
    return p.parse_args()


def load_poscar(path: Path):
    lines = [line.strip() for line in path.read_text().splitlines() if line.strip()]
    if len(lines) < 8:
        raise ValueError("POSCAR too short.")

    comment = lines[0]
    scale = lines[1]
    lattice = lines[2:5]
    species = lines[5].split()
    counts = [int(x) for x in lines[6].split()]
    idx = 7
    selective = None
    if lines[idx].lower().startswith("s"):
        selective = lines[idx]
        idx += 1
    mode = lines[idx].lower()
    if not mode.startswith("direct"):
        raise ValueError("Only Direct coordinates are supported.")
    idx += 1

    total = sum(counts)
    coords = [lines[idx + i] for i in range(total)]
    return comment, scale, lattice, species, counts, selective, "Direct", coords


def main() -> int:
    args = parse_args()
    in_path = Path(args.input).expanduser().resolve()
    if not in_path.is_file():
        raise FileNotFoundError(f"Input not found: {in_path}")

    comment, scale, lattice, species, counts, selective, mode, coords = load_poscar(
        in_path
    )
    if args.anion not in species:
        raise ValueError(f"Anion '{args.anion}' not found in species list {species}")

    by_species = {}
    cursor = 0
    for sp, count in zip(species, counts):
        by_species[sp] = coords[cursor : cursor + count]
        cursor += count

    cation_coords = []
    anion_coords = []
    for sp in species:
        if sp == args.anion:
            anion_coords.extend(by_species[sp])
        else:
            cation_coords.extend(by_species[sp])

    out_path = (
        Path(args.output).expanduser().resolve()
        if args.output
        else in_path.with_name(f"{in_path.stem}_merged.vasp")
    )

    out_lines = [
        f"{comment} (merged cations)",
        scale,
        *lattice,
        f"{args.cation} {args.anion}",
        f"{len(cation_coords)} {len(anion_coords)}",
    ]
    if selective:
        out_lines.append(selective)
    out_lines.append(mode)
    out_lines.extend(cation_coords)
    out_lines.extend(anion_coords)

    out_path.write_text("\n".join(out_lines) + "\n")
    print(out_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
