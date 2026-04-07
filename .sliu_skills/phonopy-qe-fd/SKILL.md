---
name: phonopy-qe-fd
description: Use when work in Sandbox needs a Phonopy finite-displacement workflow with Quantum ESPRESSO, including preparing a symmetry-clean reference structure, running `phonopy --qe -d`, building displaced SCF inputs, generating run loops, assembling `FORCE_SETS`, or documenting/debugging the workflow.
---

# Phonopy QE Finite Displacement

Use this skill for Phonopy finite-displacement phonon workflows driven by Quantum ESPRESSO SCF force calculations.

## First Read

- Read `../references/qe-phonopy-fd.md`.
- If the starting structure may have lost symmetry, also read `../references/qe-structure.md` and `../references/qe-troubleshooting.md`.
- Reuse existing shared scripts first: `../scripts/qe_out_to_vasp.py` and `../scripts/find_sym.py`.
- Reuse project-local `head`, `scan.bash`, and loop scripts when they already exist.

## Core Workflow

1. Confirm that the reference structure is fully optimized.
2. For symmetry-sensitive runs, prefer a symmetrized structure that QE accepts with `nosym = .false.`.
3. Generate displaced supercells with `phonopy --qe -d --dim="..." -c M.in -v`. Do not use the removed `--pwscf` flag.
4. Build a `head` file for displaced SCF runs. Keep `calculation = 'scf'`, `tprnfor = .true.`, and usually `nosym = .true.` for the displaced supercells.
5. Concatenate `head` with each `supercell-XXX.in` file to create the final displaced QE inputs. Prefer an existing `scan.bash` or an equivalent project-local script.
6. Run one QE SCF calculation per displaced supercell. Do not relax displaced structures and do not change atom ordering.
7. Build `FORCE_SETS` with `phonopy --qe -f ...`.
8. If the user needs the final spectrum, continue to `band.conf`, optional `BORN`, and the Phonopy plotting step.

## Checks That Matter

- The symmetry of the starting structure controls how many displaced supercells Phonopy generates.
- `nat`, `ntyp`, `pseudo_dir`, `outdir`, and `K_POINTS` in `head` must match the generated supercell workflow.
- If `head` uses relative paths such as `./psps` and `./tmp`, run the QE jobs from the directory those paths were written for.
- For displaced SCF jobs, forces must be printed and the run must finish cleanly.

## Related References

- `../references/qe-structure.md` for extracting relaxed structures, symmetry cleanup, and choosing refined/conventional/primitive cells
- `../references/qe-troubleshooting.md` for `spglib`, P1 fallback, parsing failures, and path mistakes
- `../references/scripts.md` for detailed CLI options of the shared helper scripts
