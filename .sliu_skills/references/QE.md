# Quantum Espresso (QE) Reference

This file documents Quantum Espresso related tools, workflows, and skills for phonon calculations.

---

## Table of Contents

1. [Quick Reference](#quick-reference)
2. [Phonon Calculation Workflow](#phonon-calculation-workflow)
3. [SCF Input Generation](#scf-input-generation)
4. [Phonon Input Generation](#phonon-input-generation)
5. [Parsing Phonon Outputs](#parsing-phonon-outputs)
6. [Plotting Phonon Dispersion](#plotting-phonon-dispersion)
7. [Helper Scripts](#helper-scripts)

---

## Quick Reference

| Step | Code | Purpose |
|------|------|---------|
| Ground state | `pw.x` | SCF calculation |
| Phonons at q | `ph.x` | Linear-response phonon calculation |
| Fourier interp. | `q2r.x` | q-space → real space force constants |
| Dispersion | `matdyn.x` | Real space → q-space interpolation |
| Plotting | `plot_phonon.py` | Generate phonon band plots |

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
| [plot_phonon.py](scripts/plot_phonon.py) | Generate phonon band structure plots |
| [parse_phonon.py](scripts/parse_phonon.py) | Extract frequencies, Born charges from outputs |
| [split_modes.py](scripts/split_modes.py) | Split dynmat.axsf into separate XSF files |
| [qe_out_to_vasp.py](scripts/qe_out_to_vasp.py) | Extract final structure from QE output to VASP |
| [find_sym.py](scripts/find_sym.py) | Analyze and symmetrize crystal structures |

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