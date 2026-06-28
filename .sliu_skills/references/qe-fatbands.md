---
name: qe-fatbands-reference
description: Quantum ESPRESSO projected / fat band workflow. Run projwfc.x with filproj='fatband', format projections with qe_format_fatbands.py, and plot with qe_plot_fatbands.py.
---

# QE Fatbands Workflow

Use this reference when the user asks for projected band structures, fatbands, or orbital-character plots from Quantum ESPRESSO.

## Quick Route

1. Run a converged SCF calculation.
2. Run `pw.x` with `calculation = 'bands'` along an explicit high-symmetry path.
3. Run `projwfc.x` with `filproj = 'fatband'`.
4. Format projections with `qe_format_fatbands.py`.
5. Create/edit a `.projs` file selecting the orbitals to plot.
6. Plot with `qe_plot_fatbands.py --fatband`.

## Required QE Outputs

| File | Produced by | Purpose |
|------|-------------|---------|
| `bands.out` | `pw.x` (`calculation = 'bands'`) | Band eigenvalues and k-path |
| `klabel` | User | High-symmetry point labels |
| `projwfc.out` | `projwfc.x` | Atomic state definitions |
| `fatband.projwfc_up` | `projwfc.x` (`filproj='fatband'`) | Raw projection weights |
| `fatband.projwfc_down` | `projwfc.x` (spin-polarized) | Spin-down projection weights |

## projwfc.x Input Example

```text
&projwfc
    outdir='./tmp/'
    prefix='system'
    lsym=.false.
    filproj = 'fatband'
/
```

Use the same `prefix` and `outdir` as the SCF and bands steps.

## Formatting Projections

Run the formatter from the directory containing `projwfc.out` and `fatband.projwfc_up`:

```bash
python3 ~/Sandbox/.sliu_skills/scripts/qe_format_fatbands.py \
    -i projwfc.out \
    -p fatband.projwfc_up \
    -o fatband_formatted
```

Arguments:

| Argument | Default | Description |
|----------|---------|-------------|
| `-i, --input` | `projwfc.out` | `projwfc.x` output file |
| `-p, --proj` | `fatband.projwfc_up` | Raw projection file |
| `-o, --output` | `fatband_formatted` | Output base name |
| `-v, --verbose` | off | Print detailed diagnostics |

Outputs:

- `<output>.npy` — NumPy array of shape `(nlorbs, nks, nbands)`
- `<output>.projs` — Auto-generated projection definitions
- `<output>.summary` — Human-readable state summary

## The `.projs` File Format

The projection definition file has one header line with the number of projections, followed by one line per projection:

```text
<num_projections>
<element> <orbital> [<atom_numbers>] <color>
```

### Examples

All atoms of a type:

```text
2
Ti d tab:red
Pb d tab:blue
```

Specific atoms:

```text
2
Ti d 1 tab:red
O p 3 tab:blue
```

Multiple specific atoms:

```text
2
O p 1,3 tab:green
Ti d tab:red
```

Color names follow matplotlib conventions (`tab:red`, `tab:blue`, `tab:green`, `tab:orange`, `tab:purple`, ...).

## Plotting

### Plain Bands

```bash
python3 ~/Sandbox/.sliu_skills/scripts/qe_plot_fatbands.py \
    -o bands.out -k klabel -n pbe -e 4 4 2 -fe 1 -r
```

### Fatbands

```bash
python3 ~/Sandbox/.sliu_skills/scripts/qe_plot_fatbands.py \
    -o bands.out \
    -k klabel \
    -n pbe \
    -e 5 5 2 \
    -fe 3 6.5 \
    -r \
    --fatband \
    --proj plot.projs \
    --proj-data fatband_formatted.npy \
    --proj-source projwfc.out \
    --scale 100
```

Common arguments:

| Argument | Default | Description |
|----------|---------|-------------|
| `-o, --output` | required | QE bands output file |
| `-k, --klabels` | None | `klabel` file |
| `-n, --name` | `pbe` | Tag for output filenames |
| `-e EMIN EMAX ESTEP` | `4 4 2` | Energy window relative to Fermi |
| `-fe MODE [VALUE]` | `1` | Fermi reference: `1`=(VBM+CBM)/2, `2`=VBM, `3`=value |
| `-s {1,2,4}` | `1` | Spin treatment |
| `-ne NUP NDN` | None | Electron counts for `nspin=2` |
| `-r, --raw` | off | Export raw band data |
| `--fatband` | off | Enable fatband overlay |
| `--proj` | required with `--fatband` | `.projs` file |
| `--proj-data` | required with `--fatband` | `.npy` projection data |
| `--proj-source` | `projwfc.out` (current dir) | `projwfc.x` output used to resolve state indices |
| `--scale` | `100` | Marker-size scale factor |

### Energy Range Convention

`-e 5 5 2` means plot from **-5 eV** to **+5 eV** relative to the chosen Fermi reference, with y-axis ticks every 2 eV.

### Fermi Reference Modes

- `-fe 1` : midpoint of VBM and CBM (default)
- `-fe 2` : VBM
- `-fe 3 6.5` : user-specified value, here 6.5 eV

## Projection Data Layout

The `.npy` file stores a 3D array:

```python
import numpy as np
proj = np.load('fatband_formatted.npy')  # shape: (nlorbs, nks, nbands)
weight = proj[state_index, kpoint_index, band_index]
```

State/k-point/band numbers in the summary are **1-based**. Subtract 1 when indexing the NumPy array directly.

Example — sum all Ti d states (states 6–10 in 1-based = indices 5–9 in 0-based):

```python
ti_d = [5, 6, 7, 8, 9]
weight = proj[ti_d, :, :].sum(axis=0)
```

## Generated Files

Without `--fatband`:

- `<bands.out>_<name>.png`
- `<bands.out>_<name>.eps`
- `<name>_bands.dat` (with `-r`)
- `xklabel.dat` (with `-r`)

With `--fatband`:

- All of the above
- `<bands.out>_fatband_<name>.png`
- `<bands.out>_fatband_<name>.eps`

## Troubleshooting

### No markers appear in the fatband plot
- Check the energy range (`-e`) covers the bands of interest.
- Verify element/orbital names in the `.projs` file match `fatband_formatted.summary`.
- Make sure `bands.out` and `projwfc.out` are from the same calculation.

### Fermi level looks shifted
- Use `-fe 3 <value>` to set the Fermi energy explicitly from `scf.out`.
- Confirm `bands.out` and the projection files share the same reference.

### K-point labels do not match
- Ensure the number of labels in `klabel` equals the number of special-point boundaries detected along the path.
- Check the `K_POINTS {crystal_b}` path in `bands.in`.
