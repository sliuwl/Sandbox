#!/usr/bin/env python3
"""Read a Quantum ESPRESSO output file with ASE and write the final structure as VASP."""

from __future__ import annotations

import argparse
from pathlib import Path


def extract_final_structure_manual(qe_output: Path):
    """Extract the final structure when ASE fails (no 'Begin final coordinates' marker)."""
    content = qe_output.read_text()
    lines = content.split('\n')

    # Find the last occurrence of CELL_PARAMETERS
    cell_params_idx = None
    for i in range(len(lines) - 1, -1, -1):
        if 'CELL_PARAMETERS' in lines[i]:
            cell_params_idx = i
            break

    if cell_params_idx is None:
        raise ValueError("No CELL_PARAMETERS found in QE output")

    # Extract cell parameters (next 3 lines, skipping empty line if present)
    cell_params = []
    for i in range(cell_params_idx + 1, cell_params_idx + 5):
        if i < len(lines) and lines[i].strip():
            try:
                cell_params.append([float(x) for x in lines[i].split()])
            except ValueError:
                continue

    if len(cell_params) < 3:
        raise ValueError(f"Could not extract 3 cell parameter rows, got {len(cell_params)}")

    # Find ATOMIC_POSITIONS after CELL_PARAMETERS
    atomic_pos_idx = None
    for i in range(cell_params_idx, min(cell_params_idx + 10, len(lines))):
        if 'ATOMIC_POSITIONS' in lines[i]:
            atomic_pos_idx = i
            break

    if atomic_pos_idx is None:
        raise ValueError("No ATOMIC_POSITIONS found after CELL_PARAMETERS")

    # Find the end of ATOMIC_POSITIONS
    start_idx = atomic_pos_idx + 1
    end_idx = start_idx
    for i in range(start_idx, len(lines)):
        line = lines[i].strip()
        if not line:
            end_idx = i
            break
        if 'Writing config' in line or 'NEW-OLD' in line:
            end_idx = i
            break

    # Extract atomic positions
    atoms = []
    for i in range(start_idx, end_idx):
        parts = lines[i].split()
        if len(parts) >= 4:
            try:
                atoms.append((parts[0], float(parts[1]), float(parts[2]), float(parts[3])))
            except ValueError:
                continue

    if not atoms:
        raise ValueError("No atomic positions found")

    # Create ASE Atoms object
    from ase import Atoms
    from ase.cell import Cell

    cell = Cell(cell_params)
    symbols = [a[0] for a in atoms]
    scaled_positions = [[a[1], a[2], a[3]] for a in atoms]

    # Create atoms with explicit element list - this ensures correct element count
    atoms_obj = Atoms(symbols, scaled_positions=scaled_positions, cell=cell, pbc=True)

    return atoms_obj, cell_params


def write_vasp_manually(output: Path, atoms, cell_params):
    """Write VASP file manually to ensure correct format."""
    from collections import Counter

    symbols = atoms.get_chemical_symbols()
    counts = Counter(symbols)
    unique_elements = list(counts.keys())

    # Build element string and count string
    element_str = "  ".join(unique_elements)
    count_str = "  ".join(str(counts[e]) for e in unique_elements)

    scaled = atoms.get_scaled_positions()

    lines = []
    lines.append(element_str + "\n")
    lines.append("  1.0000000000000000\n")
    for row in cell_params:
        lines.append(f" {row[0]:.14f} {row[1]:.14f} {row[2]:.14f}\n")

    # Check if second line matches elements
    second_line = "  ".join(f"{e:>2}" for e in unique_elements)
    lines.append(second_line + "\n")
    lines.append(count_str + "\n")

    lines.append("Direct\n")
    for pos in scaled:
        lines.append(f" {pos[0]:.14f} {pos[1]:.14f} {pos[2]:.14f}\n")

    output.write_text("".join(lines))
    return output


def write_cif(output: Path, atoms, cell_params):
    """Write CIF file."""
    from collections import Counter

    symbols = atoms.get_chemical_symbols()
    counts = Counter(symbols)

    # Get unique elements in order of first appearance
    seen = set()
    unique_elements = []
    for s in symbols:
        if s not in seen:
            seen.add(s)
            unique_elements.append(s)

    scaled = atoms.get_scaled_positions()

    lines = []
    lines.append("data_extracted_structure\n")
    lines.append("_audit_creation_date              2026-04-06\n")
    lines.append("_audit_creation_method            'Extracted from QE output'\n")
    lines.append("\n")
    lines.append(f"_cell_length_a                    {cell_params[0][0]:.6f}\n")
    lines.append(f"_cell_length_b                    {cell_params[1][1]:.6f}\n")
    lines.append(f"_cell_length_c                    {cell_params[2][2]:.6f}\n")
    lines.append("_cell_angle_alpha                 90.0\n")
    lines.append("_cell_angle_beta                  90.0\n")
    lines.append("_cell_angle_gamma                 90.0\n")
    lines.append("\n")
    lines.append("_symmetry_space_group_name_H-M    'P 1'\n")
    lines.append("_symmetry_Int_Tables_number       1\n")
    lines.append("\n")
    lines.append("loop_\n")
    lines.append("_atom_site_label\n")
    lines.append("_atom_site_type_symbol\n")
    lines.append("_atom_site_fract_x\n")
    lines.append("_atom_site_fract_y\n")
    lines.append("_atom_site_fract_z\n")

    # Create labeled atoms
    label_counts = Counter()
    for i, (symbol, pos) in enumerate(zip(symbols, scaled)):
        label_counts[symbol] += 1
        label = f"{symbol}{label_counts[symbol]}"
        lines.append(f"{label:5s}  {symbol:2s}  {pos[0]:12.10f} {pos[1]:12.10f} {pos[2]:12.10f}\n")

    output.write_text("".join(lines))
    return output


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Read the last structure from a Quantum ESPRESSO output and export it "
            "as a VASP POSCAR-style file or CIF file."
        )
    )
    parser.add_argument("qe_output", help="Path to the Quantum ESPRESSO output file, e.g. qe.out")
    parser.add_argument(
        "-o",
        "--output",
        help="Output filename. If omitted, uses input basename with format suffix.",
    )
    parser.add_argument(
        "-f",
        "--format",
        choices=["vasp", "cif"],
        default="vasp",
        help="Output format: 'vasp' for VASP POSCAR (default), 'cif' for CIF.",
    )
    return parser.parse_args()




def ensure_suffix(path: Path, fmt: str) -> Path:
    """Ensure correct suffix based on format."""
    if fmt == "vasp":
        return path if path.suffix == ".vasp" else path.with_suffix(".vasp")
    elif fmt == "cif":
        return path if path.suffix == ".cif" else path.with_suffix(".cif")
    return path


def main() -> None:
    args = parse_args()

    qe_output = Path(args.qe_output).expanduser().resolve()
    if not qe_output.is_file():
        raise FileNotFoundError(f"QE output file not found: {qe_output}")

    # Determine output path
    if args.output:
        output = Path(args.output).expanduser()
    else:
        output = qe_output.with_suffix(f".{args.format}")
    output = ensure_suffix(output, args.format)

    from ase.io import read

    # Try standard ASE reading first
    try:
        atoms = read(qe_output, format="espresso-out", index=-1)
        atoms.wrap()
        cell_params = atoms.get_cell().array
    except AssertionError as e:
        # ASE failed, likely due to missing 'Begin final coordinates' marker
        # Fall back to manual extraction
        print(f"ASE parsing failed: {e}")
        print("Falling back to manual structure extraction...")
        atoms, cell_params = extract_final_structure_manual(qe_output)

    # Write in the requested format
    if args.format == "cif":
        write_cif(output, atoms, cell_params)
    else:
        write_vasp_manually(output, atoms, cell_params)

    print(f"Wrote {output}")


if __name__ == "__main__":
    main()