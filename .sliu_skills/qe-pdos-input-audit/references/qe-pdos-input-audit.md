# QE PDOS Input Audit Reference

This reference supports `qe-pdos-input-audit` for quick, repeatable checks on
Quantum ESPRESSO PDOS workflows (`pw.x` + `projwfc.x`).

## 1. Minimum Consistency Set

Always align these across `scf.in`, `nscf.in`, and `pdos.in`:

- `prefix`
- `outdir`
- `pseudo_dir` (for `pw.x` stages)
- cell and atomic structure in SCF/NSCF
- `ecutwfc` and `ecutrho` in SCF/NSCF

If these drift, `projwfc.x` output may be missing, inconsistent, or physically misleading.

## 2. NSCF Input Checks

In `nscf.in`, verify:

- `calculation = 'nscf'`
- valid namelist syntax (commas/quotes/slashes)
- `nbnd` is high enough for the requested DOS window
- k-mesh is denser than SCF for smooth DOS

### Tetrahedra setup for sharper DOS

When the user asks for sharper DOS:

- set `occupations = 'tetrahedra'`
- use unshifted automatic mesh (`... 0 0 0`)

Do not combine this intent with unnecessary Gaussian broadening choices in post-processing unless explicitly requested.

## 3. PROJWFC Input Checks (`pdos.in`)

In `&PROJWFC`, verify:

- `prefix` and `outdir` match NSCF stage
- `DeltaE` is explicit and reasonable for the target plot resolution
- `Emin`/`Emax` span the report range
- `filpdos` naming is intentional

## 4. Job Script Sanity

Common mistake: script copied from Berry or bands workflow.

For PDOS, expected command chain is:

1. `pw.x -i scf.in > scf.out`
2. `pw.x -i nscf.in > nscf.out`
3. `projwfc.x -i pdos.in > pdos.out`

If stage 2/3 points to `berry.in`, `bands.in`, or unrelated files, patch before submission.

## 5. Output Validation Checklist

After run, verify:

- `scf.out` and `nscf.out` contain `JOB DONE`
- `nscf.out` contains `the Fermi energy is`
- `pdos.out` contains `JOB DONE`
- expected PDOS files exist: `*.pdos_atm*` and optionally `*.pdos_tot`

If files are absent, check `prefix/outdir`, failed NSCF stage, and `projwfc.x` input path.

