# Quantum Espresso (QE) Reference

This file documents Quantum Espresso related tools, workflows, and skills for phonon calculations.

---

## Table of Contents

1. [Quick Reference](#quick-reference)
2. [Structure Optimization](#structure-optimization)
   - [Variable-Cell Relaxation (vc-relax)](#variable-cell-relaxation-vc-relax)
   - [Extract Final Structure](#extract-final-structure)
   - [Re-optimization](#re-optimization)
3. [Phonon Calculation Workflow](#phonon-calculation-workflow)
4. [SCF Input Generation](#scf-input-generation)
5. [Phonon Input Generation](#phonon-input-generation)
6. [Parsing Phonon Outputs](#parsing-phonon-outputs)
7. [Plotting Phonon Dispersion](#plotting-phonon-dispersion)
8. [Helper Scripts](#helper-scripts)

---

## Quick Reference

| Step | Code | Purpose |
|------|------|---------|
| Ground state | `pw.x` | SCF calculation |
| Phonons at q | `ph.x` | Linear-response phonon calculation |
| Fourier interp. | `q2r.x` | q-space → real space force constants |
| Dispersion | `matdyn.x` | Real space → q-space interpolation |
| Plotting | `plot_phonon.py` | Generate phonon band plots |
| Structure relax | `pw.x` with `vc-relax` | Full ionic + cell optimization |
| Convert structure | `qe_out_to_vasp.py` | Extract final structure |

---

## Structure Optimization

### Variable-Cell Relaxation (vc-relax)

This performs full structural optimization including both atomic positions and unit cell parameters.

```bash
&CONTROL
  calculation    = 'vc-relax',
  prefix         = 'pto',
  pseudo_dir     = './psps',
  outdir         = './tmp/',
  tstress        = .true.,
  tprnfor        = .true.,
  etot_conv_thr  = 1.0d-5,
  forc_conv_thr  = 1.0d-4,
  nstep          = 100
/

&SYSTEM
  nosym          = .true.,      ! Disable symmetry for full relaxation
  ibrav          = 0,           ! Free lattice vectors
  nat            = 5,
  ntyp           = 3,
  ecutwfc        = 50.0,
  ecutrho        = 250.0,
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
  cell_dofree    = 'all'        ! Relax all cell parameters
/

ATOMIC_SPECIES
Pb  207.2    pb_pbesol_v1.uspp.F.UPF
Ti   47.867  ti_pbesol_v1.4.uspp.F.UPF
O    15.999  o_pbesol_v1.2.uspp.F.UPF

K_POINTS {automatic}
8 8 8 0 0 0

CELL_PARAMETERS (angstrom)
3.90  0.00  0.00
0.00  3.90  0.00
0.00  0.00  4.15

ATOMIC_POSITIONS (crystal)
Pb  0.0  0.0  0.00
Ti  0.5  0.5  0.51
O   0.5  0.5  0.01
O   0.5  0.0  0.51
O   0.0  0.5  0.51
```

**Key Parameters:**

| Parameter | Typical Value | Description |
|-----------|---------------|-------------|
| `calculation` | `'vc-relax'` | Variable-cell relaxation |
| `nosym` | `.true.` | Disable symmetry for full relaxation |
| `ibrav` | 0 | Free-form lattice vectors |
| `cell_dofree` | `'all'` or `'volume'` | Relax all cell or just volume |
| `cell_dynamics` | `'bfgs'` | BFGS optimizer (recommended) |
| `press_conv_thr` | 0.5 d0 | Pressure convergence threshold (kBar) |
| `etot_conv_thr` | 1.0d-5 | Energy convergence (Ry) |
| `forc_conv_thr` | 1.0d-4 | Force convergence (Ry/bohr) |

**Running the calculation:**
```bash
mkdir -p tmp/
pw.x < vc-relax.in > vc-relax.out
```

**Cell Degrees of Freedom Options:**
- `'all'` - Relax a, b, c and all angles
- `'volume'` - Only optimize volume (keep shape)
- `'x'`, `'y'`, `'z'` - Relax only along specific axis
- `'xy'`, `'xz'`, `'yz'` - Relax specific plane

### Extract Final Structure

After vc-relax completes, **always use qe_out_to_vasp.py** to extract the final optimized structure:

```bash
python qe_out_to_vasp.py vc-relax.out -o final_structure.vasp
```

**Important:** Do NOT manually extract from "Begin final coordinates" section - use the script. It handles:
- Locating the correct final coordinates in the output
- Parsing CELL_PARAMETERS and ATOMIC_POSITIONS
- Converting to VASP/POSCAR format

After extraction, analyze symmetry:
```bash
python find_sym.py final_structure.vasp -k refined
```

### Re-optimization

For better convergence, you can perform multiple relaxation steps:

1. **First pass**: Use stricter convergence or different optimizer
2. **Second pass**: Use the output structure as input for final optimization

Use `conv_thr = 1.0d-9` for the final run to get precise forces.

### Create Doped Supercell

Use `make_doped_supercell.py` to create supercells with dopants:

```bash
# Create 2x2x1 La-doped anatase supercell (24 atoms)
python make_doped_supercell.py anatase.cif La 1 -r "2 2 1" -o La_anatase.vasp

# Generate QE vc-relax.in automatically
python make_doped_supercell.py anatase.cif La 1 -r "2 1 1" --generate-qe

# Custom k-points and ecutwfc
python make_doped_supercell.py rutile.cif Nb 2 -r "2 2 1" -k 4 4 6 -e 60

# Multiple dopant atoms, random positions
python make_doped_supercell.py TiO2.cif Fe 3 -r "2 2 2" -s random
```

**Options:**

| Option | Description |
|--------|-------------|
| `-r, --repeat` | Supercell repetition (e.g., "2 2 1") |
| `-s, --site` | Site selection: first, last, random |
| `-k, --kpoints` | K-points grid (default: 6 6 6) |
| `-e, --ecutwfc` | Plane-wave cutoff in Ry (default: 50) |
| `--generate-qe` | Generate QE vc-relax.in file |

**Supported input formats:** CIF, POSCAR, CONTCAR, and other pymatgen-supported formats.

---

## Phonon Calculation Workflow

### Part I: Gamma-Point Phonon Calculation

In many cases, you only need phonon frequencies at the Brillouin zone center (Γ point). This is sufficient for:
- Checking dynamical stability (all phonon frequencies positive)
- Obtaining dielectric properties (Born effective charges and dielectric constant)
- Studying zone-center optical modes

**Complete workflow:**
```bash
# 1. Ground-state SCF
pw.x < scf.in > scf.out

# 2. Gamma-point phonons (with dielectric properties)
ph.x < ph-gamma.in > ph-gamma.out
```

### Part II: Phonon Dispersion

For full phonon dispersion along high-symmetry paths:

```bash
# 1. Ground-state SCF (use Gamma-centered k-grid)
pw.x < scf.in > scf.out

# 2. Phonons on q-grid
ph.x < ph-grid.in > ph-grid.out

# 3. Fourier interpolation
q2r.x < q2r.in > q2r.out

# 4. Dispersion along path
matdyn.x < disp.in > disp.out

# 5. Plot
python plot_phonon.py pto.disp.freq.gp --labels "Γ,X,M,Γ,Z"
```

---

## SCF Input Generation

### K-Point Grid: Gamma-Centered vs Shifted

**Gamma-centered grid (includes Γ point):**
```bash
K_POINTS {automatic}
8 8 8 0 0 0
```
Produces 75 k-points for 8×8×8 grid.

**Shifted grid (avoid Γ point):**
```bash
K_POINTS {automatic}
8 8 8 1 1 1
```
Produces 40 k-points for same grid size.

**Why shifted grid has fewer k-points:**
- Gamma-centered: Grid is symmetric around Γ, contains redundancy at zone center
- Shifted: Balanced distribution, each k-point is distinct when folded back

**Recommendation:**
- Use shifted grid to save computation time (40 vs 75 k-points)
- For fully optimized structures, results are NOT sensitive to the shift
- For **polar materials** needing accurate dielectric constants: use Gamma-centered

### Key SCF Parameters

| Parameter | Typical Value | Description |
|-----------|---------------|-------------|
| `ecutwfc` | 40-80 Ry | Plane-wave cutoff |
| `ecutrho` | 4× ecutwfv | Charge density cutoff |
| `conv_thr` | 1.0d-8 | SCF convergence threshold |
| `outdir` | ./tmp/ | Temporary files directory |

---

## Phonon Input Generation

### 1. Gamma-Point Phonons (ph.x)

```bash
&INPUTPH
  tr2_ph = 1.0d-14,
  prefix = 'pto',
  outdir = './tmp/',
  fildyn = 'pto.gamma.dyn',
  epsil  = .true.
 /
0.0 0.0 0.0
```

- `epsil = .true.`: Calculate Born effective charges and dielectric constant
- **Always use for polar/ferroelectric materials**

### 2. Q-Grid Phonons (ph.x with ldisp)

```bash
&INPUTPH
  tr2_ph = 1.0d-14,
  prefix = 'pto',
  outdir = './tmp/',
  fildyn = 'pto.dyn',
  ldisp = .true.,
  nq1 = 2, nq2 = 2, nq3 = 2
 /
```

- `ldisp = .true.`: Enable q-point grid calculation
- `nq1, nq2, nq3`: Grid dimensions (produce 8 q-points for 2×2×2)

### 3. Fourier Interpolation (q2r.x)

```bash
&input
  asr='crystal',
  amass(1) = 207.2   ! Pb
  amass(2) = 47.867  ! Ti
  amass(3) = 15.999  ! O
  flfrc='pto.222.fc'
  flfrq='pto.disp.freq'
 /
```

- `asr='crystal'`: Acoustic sum rule correction
- `amass(i)`: Atomic masses in amu (same order as ATOMIC_SPECIES)

### 4. Dispersion Path (matdyn.x)

```bash
&input
  asr='crystal',
  amass(1) = 207.2
  amass(2) = 47.867
  amass(3) = 15.999
  flfrc='pto.222.fc'
  flfrq='pto.disp.freq'
  q_in_band_form = .true.
  q_in_cryst_coord = .true.
 /
5
0.0 0.0 0.0 20   ! Γ (20 points)
0.5 0.0 0.0 20   ! X (20 points)
0.5 0.5 0.0 20   ! M (20 points)
0.0 0.0 0.0 20   ! Γ
0.0 0.0 0.5 1    ! Z
```

**Common High-Symmetry Points (Perovskite/Cubic):**

| Label | Coordinates | Description |
|-------|-------------|-------------|
| Γ | (0, 0, 0) | Zone center |
| X | (0.5, 0, 0) | Face center (100) |
| M | (0.5, 0.5, 0) | Face diagonal (110) |
| R | (0.5, 0.5, 0.5) | Zone corner (111) |
| Z | (0, 0, 0.5) | (001) face center |

---

## Parsing Phonon Outputs

### Extract Frequencies from dynmat.out

```bash
python parse_phonon.py dynmat.out
```

This script extracts:
- All phonon frequencies in cm⁻¹
- Negative frequencies (imaginary modes) warning
- Dynamical stability assessment

### Key Output Values

**From dynmat.out:**
```
omega(  1) =       -0.006838 [cm-1]   <- Imaginary (unstable)
omega(  2) =        0.006838 [cm-1]   <- Acoustic at Γ (~0)
omega(  3) =       87.234567 [cm-1]   <- Optical mode
```

**From ph-gamma.out** (requires `epsil = .true.`):
```
Z(*) =  effective charges    <- Born effective charges
epsilon (high frequency)    <- Electronic dielectric (ε∞)
epsilon (static)            <- Static dielectric (ε0)
```

### Interpretation Guide

| Quantity | Physical Meaning | Typical Values |
|----------|------------------|----------------|
| Negative ω | Imaginary frequency → instability | -10 to -100 cm⁻¹ |
| Acoustic modes at Γ | Should be ~0 cm⁻¹ | ≤ 1 cm⁻¹ |
| TO/LO split | Coulomb interaction in polar materials | 50-200 cm⁻¹ |
| Z\*(Pb) | Born charge for Pb | 3-5 (nominal: +2) |
| Z\*(Ti) | Born charge for Ti | 6-10 (nominal: +4) |
| ε∞ | Electronic dielectric | 3-10 |
| ε0 | Static dielectric | 10-100 (ferroelectrics) |

---

## Plotting Phonon Dispersion

### Basic Usage

```bash
python plot_phonon.py pto.disp.freq.gp --labels "Γ,X,M,Γ,Z"
```

### Full Options

```bash
python plot_phonon.py pto.disp.freq.gp \
    --labels "Γ,X,M,Γ,Z" \
    --freq-max 800 \
    --output PbTiO3_bands \
    --format pdf \
    --style publication
```

### Important: K-Point Labels

**You must manually set the k-point labels** to match your specific path:

| Path | Labels |
|------|--------|
| Γ-X-M-Γ-Z | `['Γ', 'X', 'M', 'Γ', 'Z']` |
| Γ-X-R-M | `['Γ', 'X', 'R', 'M']` |
| Γ-L-Γ | `['Γ', 'L', 'Γ']` |

The number of labels must match the number of high-symmetry points defined in your `matdyn.x` input (the first number in the file).

### Output Formats

| Format | Use Case |
|--------|----------|
| PNG | Presentations, posters (300+ DPI) |
| PDF | Publication-quality (vector) |
| EPS | Old journals, LaTeX |
| SVG | Web, editable |

---

## Helper Scripts

### Available Scripts

| Script | Purpose |
|--------|---------|
| [generate_vcrelax.py](scripts/generate_vcrelax.py) | Generate structure optimization input files |
| [generate_phonon_workflow.py](scripts/generate_phonon_workflow.py) | Generate complete phonon dispersion workflow |
| [make_heterostructure.py](scripts/make_heterostructure.py) | Create heterostructures/superlattices with termination control |
| [make_doped_supercell.py](scripts/make_doped_supercell.py) | Create doped supercells by replacing host atoms with dopants |
| [qe_out_to_vasp.py](scripts/qe_out_to_vasp.py) | Extract final structure from QE output to VASP |
| [find_sym.py](scripts/find_sym.py) | Analyze and symmetrize crystal structures |
| [analyze_results.py](scripts/analyze_results.py) | Analyze findMetal.py database results |
| [plot_phonon.py](scripts/plot_phonon.py) | Generate phonon band structure plots |
| [parse_phonon.py](scripts/parse_phonon.py) | Extract frequencies, Born charges from outputs |
| [split_modes.py](scripts/split_modes.py) | Split dynmat.axsf into separate XSF files |

### Generate Structure Optimization Input

```bash
# From atom list file
python generate_vcrelax.py atoms.txt lattice.txt -o vc-relax.in

# Custom k-points and cutoff
python generate_vcrelax.py atoms.txt -o vc-relax.in -k "6 6 6" --ecutwfc 60

# Relax only volume (keep shape)
python generate_vcrelax.py atoms.txt -o vc-relax.in --cell-dofree volume
```

**Atoms file format:**
```
Pb  0.0  0.0  0.0
Ti  0.5  0.5  0.5
O   0.5  0.5  0.0
O   0.5  0.0  0.5
O   0.0  0.5  0.5
```

**Lattice file format (optional):**
```
3.90  0.00  0.00
0.00  3.90  0.00
0.00  0.00  4.15
```

### Generate Complete Phonon Workflow

Generate all files for a phonon dispersion calculation from a structure file:

```bash
# Basic usage (from POSCAR)
python generate_phonon_workflow.py POSCAR

# From QE vc-relax output
python generate_phonon_workflow.py vc-relax.in

# Custom settings
python generate_phonon_workflow.py POSCAR \
    -k 6 6 6 \              # K-points
    -q 3 3 3 \              # Q-grid for phonons
    --tot-charge 0.4 \      # Doping (holes)
    --path G,X,M,G,Z        # High-symmetry path
```

**Output Directory Structure:**
```
<prefix>-phonon-dispersion/
├── 00SCF/scf.in         # SCF input
├── 02Grid/ph-grid.in    # Phonon q-grid input
├── 03q2r/q2r.in         # Fourier interpolation
├── 04matdyn/matdyn.in   # Dispersion path
├── 05Plot/plot_phonon.py
├── psps/                # (empty - copy pseudopotentials here)
├── tmp/                 # QE temp files
└── run_phonon.sh        # Job script
```

**Workflow execution:**
```bash
cd <prefix>-phonon-dispersion
# Copy pseudopotentials to psps/
cp ../path/to/psps/*.UPF psps/
sbatch run_phonon.sh
```

### Create Heterostructure / Superlattice

Create heterostructures by stacking 2D materials with control over terminations:

```bash
# Basic Ca2F2 / TiO2 / Ca2F2 sandwich
python make_heterostructure.py Ca2F2.vasp TiO2.cif -n 2 -g 3 -o sandwich.vasp

# Control TiO2 termination (O at both interfaces)
python make_heterostructure.py Ca2F2.vasp TiO2.cif --bottom-term O --top-term O -n 2

# Options:
# -n, --nlayers N   Number of unit cells of top layer
# -g, --gap ANG     Gap between layers (default: 3.0 Å)
# -r, --ref         ab lattice: first/last/average
# -b, --bottom-term O/Ti   Bottom termination
# -t, --top-term    O/Ti   Top termination
```

### Analyze findMetal.py Results

Analyze database query results, filter by lattice constant and sort:

```bash
# Find candidates with a ~ 4.7 Å, sorted by workfunction
python analyze_results.py Results.txt -t 4.7 -r 0.3 -s workfunction

# Top 10 closest to target
python analyze_results.py Results.txt -t 4.7 -r 0.2 -s a -n 10
```

### Phonon Visualization Workflow

1. Run phonon calculation (`ph.x`)
2. Post-process with `dynmat.x` to generate `dynmat.axsf`
3. Use `split_modes.py` to extract individual modes:

   ```bash
   python3 split_modes.py dynmat.axsf
   ```

4. Visualize with VESTA or XCrysDen:

   ```bash
   xcrysden --xsf dynmat_mode06.xsf
   ```

---

## Default Pseudopotentials (GBRV PBEsol)

These pseudopotentials are used by default in the workflow:

| Element | Mass (amu) | Pseudopotential File |
|---------|------------|---------------------|
| O | 15.999 | `o_pbesol_v1.2.uspp.F.UPF` |
| Ti | 47.867 | `ti_pbesol_v1.4.uspp.F.UPF` |
| Pb | 207.2 | `pb_pbesol_v1.uspp.F.UPF` |

The script `generate_vcrelax.py` includes built-in mappings for common elements.

**Location:** Place pseudopotentials in `./psps/` directory relative to your input file.

---

## Atomic Masses Reference

| Element | Mass (amu) |
|---------|------------|
| H | 1.008 |
| C | 12.011 |
| N | 14.007 |
| O | 15.999 |
| Ti | 47.867 |
| Fe | 55.845 |
| Cu | 63.546 |
| Zn | 65.38 |
| Sr | 87.62 |
| Zr | 91.224 |
| Nb | 92.906 |
| Ba | 137.327 |
| La | 138.905 |
| Pb | 207.2 |

---

## Common Issues

| Issue | Solution |
|-------|----------|
| Slow SCF convergence | Increase `mixing_beta` or `ecutwfc` |
| Wrong prefix/outdir in ph.x | Must match SCF calculation |
| Missing q2r output | Ensure all pto.dyn* files exist |
| Negative frequencies | Structure is dynamically unstable |
| acafcs error in matdyn | Check atomic masses match in q2r and matdyn |
| K-point labels wrong in plot | Manually edit labels in plotting command |