---
name: qe-phonopy-fd
description: Use when work in Sandbox needs a Phonopy finite-displacement phonon workflow with Quantum ESPRESSO, including checking the relaxed structure, symmetry cleanup before `phonopy --qe -d`, building displaced SCF inputs, assembling `FORCE_SETS`, adding `BORN`, or diagnosing failed QE plus Phonopy phonon runs.
---

# QE Phonopy Finite Displacement

Use this skill for finite-displacement phonons with Phonopy and QE.

## First Read

- Read `../references/qe-phonopy-fd.md`.
- If the starting structure may have lost symmetry, also read `../references/qe-structure.md`.
- Use `../scripts/qe_out_to_vasp.py` and `../scripts/find_sym.py` before copying structures manually.
- If Phonopy unexpectedly falls to low symmetry or generates too many displacements, route to `../qe-symmetry-repair/SKILL.md`.
- Reuse project-local `head`, `scan.bash`, and loop scripts when they already exist and match the workflow.

## Core Workflow

1. Start from a fully optimized reference structure. If only a QE output exists, extract the last structure first and check whether it still matches the intended symmetry.
2. For symmetry-sensitive workflows, prefer a structure that QE accepts with `nosym = .false.` without a meaningful extra ionic or cell move.
3. Generate displacements with `phonopy --qe -d --dim="..." -c M.in -v`. Do not use the removed `--pwscf` flag.
4. Build complete QE SCF inputs for each displaced supercell. Keep `calculation = 'scf'`, `tprnfor = .true.`, matching `nat/ntyp`, and usually `nosym = .true.` for the displaced jobs.
5. Run one SCF calculation per displaced supercell. Do not relax them and do not reorder atoms.
6. Build `FORCE_SETS` with `phonopy --qe -f ...`, then continue to `band.conf` and optional `BORN` if the user needs the final phonon bands.

## Checks That Matter

- The symmetry of the starting structure directly controls how many displaced supercells Phonopy generates.
- `nat`, `ntyp`, `pseudo_dir`, `outdir`, and `K_POINTS` in the displaced-input header must match the generated supercell workflow.
- Relative paths such as `./psps` and `./tmp` only work if the QE jobs are launched from the directory those paths were written for.
- `FORCE_SETS` fails if any displaced job is missing, forces were not printed, or atom ordering changed.
- NAC only makes sense when the `BORN` file is consistent with the same structure convention used by Phonopy.

## Related References

- `../references/qe-phonopy-fd.md` for the detailed step-by-step workflow
- `../references/qe-structure.md` for extraction, supercell preparation, and symmetry cleanup
- `../references/qe-troubleshooting.md` for P1 fallback, environment issues, and path mistakes
- `../references/scripts.md` for the shared structure and phonon helper CLIs
