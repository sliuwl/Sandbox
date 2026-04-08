---
name: qe-bands-reference
description: Quantum ESPRESSO band-structure workflows in Sandbox using a converged SCF run, `pw.x` with `calculation = 'bands'`, explicit `K_POINTS {crystal_b}`, `klabel`, and the shared `qe_plot_bands.py` plotting script.
---

# QE Bands Workflow

Use this reference when the user asks for a standard QE band structure from `pw.x` rather than DOS, projected bands, or Wannier workflows.

## Quick Route

- run a converged SCF calculation
- reuse the same `prefix`, `outdir`, structure, and pseudopotentials
- run `pw.x` with `calculation = 'bands'` along an explicit high-symmetry path
- label the special points with `klabel`
- plot with `qe_plot_bands.py`

## Minimum Input Pattern

### `scf.in`

The SCF stage should provide the ground-state charge density and wavefunctions:

```text
&CONTROL
  calculation = 'scf',
  prefix = 'system',
  pseudo_dir = './psps',
  outdir = './tmp/'
/
...
K_POINTS {automatic}
8 8 8 0 0 0
```

### `bands.in`

The band-path stage should reuse the same system definition:

```text
&CONTROL
  calculation = 'bands',
  prefix = 'system',
  outdir = './tmp/'
/
&SYSTEM
  ...
  nbnd = 30,
/
...
nosym = .true.
K_POINTS {crystal_b}
```

Practical rules:

- keep `prefix` and `outdir` identical to the SCF stage
- use the same lattice, atomic positions, and pseudopotentials
- set `nbnd` high enough to include the conduction bands you want to inspect
- `nosym = .true.` is usually the safest choice for an explicit path

## How `K_POINTS {crystal_b}` Works

For `K_POINTS {crystal_b}`, the fourth number is the number of interpolated points from the current vertex to the next one.

Example:

```text
K_POINTS {crystal_b}
4
0.0 0.0 0.0 30
0.5 0.0 0.0 30
0.5 0.5 0.0 30
0.0 0.0 0.0  0
```

This means:

- `Gamma -> X` sampled with 30 points
- `X -> M` sampled with 30 points
- the final `0` closes the list without interpolating to an extra next segment

For path breaks such as `Z|X`, place `0` on the point before the discontinuity. That tells QE not to connect the previous segment continuously to the next one.

## Building `klabel`

The `klabel` file should contain one label per special-point boundary detected along the plotted path.

Example:

```text
$\Gamma$
X
M
$\Gamma$
Z|X
R
```

Rules:

- the number of labels must match the number of special positions in the plotted path
- `Z|X` style labels are used when the path is intentionally discontinuous
- if the label count is wrong, the plotting script can still continue, but the output will be misaligned or padded

## How To Choose the Path

Use one of these routes:

- published convention for the target lattice when direct comparison to literature matters
- SeeK-path when a standardized symmetry-consistent path is preferred
- `pymatgen` `HighSymmKpath` when the structure is already in a Python-based workflow

If the relaxed structure is only slightly distorted numerically, symmetrize or at least analyze it first, then generate the path from the cleaned structure. Otherwise the automatically generated path may collapse to unnecessarily low symmetry.

## Plotting With `qe_plot_bands.py`

Show the help:

```bash
python3 ~/Sandbox/.sliu_skills/scripts/qe_plot_bands.py --help
```

Typical example:

```bash
python3 ~/Sandbox/.sliu_skills/scripts/qe_plot_bands.py \
  -o bands.out \
  -k klabel \
  -e 4 4 2 \
  -n pbe \
  -fe 1 \
  -r
```

Useful flags:

- `-o`: QE `bands` output file to parse
- `-k`: label file
- `-e below above step`: plot window relative to the chosen Fermi reference
- `-fe 1`: use `(VBM + CBM) / 2`
- `-fe 2`: use `VBM`
- `-fe 3 VALUE`: use an explicit Fermi energy in eV
- `-r`: export raw data files in addition to the figure

## Common Failure Modes

- `bands.in` does not reuse the SCF `prefix` or `outdir`
- `nbnd` is too small to include the conduction bands of interest
- the structure or symmetry used to generate the path does not match the structure used in the calculation
- `klabel` has the wrong number of entries
- the Python environment used for plotting is missing `numpy` or `matplotlib`

## Related References

- `qe-structure.md` for structure extraction and symmetry cleanup
- `qe-troubleshooting.md` for parser, symmetry, and environment failures
- `scripts.md` for the shared script CLI details
