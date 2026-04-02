#!/usr/bin/env python3
"""
Quantum Espresso Phonon Band Structure Plotter
===============================================
Generates publication-quality phonon dispersion plots.

Usage: python plot_phonon.py [--freq-min FMIN] [--freq-max FMAX]
                            [--output OUTPUT] [--format FORMAT]
                            [--labels LABEL1,LABEL2,...]
                            data_file
"""

import numpy as np
import matplotlib.pyplot as plt
import argparse
import os


def load_phonon_data(freq_file):
    """Load phonon frequency data from matdyn output."""
    data = np.loadtxt(freq_file)
    return data


def load_qpoints(qpoints_file):
    """Load q-point information."""
    if os.path.exists(qpoints_file):
        return np.loadtxt(qpoints_file)
    return None


def get_high_symmetry_positions(data, kpt):
    """Calculate x-positions of high-symmetry points."""
    if kpt is None:
        return None

    nkpt = kpt.shape[0]
    xkpt = [0.0]
    count = 0

    for j in range(nkpt - 1):
        count += int(kpt[j, 3])
        xkpt.append(data[count, 0])

    return xkpt


def parse_labels(label_string):
    """Parse labels from comma-separated string."""
    return [l.strip() for l in label_string.split(',')]


def plot_phonon_bands(freq_file, qpoints_file=None,
                      labels=None, freq_min=0, freq_max=None,
                      output='bands', fmt='png', style='publication'):
    """
    Plot phonon band structure.

    Parameters:
    -----------
    freq_file : str
        Path to pto.disp.freq.gp file
    qpoints_file : str, optional
        Path to qpoints file
    labels : list, optional
        High-symmetry point labels
    freq_min, freq_max : float
        Frequency range in cm^-1
    output : str
        Output filename base
    fmt : str
        Output format (png, pdf, eps, svg)
    style : str
        Plot style ('publication', 'presentation', 'thesis')
    """

    # Load data
    data = load_phonon_data(freq_file)
    kpt = load_qpoints(qpoints_file) if qpoints_file else None

    # Configure style
    if style == 'publication':
        plt.rcParams.update({
            'font.size': 10,
            'axes.labelsize': 12,
            'xtick.labelsize': 10,
            'ytick.labelsize': 10,
            'legend.fontsize': 8,
            'lines.linewidth': 1.0,
            'figure.dpi': 300
        })
        figsize = (6, 4)
    elif style == 'presentation':
        plt.rcParams.update({
            'font.size': 14,
            'axes.labelsize': 16,
            'lines.linewidth': 2.0
        })
        figsize = (10, 6)
    elif style == 'thesis':
        plt.rcParams.update({
            'font.size': 11,
            'axes.labelsize': 14,
            'lines.linewidth': 1.5
        })
        figsize = (7, 5)

    # Create figure
    fig, ax = plt.subplots(figsize=figsize)

    # Number of modes = columns - 1 (first column is distance)
    nks, ncols = data.shape
    nmodes = ncols - 1

    # Determine frequency range
    if freq_max is None:
        freq_max = np.max(data[:, 1:]) * 1.1

    # Plot each mode
    for i in range(1, ncols):
        ax.plot(data[:, 0], data[:, i], '-k', lw=plt.rcParams['lines.linewidth'])

    # Mark high-symmetry points
    if kpt is not None:
        xkpt = get_high_symmetry_positions(data, kpt)
        for xi in xkpt:
            ax.axvline(xi, color='#1f77b4', linewidth=0.8, linestyle='--', alpha=0.7)

        # Set x-axis labels
        if labels is not None and len(labels) > 0:
            ax.set_xticks(xkpt)
            ax.set_xticklabels(labels)

    # Set axis limits
    ax.set_xlim([0, data[-1, 0]])
    ax.set_ylim([freq_min, freq_max])

    # Labels
    ax.set_xlabel('Wavevector', fontsize=plt.rcParams['axes.labelsize'])
    ax.set_ylabel('Frequency (cm$^{-1}$)', fontsize=plt.rcParams['axes.labelsize'])

    # Add zero line
    if freq_min < 0:
        ax.axhline(0, color='red', linewidth=0.8, linestyle='-', alpha=0.5)

    # Tight layout and save
    plt.tight_layout()

    # Save in requested formats
    formats = fmt.split(',') if ',' in fmt else [fmt]
    for f in formats:
        output_file = f'{output}.{f}'
        plt.savefig(output_file, dpi=300 if f == 'png' else None)
        print(f'Saved: {output_file}')

    plt.close()


def main():
    parser = argparse.ArgumentParser(
        description='Plot QE phonon band structures',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  python plot_phonon.py pto.disp.freq.gp --labels Γ,X,M,Γ,Z
  python plot_phonon.py pto.disp.freq.gp -o my_bands -f pdf,png
  python plot_phonon.py pto.disp.freq.gp --freq-max 1000 --style presentation
        '''
    )

    parser.add_argument('input', help='Input file (pto.disp.freq.gp)')
    parser.add_argument('--qpoints', '-q', default='qpoints',
                        help='Q-points file (default: qpoints)')
    parser.add_argument('--labels', '-l', default='Γ,X,M,Γ,Z',
                        help='K-point labels (comma-separated)')
    parser.add_argument('--freq-min', type=float, default=0,
                        help='Minimum frequency (cm⁻¹)')
    parser.add_argument('--freq-max', type=float, default=None,
                        help='Maximum frequency (cm⁻¹)')
    parser.add_argument('--output', '-o', default='bands',
                        help='Output filename base (default: bands)')
    parser.add_argument('--format', '-f', default='png',
                        help='Output format: png, pdf, eps, svg (default: png)')
    parser.add_argument('--style', '-s', default='publication',
                        choices=['publication', 'presentation', 'thesis'],
                        help='Plot style (default: publication)')

    args = parser.parse_args()

    # Parse labels
    labels = parse_labels(args.labels)

    # Check input file exists
    if not os.path.exists(args.input):
        print(f'Error: Input file not found: {args.input}')
        return 1

    # Check qpoints file exists
    qpoints_file = args.qpoints if os.path.exists(args.qpoints) else None

    # Generate plot
    plot_phonon_bands(
        args.input,
        qpoints_file=qpoints_file,
        labels=labels,
        freq_min=args.freq_min,
        freq_max=args.freq_max,
        output=args.output,
        fmt=args.format,
        style=args.style
    )

    return 0


if __name__ == '__main__':
    exit(main())