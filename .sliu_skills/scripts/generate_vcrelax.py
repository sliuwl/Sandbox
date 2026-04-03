#!/usr/bin/env python3
"""
Generate QE vc-relax input files with customizable parameters.

Usage: python generate_vcrelax.py [--prefix PREFIX] [--kpoints K1,K2,K3]
                                   [--ecutwfc E_CUT] [--ecutrho RHO_CUT]
                                   [--cell-dofree {all,volume,x,y,z}]
                                   [--conv-thr CONV] [--force-thr FORCE]
                                   <output_file>
"""

import argparse
import os


# Default pseudopotentials (GBRV PBEsol)
DEFAULT_PSEUDOS = {
    'H':  ('1.008',   'H.pbesol-nl-rrkjus_psl.1.0.0.UPF'),
    'He': ('4.0026',  'He.pbesol-spn-rrkjus_psl.1.0.0.UPF'),
    'Li': ('6.94',    'Li.pbesol-sssp效率efficiency.UPF'),
    'Be': ('9.0122',  'Be.pbesol-sssp效率efficiency.UPF'),
    'B':  ('10.81',   'B.pbesol-nl-rrkjus_psl.1.0.0.UPF'),
    'C':  ('12.011',  'C.pbesol-nl-rrkjus_psl.1.0.0.UPF'),
    'N':  ('14.007',  'N.pbesol-nl-rrkjus_psl.1.0.0.UPF'),
    'O':  ('15.999',  'o_pbesol_v1.2.uspp.F.UPF'),
    'F':  ('18.998',  'F.pbesol-nl-rrkjus_psl.1.0.0.UPF'),
    'Ne': ('20.180',  'Ne.pbesol-spn-rrkjus_psl.1.0.0.UPF'),
    'Na': ('22.990',  'Na.pbesol-sssp效率efficiency.UPF'),
    'Mg': ('24.305',  'Mg.pbesol-sssp效率efficiency.UPF'),
    'Al': ('26.982',  'Al.pbesol-sssp效率efficiency.UPF'),
    'Si': ('28.086',  'Si.pbesol-nl-rrkjus_psl.1.0.0.UPF'),
    'P':  ('30.974',  'P.pbesol-nl-rrkjus_psl.1.0.0.UPF'),
    'S':  ('32.06',   'S.pbesol-nl-rrkjus_psl.1.0.0.UPF'),
    'Cl': ('35.45',   'Cl.pbesol-nl-rrkjus_psl.1.0.0.UPF'),
    'K':  ('39.098',  'K.pbesol-sssp效率efficiency.UPF'),
    'Ca': ('40.078',  'Ca.pbesol-sssp效率efficiency.UPF'),
    'Sc': ('44.956',  'Sc.pbesol-sssp效率efficiency.UPF'),
    'Ti': ('47.867',  'ti_pbesol_v1.4.uspp.F.UPF'),
    'V':  ('50.942',  'V.pbesol-sssp效率efficiency.UPF'),
    'Cr': ('51.996',  'Cr.pbesol-sssp效率efficiency.UPF'),
    'Mn': ('54.938',  'Mn.pbesol-sssp效率efficiency.UPF'),
    'Fe': ('55.845',  'Fe.pbesol-sssp效率efficiency.UPF'),
    'Co': ('58.933',  'Co.pbesol-sssp效率efficiency.UPF'),
    'Ni': ('58.693',  'Ni.pbesol-sssp效率efficiency.UPF'),
    'Cu': ('63.546',  'Cu.pbesol-sssp效率efficiency.UPF'),
    'Zn': ('65.38',   'Zn.pbesol-sssp效率efficiency.UPF'),
    'Ga': ('69.723',  'Ga.pbesol-sssp效率efficiency.UPF'),
    'Ge': ('72.630',  'Ge.pbesol-nl-rrkjus_psl.1.0.0.UPF'),
    'As': ('74.922',  'As.pbesol-nl-rrkjus_psl.1.0.0.UPF'),
    'Se': ('78.971',  'Se.pbesol-nl-rrkjus_psl.1.0.0.UPF'),
    'Br': ('79.904',  'Br.pbesol-nl-rrkjus_psl.1.0.0.UPF'),
    'Kr': ('83.798',  'Kr.pbesol-spn-rrkjus_psl.1.0.0.UPF'),
    'Rb': ('85.468',  'Rb.pbesol-sssp效率efficiency.UPF'),
    'Sr': ('87.62',   'sr_pbesol_v1.uspp.F.UPF'),
    'Y':  ('88.906',  'Y.pbesol-sssp效率efficiency.UPF'),
    'Zr': ('91.224',  'Zr.pbesol-sssp效率efficiency.UPF'),
    'Nb': ('92.906',  'nb_pbesol_v1.uspp.F.UPF'),
    'Mo': ('95.95',   'Mo.pbesol-sssp效率efficiency.UPF'),
    'Tc': ('98',      'Tc.pbesol-sssp效率efficiency.UPF'),
    'Ru': ('101.07',  'Ru.pbesol-sssp效率efficiency.UPF'),
    'Rh': ('102.91',  'Rh.pbesol-sssp效率efficiency.UPF'),
    'Pd': ('106.42',  'Pd.pbesol-sssp效率efficiency.UPF'),
    'Ag': ('107.87',  'Ag.pbesol-sssp效率efficiency.UPF'),
    'Cd': ('112.41',  'Cd.pbesol-sssp效率efficiency.UPF'),
    'In': ('114.82',  'In.pbesol-sssp效率efficiency.UPF'),
    'Sn': ('118.71',  'Sn.pbesol-nl-rrkjus_psl.1.0.0.UPF'),
    'Sb': ('121.76',  'Sb.pbesol-nl-rrkjus_psl.1.0.0.UPF'),
    'Te': ('127.60',  'Te.pbesol-nl-rrkjus_psl.1.0.0.UPF'),
    'I':  ('126.90',  'I.pbesol-nl-rrkjus_psl.1.0.0.UPF'),
    'Xe': ('131.29',  'Xe.pbesol-spn-rrkjus_psl.1.0.0.UPF'),
    'Cs': ('132.91',  'Cs.pbesol-sssp效率efficiency.UPF'),
    'Ba': ('137.33',  'ba_pbesol_v1.uspp.F.UPF'),
    'La': ('138.91',  'La.pbesol-sssp效率efficiency.UPF'),
    'Ce': ('140.12',  'Ce.pbesol-sssp效率efficiency.UPF'),
    'Pr': ('140.91',  'Pr.pbesol-sssp效率efficiency.UPF'),
    'Nd': ('144.24',  'Nd.pbesol-sssp效率efficiency.UPF'),
    'Pm': ('145',     'Pm.pbesol-sssp效率efficiency.UPF'),
    'Sm': ('150.36',  'Sm.pbesol-sssp效率efficiency.UPF'),
    'Eu': ('151.96',  'Eu.pbesol-sssp效率efficiency.UPF'),
    'Gd': ('157.25',  'Gd.pbesol-sssp效率efficiency.UPF'),
    'Tb': ('158.93',  'Tb.pbesol-sssp效率efficiency.UPF'),
    'Dy': ('162.50',  'Dy.pbesol-sssp效率efficiency.UPF'),
    'Ho': ('164.93',  'Ho.pbesol-sssp效率efficiency.UPF'),
    'Er': ('167.26',  'Er.pbesol-sssp效率efficiency.UPF'),
    'Tm': ('168.93',  'Tm.pbesol-sssp效率efficiency.UPF'),
    'Yb': ('173.05',  'Yb.pbesol-sssp效率efficiency.UPF'),
    'Lu': ('174.97',  'Lu.pbesol-sssp效率efficiency.UPF'),
    'Hf': ('178.49',  'Hf.pbesol-sssp效率efficiency.UPF'),
    'Ta': ('180.95',  'Ta.pbesol-sssp效率efficiency.UPF'),
    'W':  ('183.84',  'W.pbesol-sssp效率efficiency.UPF'),
    'Re': ('186.21',  'Re.pbesol-sssp效率efficiency.UPF'),
    'Os': ('190.23',  'Os.pbesol-sssp效率efficiency.UPF'),
    'Ir': ('192.22',  'Ir.pbesol-sssp效率efficiency.UPF'),
    'Pt': ('195.08',  'Pt.pbesol-sssp效率efficiency.UPF'),
    'Au': ('196.97',  'Au.pbesol-sssp效率efficiency.UPF'),
    'Hg': ('200.59',  'Hg.pbesol-sssp效率efficiency.UPF'),
    'Tl': ('204.38',  'Tl.pbesol-sssp效率efficiency.UPF'),
    'Pb': ('207.2',   'pb_pbesol_v1.uspp.F.UPF'),
    'Bi': ('208.98',  'Bi.pbesol-nl-rrkjus_psl.1.0.0.UPF'),
    'Po': ('209',     'Po.pbesol-nl-rrkjus_psl.1.0.0.UPF'),
    'At': ('210',     'At.pbesol-nl-rrkjus_psl.1.0.0.UPF'),
    'Rn': ('222',     'Rn.pbesol-spn-rrkjus_psl.1.0.0.UPF'),
}


def parse_atoms_file(atoms_file):
    """Parse simple atom list file or generate from structure."""
    atoms = []
    with open(atoms_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                parts = line.split()
                if len(parts) >= 4:
                    element = parts[0]
                    x, y, z = float(parts[1]), float(parts[2]), float(parts[3])
                    atoms.append((element, x, y, z))
    return atoms


def parse_lattice_file(lattice_file):
    """Parse lattice vectors from file."""
    vectors = []
    with open(lattice_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                parts = line.split()
                if len(parts) >= 3:
                    v = [float(parts[0]), float(parts[1]), float(parts[2])]
                    vectors.append(v)
    return vectors


def generate_vcrelax_input(atoms, lattice_vectors, args):
    """Generate vc-relax input file content."""

    # Get unique elements
    elements = list(dict.fromkeys([a[0] for a in atoms]))

    # Build ATOMIC_SPECIES
    atomic_species = []
    for elem in elements:
        if elem in DEFAULT_PSEUDOS:
            mass, pseudo = DEFAULT_PSEUDOS[elem]
        else:
            # Try to use element name as pseudo file
            mass = '0'  # Will use default
            pseudo = f'{elem}.UPF'
            print(f"Warning: No default pseudo for {elem}, using {pseudo}")
        atomic_species.append(f"{elem}  {mass}  {pseudo}")

    # Estimate ecutwfc if not provided
    ecutwfc = args.ecutwfc or 50.0
    ecutrho = args.ecutrho or ecutwfc * 5

    # Build cell parameters string
    cell_params = "\n".join([f"{v[0]:10.6f}  {v[1]:10.6f}  {v[2]:10.6f}"
                             for v in lattice_vectors])

    # Build atomic positions string
    atomic_positions = "\n".join([f"{a[0]:4s}  {a[1]:12.8f}  {a[2]:12.8f}  {a[3]:12.8f}"
                                   for a in atoms])

    # k-points
    kpoints = args.kpoints or "8 8 8"
    k1, k2, k3 = kpoints.replace(',', ' ').split()[:3]
    k_shift = args.no_shift and "0 0 0" or "0 0 0"

    # Cell degrees of freedom
    cell_dofree = args.cell_dofree or "all"
    conv_thr = args.conv_thr or "1.0d-8"
    forc_thr = args.force_thr or "1.0d-4"
    press_thr = args.press_thr or "0.5d0"
    nstep = args.nstep or "100"
    mixing = args.mixing or "0.5"
    upscale = args.upscale or "100.D0"

    content = f"""! QE vc-relax input file
! Generated by generate_vcrelax.py

&CONTROL
  calculation    = 'vc-relax'
  prefix         = '{args.prefix or 'system'}'
  pseudo_dir     = './psps'
  outdir         = './tmp/'
  tstress        = .true.
  tprnfor        = .true.
  etot_conv_thr  = 1.0d-5
  forc_conv_thr  = {forc_thr}
  nstep          = {nstep}
/

&SYSTEM
  nosym          = .true.
  ibrav          = 0
  nat            = {len(atoms)}
  ntyp           = {len(elements)}
  tot_charge     = 0.0
  ecutwfc        = {ecutwfc}
  ecutrho        = {ecutrho}
  occupations    = 'smearing'
  smearing       = 'mv'
  degauss        = 0.001
/

&ELECTRONS
  mixing_mode    = 'plain'
  mixing_beta    = {mixing}
  conv_thr       = {conv_thr}
/

&IONS
  upscale        = {upscale}
/

&CELL
  cell_dynamics  = 'bfgs'
  press_conv_thr = {press_thr}
  cell_dofree    = '{cell_dofree}'
/

ATOMIC_SPECIES
{chr(10).join(atomic_species)}

K_POINTS {{automatic}}
{k1} {k2} {k3} {k_shift}

CELL_PARAMETERS (angstrom)
{cell_params}

ATOMIC_POSITIONS (crystal)
{atomic_positions}
"""
    return content


def main():
    parser = argparse.ArgumentParser(
        description='Generate QE vc-relax input file',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  # Generate from atom list file
  generate_vcrelax.py atoms.txt lattice.txt -o vc-relax.in

  # Custom k-points and ecut
  generate_vcrelax.py atoms.txt lattice.txt -o vc-relax.in -k "6 6 6" --ecutwfc 60

  # Relax only volume (keep lattice shape)
  generate_vcrelax.py atoms.txt lattice.txt -o vc-relax.in --cell-dofree volume
        '''
    )

    parser.add_argument('atoms', help='Atoms file (format: element x y z per line)')
    parser.add_argument('lattice', nargs='?', help='Lattice vectors file (optional)')
    parser.add_argument('-o', '--output', default='vc-relax.in', help='Output file name')
    parser.add_argument('-p', '--prefix', default='system', help='Prefix for output files')
    parser.add_argument('-k', '--kpoints', help='K-point grid (e.g., "8 8 8" or "6,6,6")')
    parser.add_argument('--no-shift', action='store_true', help='Do not shift k-point grid')
    parser.add_argument('--ecutwfc', type=float, help='Planewave cutoff (Ry)')
    parser.add_argument('--ecutrho', type=float, help='Charge density cutoff (Ry)')
    parser.add_argument('--conv-thr', help='SCF convergence threshold (e.g., 1.0d-8)')
    parser.add_argument('--force-thr', help='Force convergence threshold')
    parser.add_argument('--press-thr', help='Pressure convergence threshold')
    parser.add_argument('--cell-dofree', choices=['all', 'volume', 'x', 'y', 'z', 'xy', 'xz', 'yz'],
                        help='Cell degrees of freedom to optimize')
    parser.add_argument('--nstep', type=int, help='Maximum ionic steps')
    parser.add_argument('--mixing', help='Mixing beta')
    parser.add_argument('--upscale', help='Ionic update upscale factor')

    args = parser.parse_args()

    # Parse atoms file
    if not os.path.exists(args.atoms):
        print(f"Error: Atoms file not found: {args.atoms}")
        return 1

    atoms = parse_atoms_file(args.atoms)
    if not atoms:
        print("Error: No atoms found in file")
        return 1

    print(f"Found {len(atoms)} atoms: {', '.join(dict.fromkeys([a[0] for a in atoms]))}")

    # Parse lattice vectors or use defaults
    if args.lattice:
        if not os.path.exists(args.lattice):
            print(f"Error: Lattice file not found: {args.lattice}")
            return 1
        lattice = parse_lattice_file(args.lattice)
    else:
        # Default simple cubic lattice
        lattice = [[3.9, 0.0, 0.0], [0.0, 3.9, 0.0], [0.0, 0.0, 3.9]]
        print("Using default lattice vectors (3.9 x 3.9 x 3.9)")

    # Generate input
    content = generate_vcrelax_input(atoms, lattice, args)

    # Write output
    with open(args.output, 'w') as f:
        f.write(content)

    print(f"Wrote: {args.output}")
    print("\nTo run:")
    print(f"  mkdir -p tmp/")
    print(f"  pw.x < {args.output} > {args.output.replace('.in', '.out')}")

    return 0


if __name__ == '__main__':
    exit(main())