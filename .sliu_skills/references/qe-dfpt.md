---
name: qe-dfpt-reference
description: Density-functional perturbation theory phonon workflows in Quantum ESPRESSO using `ph.x`, `q2r.x`, and `matdyn.x`.
---

# QE DFPT Phonon Workflow

Use this reference when the user asks for phonons from QE’s DFPT stack instead of Phonopy finite displacements.

## Quick Route

- SCF with `pw.x`
- phonons with `ph.x`
- real-space force constants with `q2r.x`
- band interpolation with `matdyn.x`
- plotting with `plot_phonon.py`

## Gamma-Point Phonons

For a zone-center stability check:

```bash
pw.x < scf.in > scf.out
ph.x < ph-gamma.in > ph-gamma.out
```

For polar materials, include:

```text
epsil = .true.
```

so the dielectric tensor and Born effective charges are computed.

## Phonon Dispersion from a q-Grid

Typical flow:

```bash
pw.x < scf.in > scf.out
ph.x < ph-grid.in > ph-grid.out
q2r.x < q2r.in > q2r.out
matdyn.x < matdyn.in > matdyn.out
python3 ~/Sandbox/.sliu_skills/scripts/plot_phonon.py system.disp.freq.gp --labels "Γ,X,M,Γ,Z"
```

## Minimal Input Patterns

### `ph.x` on a q-grid

```text
&INPUTPH
  tr2_ph = 1.0d-14,
  prefix = 'system',
  outdir = './tmp/',
  fildyn = 'system.dyn',
  ldisp  = .true.,
  nq1    = 2,
  nq2    = 2,
  nq3    = 2
/
```

### `q2r.x`

```text
&input
  asr   = 'crystal',
  amass(1) = 207.2,
  amass(2) = 47.867,
  amass(3) = 15.999,
  flfrc = 'system.fc',
  flfrq = 'system.freq'
/
```

### `matdyn.x`

```text
&input
  asr              = 'crystal',
  amass(1)         = 207.2,
  amass(2)         = 47.867,
  amass(3)         = 15.999,
  flfrc            = 'system.fc',
  flfrq            = 'system.freq',
  q_in_band_form   = .true.,
  q_in_cryst_coord = .true.
/
```

Then append the number of path points and the coordinates of each high-symmetry point.

## K-Point Advice

- Gamma-centered grids are safer for polar materials and dielectric properties.
- Shifted grids can reduce the irreducible k-point count and save time for nonpolar cases.
- Keep `prefix` and `outdir` consistent across `pw.x`, `ph.x`, `q2r.x`, and `matdyn.x`.

## Common Outputs

- `ph-gamma.out`: frequencies and optional dielectric data at Gamma
- `*.dyn*`: dynamical matrices
- `*.fc`: real-space force constants
- `*.freq` or `*.disp.freq`: interpolated frequencies

## Script Support

- `parse_phonon.py` for extracting frequencies from QE phonon outputs
- `plot_phonon.py` for band plotting
- `split_modes.py` for splitting `dynmat.axsf` into individual mode files
