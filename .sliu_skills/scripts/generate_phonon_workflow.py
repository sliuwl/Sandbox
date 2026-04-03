#!/usr/bin/env python3
"""Generate a complete phonon dispersion calculation workflow from a structure file.

Usage:
    generate_phonon_workflow.py <structure_file> [options]

Arguments:
    structure_file: POSCAR-format file or QE input with lattice + positions

Options:
    -o, --output-dir DIR    Output directory (default: <prefix>-phonon-dispersion)
    -p, --prefix PREFIX     Output prefix (default: from structure filename)
    -k, --kpoints K K K     K-point grid (default: 8 8 8)
    -q, --qgrid N N N       Phonon q-grid (default: 2 2 2)
    --ecutwfc CUTOFF        Plane-wave cutoff in Ry (default: 50)
    --ecutrho CUTOFF        Charge density cutoff in Ry (default: 250)
    --tot-charge CHARGE     Total charge (default: 0.0)
    --smearing SMEARING     Smearing type (default: mv)
    --degauss VAL           Smearing width in Ry (default: 0.001)
    --no-symmetry           Disable symmetry (nosym = .true.)
    --path POINTS           High-symmetry path as comma-separated points (default: G,X,S,G,Y,Z)

Examples:
    # Basic usage
    generate_phonon_workflow.py POSCAR

    # Custom k-points and q-grid
    generate_phonon_workflow.py POSCAR -k 6 6 6 -q 3 3 3

    # With doping
    generate_phonon_workflow.py POSCAR --tot-charge 0.4
"""

import argparse
import os
import sys
import re
from pathlib import Path
from dataclasses import dataclass
from typing import Optional


@dataclass
class PhononWorkflowConfig:
    """Configuration for phonon workflow."""
    prefix: str = "tio2"
    output_dir: Path = None
    k_points: tuple = (8, 8, 8)
    q_grid: tuple = (2, 2, 2)
    ecutwfc: float = 50.0
    ecutrho: float = 250.0
    tot_charge: float = 0.0
    smearing: str = "mv"
    degauss: float = 0.001
    nosym: bool = False
    path_points: str = "G,X,S,G,Y,Z"
    path_npoints: int = 20


def parse_poscar(file_path: Path) -> dict:
    """Parse a POSCAR file to extract lattice and atomic positions."""
    with open(file_path) as f:
        lines = f.readlines()

    # Skip comment line
    scale = float(lines[1].strip())

    # Lattice vectors
    lattice = []
    for i in range(2, 5):
        parts = lines[i].split()
        lattice.append([float(x) * scale for x in parts[:3]])

    # Parse elements and counts
    elements_line = lines[5].strip()
    counts_line = lines[6].strip()

    # Handle both formats (with/without element names)
    if elements_line[0].isdigit():
        elements = None
        counts = [int(x) for x in elements_line.split()]
    else:
        elements = elements_line.split()
        counts = [int(x) for x in counts_line.split()]

    # Atomic positions
    nat = sum(counts)
    positions = []
    for i in range(7, 7 + nat):
        parts = lines[i].split()
        positions.append([float(x) for x in parts[:3]])

    return {
        'lattice': lattice,
        'elements': elements,
        'counts': counts,
        'positions': positions,
        'nat': nat
    }


def parse_qe_input(file_path: Path) -> dict:
    """Parse a QE input file to extract relevant parameters."""
    with open(file_path) as f:
        content = f.read()

    # Extract SYSTEM section parameters
    nat = int(re.search(r'nat\s*=\s*(\d+)', content).group(1))
    ntyp = int(re.search(r'ntyp\s*=\s*(\d+)', content).group(1))

    tot_charge = 0.0
    if match := re.search(r'tot_charge\s*=\s*([0-9.e+-]+)', content):
        tot_charge = float(match.group(1))

    nosym = False
    if re.search(r'nosym\s*=\s*\.false\.', content):
        nosym = False
    elif re.search(r'nosym\s*=\s*\.true\.', content):
        nosym = True

    ecutwfc = 50.0
    if match := re.search(r'ecutwfc\s*=\s*([0-9.]+)', content):
        ecutwfc = float(match.group(1))

    ecutrho = 250.0
    if match := re.search(r'ecutrho\s*=\s*([0-9.]+)', content):
        ecutrho = float(match.group(1))

    # Extract lattice - find the block after CELL_PARAMETERS
    lattice = []
    lines = content.split('\n')
    in_cell = False
    for line in lines:
        if 'CELL_PARAMETERS' in line:
            in_cell = True
            continue
        if in_cell:
            if 'ATOMIC_POSITIONS' in line:
                break
            if line.strip() and not line.strip().startswith('!'):
                parts = line.split()
                if len(parts) == 3 and parts[0].replace('.', '').replace('-', '').isdigit():
                    lattice.append([float(x) for x in parts])

    # Extract atomic positions
    positions = []
    elements = []
    for match in re.finditer(r'^(Ti|O|Pb|Si|C|N|H|F|Cl|Ba|Sr|Zr|La|Nb)\s+([0-9.-]+)\s+([0-9.-]+)\s+([0-9.-]+)',
                             content, re.MULTILINE):
        elements.append(match.group(1))
        positions.append([float(match.group(i)) for i in range(2, 5)])

    # Extract atomic species info
    species_info = {}
    for match in re.finditer(r'^(\w+)\s+([\d.]+)\s+(\S+.UPF)', content, re.MULTILINE):
        species_info[match.group(1)] = (match.group(2), match.group(3))

    return {
        'lattice': lattice,
        'elements': elements,
        'counts': [1] * len(elements),  # Placeholder
        'positions': positions,
        'nat': nat,
        'ntyp': ntyp,
        'tot_charge': tot_charge,
        'nosym': nosym,
        'ecutwfc': ecutwfc,
        'ecutrho': ecutrho,
        'species_info': species_info
    }


def get_element_mass(element: str) -> float:
    """Get atomic mass for common elements."""
    masses = {
        'H': 1.008, 'C': 12.011, 'N': 14.007, 'O': 15.999,
        'Si': 28.086, 'S': 32.065, 'Cl': 35.453, 'Ti': 47.867,
        'Fe': 55.845, 'Cu': 63.546, 'Zn': 65.38, 'Sr': 87.62,
        'Zr': 91.224, 'Nb': 92.906, 'Ba': 137.327, 'La': 138.905,
        'Pb': 207.2
    }
    return masses.get(element, 1.0)


def format_lattice(lattice: list) -> str:
    """Format lattice parameters for QE input."""
    lines = []
    for vec in lattice:
        lines.append(f"{vec[0]:14.8f} {vec[1]:14.8f} {vec[2]:14.8f}")
    return '\n'.join(lines)


def format_positions(elements: list, positions: list) -> str:
    """Format atomic positions for QE input."""
    lines = []
    for elem, pos in zip(elements, positions):
        lines.append(f"{elem:<4} {pos[0]:14.8f} {pos[1]:14.8f} {pos[2]:14.8f}")
    return '\n'.join(lines)


def generate_scf_input(config: PhononWorkflowConfig, structure: dict) -> str:
    """Generate SCF input file."""
    elements = structure['elements'] or ['Ti', 'O']
    species_info = structure.get('species_info', {})

    # Build ATOMIC_SPECIES
    species_lines = []
    for elem in set(elements):
        mass = get_element_mass(elem)
        if elem in species_info:
            psp_file = species_info[elem][1]
        else:
            psp_file = f"{elem.lower()}_pbesol_v1.uspp.F.UPF"
        species_lines.append(f"{elem:<4} {mass:8.3f}  {psp_file}")

    # Format path points
    path_points = config.path_points.replace('G', '0.0 0.0 0.0')
    path_formatted = []
    for point in config.path_points.split(','):
        if point == 'G':
            path_formatted.append("0.0 0.0 0.0")
        elif point == 'X':
            path_formatted.append("0.5 0.0 0.0")
        elif point == 'Y':
            path_formatted.append("0.0 0.5 0.0")
        elif point == 'Z':
            path_formatted.append("0.0 0.0 0.5")
        elif point == 'S':
            path_formatted.append("0.5 0.5 0.0")
        elif point == 'R':
            path_formatted.append("0.5 0.5 0.5")
        else:
            path_formatted.append(point)

    path_lines = '\n'.join([f"{p} {config.path_npoints}" for p in path_formatted])

    return f"""! {config.prefix} SCF calculation for phonon dispersion
! Auto-generated by generate_phonon_workflow.py

&CONTROL
  calculation    = 'scf'
  prefix         = '{config.prefix}'
  pseudo_dir     = '../psps'
  outdir         = '../tmp/'
  tstress        = .true.
  tprnfor        = .true.
  etot_conv_thr  = 1.0d-5
  forc_conv_thr  = 1.0d-4
  nstep          = 100
/

&SYSTEM
  nosym          = {f".{str(config.nosym).lower():14}  ! {'Enable' if not config.nosym else 'Disable'} symmetry"}
  ibrav          = 0
  nat            = {structure['nat']}
  ntyp           = {len(set(elements))}
  tot_charge     = {config.tot_charge}
  ecutwfc        = {config.ecutwfc}
  ecutrho        = {config.ecutrho}
  occupations    = 'smearing'
  smearing       = '{config.smearing}'
  degauss        = {config.degauss}
/

&ELECTRONS
  mixing_mode    = 'plain'
  mixing_beta    = 0.5
  conv_thr       = 1.0d-8
/

ATOMIC_SPECIES
{chr(10).join(species_lines)}

K_POINTS {{automatic}}
{config.k_points[0]} {config.k_points[1]} {config.k_points[2]} 0 0 0

CELL_PARAMETERS (angstrom)
{format_lattice(structure['lattice'])}

ATOMIC_POSITIONS (crystal)
{format_positions(elements, structure['positions'])}"""


def generate_ph_grid_input(config: PhononWorkflowConfig) -> str:
    """Generate phonon grid input file."""
    return f"""&INPUTPH
  tr2_ph = 1.0d-14,
  prefix = '{config.prefix}',
  outdir = '../tmp/',
  fildyn = '{config.prefix}.dyn',
  ldisp = .true.,
  nq1 = {config.q_grid[0]}, nq2 = {config.q_grid[1]}, nq3 = {config.q_grid[2]}
 /"""


def generate_q2r_input(config: PhononWorkflowConfig, structure: dict) -> str:
    """Generate q2r input file."""
    elements = list(set(structure['elements'] or ['Ti', 'O']))
    elements.sort()  # Consistent ordering

    # Build amass array (same order as ATOMIC_SPECIES)
    amass_lines = []
    for elem in elements:
        mass = get_element_mass(elem)
        amass_lines.append(f"  amass({elements.index(elem) + 1}) = {mass:8.3f}   ! {elem}")

    return f"""&input
  asr='crystal',
{chr(10).join(amass_lines)}
  flfrc='{config.prefix}.222.fc'
  flfrq='{config.prefix}.disp.freq'
 /"""


def generate_matdyn_input(config: PhononWorkflowConfig, structure: dict) -> str:
    """Generate matdyn input file."""
    elements = list(set(structure['elements'] or ['Ti', 'O']))
    elements.sort()

    amass_lines = []
    for elem in elements:
        mass = get_element_mass(elem)
        amass_lines.append(f"  amass({elements.index(elem) + 1}) = {mass:8.3f}   ! {elem}")

    # Format path
    path_formatted = []
    for point in config.path_points.split(','):
        if point == 'G':
            path_formatted.append(f"0.0 0.0 0.0 {config.path_npoints}")
        elif point == 'X':
            path_formatted.append(f"0.5 0.0 0.0 {config.path_npoints}")
        elif point == 'Y':
            path_formatted.append(f"0.0 0.5 0.0 {config.path_npoints}")
        elif point == 'Z':
            path_formatted.append(f"0.0 0.0 0.5 {config.path_npoints}")
        elif point == 'S':
            path_formatted.append(f"0.5 0.5 0.0 {config.path_npoints}")
        elif point == 'R':
            path_formatted.append(f"0.5 0.5 0.5 {config.path_npoints}")
        else:
            path_formatted.append(f"{point} {config.path_npoints}")

    n_points = len(config.path_points.split(','))

    return f"""&input
  asr='crystal',
{chr(10).join(amass_lines)}
  flfrc='../02Grid/{config.prefix}.222.fc'
  flfrq='{config.prefix}.disp.freq'
  q_in_band_form = .true.
  q_in_cryst_coord = .true.
 /
{n_points}
{chr(10).join(path_formatted)}"""


def generate_run_script(config: PhononWorkflowConfig, use_gpu: bool = True) -> str:
    """Generate the job submission script."""
    gpu_lines = ""
    if use_gpu:
        gpu_lines = """source /opt/sai_config/mps_mapping.d/${SLURM_JOB_PARTITION}.bash 2>/dev/null || true
nvidia-smi dmon -s pucvmte -o T > nvdmon_job-$SLURM_JOB_ID.log &
module load qe/7.3-nvhpc24.3-ompi5.0.8"""

    return f"""#!/bin/bash
#SBATCH --job-name={config.prefix}_phonon_disp
#SBATCH --partition=4V100
#SBATCH --nodes=1
#SBATCH --ntasks=4
#SBATCH --gpus-per-node=4
#SBATCH --qos=rush-gpu

source /etc/profile
source ~/.bashrc 2>/dev/null || true

{gpu_lines}

# Step 1: SCF calculation
echo "=== Step 1: SCF calculation ==="
cd 00SCF
mpirun -np $SLURM_NTASKS --map-by $MAP_OPT -mca coll_hcoll_enable 0 pw.x -i scf.in -nk 4 > scf.out
cd ..

# Step 2: Phonon on q-grid
echo "=== Step 2: Phonon calculation on q-grid ==="
cd 02Grid
mpirun -np $SLURM_NTASKS --map-by $MAP_OPT -mca coll_hcoll_enable 0 ph.x -i ph-grid.in > ph-grid.out
cd ..

# Step 3: q2r (Fourier interpolation)
echo "=== Step 3: q2r.x Fourier interpolation ==="
cd 03q2r
q2r.x < q2r.in > q2r.out
cd ..

# Step 4: matdyn (dispersion)
echo "=== Step 4: matdyn.x dispersion ==="
cd 04matdyn
matdyn.x < matdyn.in > matdyn.out
cd ..

echo "=== Phonon calculation complete ==="

exit"""


def generate_plot_script(config: PhononWorkflowConfig) -> str:
    """Generate phonon plotting script."""
    labels = config.path_points.replace(',', "','")

    return f"""#!/usr/bin/env python3
\"\"\"Plot phonon dispersion from matdyn output.\"\"\"

import numpy as np
import matplotlib.pyplot as plt

# Load data
data = np.loadtxt('../04matdyn/{config.prefix}.disp.freq.gp')
kpt = np.loadtxt('../04matdyn/qpoints', skiprows=1)

# High-symmetry labels (must match matdyn.in path)
kpt_labels = ['{labels}']

# Extract distance and frequencies
distance = data[:, 0]
frequencies = data[:, 1:]  # All phonon modes

# Plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot each mode
for i in range(frequencies.shape[1]):
    ax.plot(distance, frequencies[:, i], 'b-', linewidth=1)

# Mark high-symmetry points
unique_points = np.unique(kpt[:, 0])
for point in unique_points:
    ax.axvline(x=point, color='gray', linestyle='--', alpha=0.5)

# Set labels
ax.set_xticks(kpt[:, 0])
ax.set_xticklabels(kpt_labels)
ax.set_xlabel('Wavevector')
ax.set_ylabel(r'Frequency (cm$^{-1}$)')
ax.set_title('{config.prefix} Phonon Dispersion')

# Zero line
ax.axhline(y=0, color='black', linestyle='-', linewidth=0.5)

plt.tight_layout()
plt.savefig('phonon_bands.png', dpi=300)
print("Saved phonon_bands.png")"""


def main():
    parser = argparse.ArgumentParser(
        description='Generate complete phonon dispersion workflow',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument('structure_file', type=Path, help='POSCAR or QE input file')
    parser.add_argument('-o', '--output-dir', type=Path, help='Output directory')
    parser.add_argument('-p', '--prefix', help='Project prefix')
    parser.add_argument('-k', '--kpoints', nargs=3, type=int, default=[8, 8, 8],
                        help='K-point grid (default: 8 8 8)')
    parser.add_argument('-q', '--qgrid', nargs=3, type=int, default=[2, 2, 2],
                        help='Phonon q-grid (default: 2 2 2)')
    parser.add_argument('--ecutwfc', type=float, default=50.0,
                        help='Plane-wave cutoff in Ry (default: 50)')
    parser.add_argument('--ecutrho', type=float, default=250.0,
                        help='Charge density cutoff in Ry (default: 250)')
    parser.add_argument('--tot-charge', type=float, default=0.0,
                        help='Total charge (default: 0.0)')
    parser.add_argument('--smearing', default='mv',
                        help='Smearing type (default: mv)')
    parser.add_argument('--degauss', type=float, default=0.001,
                        help='Smearing width in Ry (default: 0.001)')
    parser.add_argument('--no-symmetry', action='store_true',
                        help='Disable symmetry')
    parser.add_argument('--path', default='G,X,S,G,Y,Z',
                        help='High-symmetry path (default: G,X,S,G,Y,Z)')

    args = parser.parse_args()

    # Determine prefix from filename
    if args.prefix:
        prefix = args.prefix
    else:
        prefix = args.structure_file.stem.split('_')[0]

    # Determine output directory
    if args.output_dir:
        output_dir = args.output_dir
    else:
        output_dir = Path(f"{prefix}-phonon-dispersion")

    # Create config
    config = PhononWorkflowConfig(
        prefix=prefix,
        output_dir=output_dir,
        k_points=tuple(args.kpoints),
        q_grid=tuple(args.qgrid),
        ecutwfc=args.ecutwfc,
        ecutrho=args.ecutrho,
        tot_charge=args.tot_charge,
        smearing=args.smearing,
        degauss=args.degauss,
        nosym=args.no_symmetry,
        path_points=args.path
    )

    # Parse input structure
    suffix = args.structure_file.suffix.lower()
    if suffix in ['.vasp', '.poscar', '']:
        print(f"Parsing POSCAR file: {args.structure_file}")
        structure = parse_poscar(args.structure_file)
    else:
        print(f"Parsing QE input file: {args.structure_file}")
        structure = parse_qe_input(args.structure_file)

    print(f"Structure: {structure['nat']} atoms, {len(set(structure['elements'] or ['Ti','O']))} species")

    # Create directory structure
    dirs = ['00SCF', '02Grid', '03q2r', '04matdyn', '05Plot', 'psps', 'tmp']
    for d in dirs:
        (output_dir / d).mkdir(parents=True, exist_ok=True)

    # Generate input files
    print(f"Generating input files in {output_dir}/")

    scf_in = generate_scf_input(config, structure)
    (output_dir / '00SCF' / 'scf.in').write_text(scf_in)

    ph_grid_in = generate_ph_grid_input(config)
    (output_dir / '02Grid' / 'ph-grid.in').write_text(ph_grid_in)

    q2r_in = generate_q2r_input(config, structure)
    (output_dir / '03q2r' / 'q2r.in').write_text(q2r_in)

    matdyn_in = generate_matdyn_input(config, structure)
    (output_dir / '04matdyn' / 'matdyn.in').write_text(matdyn_in)

    run_sh = generate_run_script(config)
    (output_dir / 'run_phonon.sh').write_text(run_sh)
    (output_dir / 'run_phonon.sh').chmod(0o755)

    plot_py = generate_plot_script(config)
    (output_dir / '05Plot' / 'plot_phonon.py').write_text(plot_py)

    print(f"Workflow generated successfully!")
    print(f"\nTo run:")
    print(f"  cd {output_dir}")
    print(f"  sbatch run_phonon.sh")


if __name__ == '__main__':
    sys.exit(main())