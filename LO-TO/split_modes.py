#!/usr/bin/env python3
"""
Split a dynmat.axsf file into separate XSF files, one for each phonon mode.

Usage:
    python split_modes.py input.axsf [output_prefix]
    python split_modes.py 000/dynmat.axsf
"""

import sys
import re
from pathlib import Path


def parse_axsf(filepath):
    """Parse an XSF file and extract crystal info and phonon modes."""
    with open(filepath, 'r') as f:
        content = f.read()

    lines = content.strip().split('\n')

    # Parse header
    primvec = []
    position_start = None

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        if line == 'PRIMVEC':
            # Read lattice vectors (next 3 lines)
            for j in range(3):
                i += 1
                primvec.append([float(x) for x in lines[i].split()])
            i += 1
            continue
        elif line.startswith('PRIMCOORD'):
            position_start = i
            break

        i += 1

    if position_start is None:
        raise ValueError("Could not parse AXSF file structure")

    # Extract each mode (PRIMCOORD block)
    modes = []
    current_mode = []

    for line in lines[position_start:]:
        if line.startswith('PRIMCOORD'):
            if current_mode:
                modes.append(current_mode)
            current_mode = [line]
        else:
            current_mode.append(line)

    # Add the last mode
    if current_mode:
        modes.append(current_mode)

    return primvec, modes


def write_mode_xsf(output_path, primvec, mode_lines):
    """Write a single mode to an XSF file (single structure format, not animation)."""
    with open(output_path, 'w') as f:
        f.write("CRYSTAL\n")
        f.write("PRIMVEC\n")
        for vec in primvec:
            f.write(f"   {vec[0]:12.6f}  {vec[1]:12.6f}  {vec[2]:12.6f}\n")
        # For single structure, use PRIMCOORD 1 (not ANIMSTEPS wrapper)
        for line in mode_lines:
            f.write(line + '\n')


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    input_file = sys.argv[1]
    output_prefix = sys.argv[2] if len(sys.argv) > 2 else None

    # Parse input
    print(f"Reading {input_file}...")
    primvec, modes = parse_axsf(input_file)
    print(f"Found {len(modes)} modes")

    # Determine output path
    input_path = Path(input_file)
    if output_prefix is None:
        # Use input filename without extension as prefix
        output_dir = input_path.parent
        output_prefix = input_path.stem  # filename without any extension
    else:
        output_dir = Path('.')
        output_prefix = Path(output_prefix)

    output_dir.mkdir(parents=True, exist_ok=True)

    # Write each mode as separate XSF
    for idx, mode_lines in enumerate(modes, start=1):
        # Mode 1 = acoustic (typically zero frequency), skip if desired
        output_file = output_dir / f"{output_prefix}_mode{idx:02d}.xsf"
        write_mode_xsf(output_file, primvec, mode_lines)
        print(f"  Written: {output_file}")

    print(f"\nDone! Extracted {len(modes)} mode files to {output_dir}")


if __name__ == "__main__":
    main()