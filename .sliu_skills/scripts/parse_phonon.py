#!/usr/bin/env python3
"""
Parse Quantum Espresso Phonon Outputs
======================================
Extract phonon frequencies, Born effective charges, and dielectric constants
from QE phonon calculation outputs.

Usage: python parse_phonon.py <dynmat.out> [ph-gamma.out]
"""

import re
import sys
import os


def parse_dynmat(filename):
    """
    Extract phonon frequencies from dynmat.out.

    Returns:
        list: Frequencies in cm^-1
    """
    frequencies = []
    if not os.path.exists(filename):
        print(f"Warning: {filename} not found")
        return frequencies

    with open(filename, 'r') as f:
        for line in f:
            if 'omega(' in line and ') =' in line:
                match = re.search(r'omega\(\s*\d+\)\s*=\s*([-\d.]+)\s*\[cm-1\]', line)
                if match:
                    freq = float(match.group(1))
                    frequencies.append(freq)
    return frequencies


def parse_ph_gamma(filename):
    """
    Extract Born effective charges and dielectric constants from ph-gamma.out.

    Returns:
        dict: Dictionary with 'born_charges', 'eps_electronic', 'eps_static'
    """
    results = {
        'born_charges': [],
        'eps_electronic': None,
        'eps_static': None
    }

    if not os.path.exists(filename):
        print(f"Warning: {filename} not found")
        return results

    with open(filename, 'r') as f:
        content = f.read()

    # Extract Born effective charges
    # Looking for pattern like:
    # atom # 1: Z* =   3.930   0.000   0.000
    #                0.000   3.930   0.000
    #                0.000   0.000   3.930
    born_pattern = r'atom #\s*(\d+):\s*Z\*\s*=\s*([-\d.]+)\s+([-\d.]+)\s+([-\d.]+)'
    matches = re.findall(born_pattern, content)

    for match in matches:
        atom_idx = int(match[0])
        charge_row = [float(match[1]), float(match[2]), float(match[3])]

        # Try to get the next two rows for the 3x3 matrix
        # This is simplified - full implementation would parse all 3 rows per atom

        results['born_charges'].append({
            'atom': atom_idx,
            'row': charge_row
        })

    # Extract electronic dielectric constant
    eps_elec_pattern = r'epsilon \(high frequency\)\s*=\s*([-\d.]+)'
    match = re.search(eps_elec_pattern, content)
    if match:
        results['eps_electronic'] = float(match.group(1))

    # Extract static dielectric constant
    eps_static_pattern = r'epsilon \(static\)\s*=\s*([-\d.]+)'
    match = re.search(eps_static_pattern, content)
    if match:
        results['eps_static'] = float(match.group(1))

    return results


def check_stability(frequencies):
    """
    Check for dynamical instabilities.

    Returns:
        tuple: (is_stable, negative_frequencies)
    """
    negative = [f for f in frequencies if f < -1.0]  # Use small threshold
    return len(negative) == 0, negative


def print_report(frequencies, phonondata=None):
    """Print a summary report."""
    print("\n" + "=" * 50)
    print("PHONON ANALYSIS REPORT")
    print("=" * 50)

    # Frequency analysis
    if frequencies:
        print(f"\nNumber of phonon modes: {len(frequencies)}")
        print(f"Frequency range: {min(frequencies):.2f} to {max(frequencies):.2f} cm^-1")

        # Check stability
        is_stable, negative = check_stability(frequencies)

        if is_stable:
            print("\nStatus: STRUCTURE IS DYNAMICALLY STABLE")
            print("        (no imaginary modes detected)")
        else:
            print(f"\nStatus: WARNING - {len(negative)} IMAGINARY MODE(S) DETECTED")
            print(f"        Imaginary frequencies: {[f'{x:.2f}' for x in negative]} cm^-1")
            print("        This indicates a dynamical instability!")
    else:
        print("\nNo phonon frequencies found")

    # Born charges and dielectric
    if phonondata:
        if phonondata['eps_electronic']:
            print(f"\nElectronic dielectric constant (ε∞): {phonondata['eps_electronic']:.4f}")
        if phonondata['eps_static']:
            print(f"Static dielectric constant (ε0): {phonondata['eps_static']:.4f}")

        if phonondata['born_charges']:
            print(f"\nBorn effective charges (first row):")
            for bc in phonondata['born_charges']:
                print(f"  Atom {bc['atom']}: Z* = {bc['row']}")

    print("\n" + "=" * 50)


def main():
    if len(sys.argv) < 2:
        print("Usage: python parse_phonon.py <dynmat.out> [ph-gamma.out]")
        print("\nExamples:")
        print("  python parse_phonon.py dynmat.out")
        print("  python parse_phonon.py dynmat.out ph-gamma.out")
        sys.exit(1)

    dynmat_file = sys.argv[1]
    ph_gamma_file = sys.argv[2] if len(sys.argv) > 2 else None

    # Parse frequencies
    print(f"Reading: {dynmat_file}")
    frequencies = parse_dynmat(dynmat_file)

    # Parse additional data if available
    phonondata = None
    if ph_gamma_file and os.path.exists(ph_gamma_file):
        print(f"Reading: {ph_gamma_file}")
        phonondata = parse_ph_gamma(ph_gamma_file)

    # Print report
    print_report(frequencies, phonondata)


if __name__ == '__main__':
    main()