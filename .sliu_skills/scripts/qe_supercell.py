#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate VASP supercells and QE structure blocks from a POSCAR."
    )
    parser.add_argument("--input", required=True, help="Path to input POSCAR/VASP file.")
    parser.add_argument(
        "--supercell",
        nargs=3,
        type=int,
        metavar=("A", "B", "C"),
        required=True,
        help="Supercell multipliers (e.g., 2 2 1).",
    )
    parser.add_argument(
        "--out-dir",
        default=None,
        help="Output directory. Defaults to the input file directory.",
    )
    parser.add_argument(
        "--stem",
        default=None,
        help="Output filename stem. Defaults to the input filename stem.",
    )
    parser.add_argument(
        "--vc-relax-template",
        default=None,
        help="Path to a QE vc-relax template containing a __STRUCTURE__ placeholder.",
    )
    parser.add_argument(
        "--vc-relax-out",
        default=None,
        help="Output path for vc-relax.in (default: vc-relax_AXBxC.in in out-dir).",
    )
    return parser.parse_args()


def load_poscar(path: Path):
    lines = [line.strip() for line in path.read_text().splitlines() if line.strip()]
    if len(lines) < 8:
        raise ValueError("POSCAR too short.")

    scale = float(lines[1])
    cell = [[float(x) * scale for x in lines[i].split()[:3]] for i in range(2, 5)]

    species = lines[5].split()
    if all(tok.replace("+", "").replace("-", "").isdigit() for tok in species):
        raise ValueError(
            "POSCAR appears to be missing a species line (VASP 4 format)."
        )
    counts = [int(x) for x in lines[6].split()]
    if sum(counts) <= 0:
        raise ValueError("Invalid atom counts.")

    idx = 7
    if lines[idx].lower().startswith("s"):
        idx += 1
    mode = lines[idx].lower()
    if not mode.startswith("direct"):
        raise ValueError("Only Direct coordinates are supported.")
    idx += 1

    coords = [
        [float(x) for x in lines[idx + i].split()[:3]] for i in range(sum(counts))
    ]
    atoms = []
    cursor = 0
    for sp, count in zip(species, counts):
        for _ in range(count):
            atoms.append((sp, coords[cursor]))
            cursor += 1
    return cell, species, counts, atoms


def build_supercell(cell, species, counts, atoms, mult):
    ax, by, cz = mult
    new_cell = [
        [cell[0][0] * ax, cell[0][1] * ax, cell[0][2] * ax],
        [cell[1][0] * by, cell[1][1] * by, cell[1][2] * by],
        [cell[2][0] * cz, cell[2][1] * cz, cell[2][2] * cz],
    ]

    new_counts = [count * ax * by * cz for count in counts]

    grouped = []
    for sp in species:
        sp_atoms = [c for s, c in atoms if s == sp]
        for tx in range(ax):
            for ty in range(by):
                for tz in range(cz):
                    for x, y, z in sp_atoms:
                        grouped.append(
                            (
                                sp,
                                (
                                    (x + tx) / ax,
                                    (y + ty) / by,
                                    (z + tz) / cz,
                                ),
                            )
                        )
    return new_cell, new_counts, grouped


def write_poscar(path: Path, title: str, cell, species, counts, grouped):
    lines = [title, "  1.0000000000000000"]
    for vec in cell:
        lines.append(f" {vec[0]:.14f} {vec[1]:.14f} {vec[2]:.14f}")
    lines.append(" ".join(species))
    lines.append(" ".join(str(c) for c in counts))
    lines.append("Direct")
    for sp in species:
        for atom_sp, frac in grouped:
            if atom_sp != sp:
                continue
            lines.append(f" {frac[0]:.14f} {frac[1]:.14f} {frac[2]:.14f}")
    path.write_text("\n".join(lines) + "\n")


def write_struc(path: Path, cell, species, grouped):
    lines = ["CELL_PARAMETERS (angstrom)"]
    for vec in cell:
        lines.append(f"    {vec[0]:.8f}     {vec[1]:.8f}     {vec[2]:.8f}")
    lines.append("")
    lines.append("ATOMIC_POSITIONS (crystal)")
    for sp in species:
        for atom_sp, frac in grouped:
            if atom_sp != sp:
                continue
            lines.append(f"{atom_sp:<2}      {frac[0]:.8f}     {frac[1]:.8f}     {frac[2]:.8f}")
    path.write_text("\n".join(lines) + "\n")


def inject_template(template_path: Path, structure_block: str) -> str:
    content = template_path.read_text()
    if "__STRUCTURE__" not in content:
        raise ValueError("Template missing __STRUCTURE__ placeholder.")
    return content.replace("__STRUCTURE__", structure_block)


def main() -> int:
    args = parse_args()
    in_path = Path(args.input).expanduser().resolve()
    if not in_path.is_file():
        print(f"Input not found: {in_path}", file=sys.stderr)
        return 1

    out_dir = Path(args.out_dir).expanduser().resolve() if args.out_dir else in_path.parent
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = args.stem or in_path.stem

    cell, species, counts, atoms = load_poscar(in_path)
    mult = tuple(args.supercell)
    cell_sc, counts_sc, grouped = build_supercell(cell, species, counts, atoms, mult)

    tag = f"{mult[0]}x{mult[1]}x{mult[2]}"
    vasp_path = out_dir / f"{stem}_{tag}.vasp"
    struc_path = out_dir / f"{stem}_{tag}.struc.in"
    vc_relax_path = (
        Path(args.vc_relax_out).expanduser().resolve()
        if args.vc_relax_out
        else out_dir / f"vc-relax_{tag}.in"
    )

    write_poscar(vasp_path, f"{stem} {tag} supercell", cell_sc, species, counts_sc, grouped)
    write_struc(struc_path, cell_sc, species, grouped)

    if args.vc_relax_template:
        structure_block = struc_path.read_text().rstrip() + "\n"
        vc_content = inject_template(Path(args.vc_relax_template), structure_block)
        vc_relax_path.write_text(vc_content)

    print(f"Wrote {vasp_path}")
    print(f"Wrote {struc_path}")
    if args.vc_relax_template:
        print(f"Wrote {vc_relax_path}")
    else:
        print("No vc-relax template provided; skipped vc-relax output.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
