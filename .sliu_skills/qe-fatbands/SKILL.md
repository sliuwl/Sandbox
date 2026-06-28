---
name: qe-fatbands
description: Quantum ESPRESSO projected / fat band workflow. Trigger when the user asks for fatbands, projected band structures, orbital character plots, or post-processing of projwfc.x output.
trigger:
  - "fatband"
  - "fatbands"
  - "projected band"
  - "projected bands"
  - "projwfc"
  - "orbital character"
  - "band projection"
out_of_scope:
  - "plain band structure without projection"
  - "Wannier functions"
  - "DOS / PDOS only"
---

# QE Fatbands Skill

Use this skill when the user wants a **projected band structure** (fatbands) from a Quantum ESPRESSO calculation.

Fatbands show the orbital character of each band by scaling marker sizes according to the projection weight of selected atomic orbitals.

## First Read

- Reference documentation: `../references/qe-fatbands.md`
- Shared scripts:
  - `../scripts/qe_format_fatbands.py`
  - `../scripts/qe_plot_fatbands.py`

## Prerequisites

1. A converged SCF calculation.
2. A `pw.x` `calculation = 'bands'` run producing `bands.out` and a `klabel` file.
3. A `projwfc.x` run with `filproj = 'fatband'` producing:
   - `projwfc.out`
   - `fatband.projwfc_up`
   - (for spin-polarized: also `fatband.projwfc_down`)

## Core Workflow

### Step 1: Parse the projection data

```bash
python3 ~/Sandbox/.sliu_skills/scripts/qe_format_fatbands.py \
    -i /path/to/projwfc.out \
    -p /path/to/fatband.projwfc_up \
    -o /path/to/fatband_formatted
```

This creates:

- `fatband_formatted.npy` — projection array `(nlorbs, nks, nbands)`
- `fatband_formatted.projs` — auto-generated projection definitions
- `fatband_formatted.summary` — human-readable state summary

### Step 2: (Optional) Customize the projection file

Edit `fatband_formatted.projs` or create a `plot.projs` file:

```text
2
Ti d tab:red
Pb d tab:blue
```

See `../references/qe-fatbands.md` for the full `.projs` format, including how to select specific atoms.

### Step 3: Plot the fatbands

```bash
python3 ~/Sandbox/.sliu_skills/scripts/qe_plot_fatbands.py \
    -o /path/to/bands.out \
    -k /path/to/klabel \
    -n pbe \
    -e 5 5 2 \
    -fe 3 6.5 \
    -r \
    --fatband \
    --proj /path/to/plot.projs \
    --proj-data /path/to/fatband_formatted.npy \
    --proj-source /path/to/projwfc.out \
    --scale 100
```

This produces:

- `bands.out_pbe.png/.eps` — plain band structure
- `bands.out_fatband_pbe.png/.eps` — fatband plot
- `pbe_bands.dat` and `xklabel.dat` when `-r` is used

## Checks That Matter

- `bands.out` and `projwfc.out` must come from the **same** calculation so they share the same Fermi reference.
- The number of labels in `klabel` must match the number of special-point boundaries detected along the path.
- The `.projs` element/orbital names must match those listed in `fatband_formatted.summary`.
- State numbers in the summary are **1-based** (QE convention); the scripts handle the conversion internally.

## Related References

- `../references/qe-bands.md` — plain band structure workflow
- `../references/qe-pdos-input-audit.md` — PDOS / `projwfc.x` input checks
- `../references/scripts.md` — all shared scripts
