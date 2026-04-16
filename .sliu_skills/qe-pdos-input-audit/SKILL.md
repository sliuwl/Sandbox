---
name: qe-pdos-input-audit
description: Use when work in Sandbox needs a Quantum ESPRESSO PDOS input audit or setup, including reviewing or fixing `scf.in`, `nscf.in`, and `pdos.in` or `projwfc.x` consistency, correcting syntax and keyword issues, aligning `prefix` and `outdir` with cutoffs and k-mesh, checking tetrahedra vs smearing choices for DOS sharpness, and verifying that job scripts run SCF to NSCF to PROJWFC instead of unrelated stages.
trigger:
  - "pdos"
  - "projected dos"
  - "dos"
  - "projwfc"
  - "nscf"
  - "density of states"
  - "total dos"
out_of_scope:
  - "band structure plotting"
  - "phonon calculations"
  - "Wannier functions"
---

# QE PDOS Input Audit

Use this skill for QE projected DOS preparation and validation before launching or rerunning jobs.

## First Read

- Read `../references/QE.md` for baseline QE input conventions already used in this workspace.
- Read `references/qe-pdos-input-audit.md` in this skill for PDOS-specific checks and fix patterns.
- Reuse local scripts in the target PDOS folder (`sum_states.py`, `plot_sum_dos.py`) before writing new one-off parsing scripts.

## Core Workflow

1. Confirm the PDOS target files belong to the same workflow directory and are mutually consistent: `scf.in`, `nscf.in`, `pdos.in`, and job script (`gpu_qe.sbatch` or equivalent).
2. In `nscf.in`, enforce basic validity first: proper namelist syntax, consistent `prefix`/`outdir`/`pseudo_dir`, matching structure and cutoffs vs SCF, and a sufficient `nbnd`.
3. For sharper DOS when requested, set `occupations = 'tetrahedra'` in NSCF and use an unshifted k-grid (`... 0 0 0`). Keep this decision explicit in comments.
4. In `pdos.in` (`&PROJWFC`), align `prefix` and `outdir` with SCF/NSCF; keep energy window and `DeltaE` explicit; avoid conflicting broadening settings when tetrahedra behavior is the intent.
5. Audit the batch script command sequence and patch mismatches so the run order is SCF -> NSCF -> PROJWFC (`pw.x`, `pw.x`, `projwfc.x`).
6. Validate by checking outputs for expected markers (`the Fermi energy is`, `JOB DONE`, generated `*.pdos_atm*` files) before post-processing.

## Checks That Matter

- `prefix` and `outdir` must match across SCF, NSCF, and PROJWFC inputs.
- NSCF cutoffs and crystal definition should match SCF; do not silently drift input physics between stages.
- `occupations = 'tetrahedra'` improves DOS sharpness only when k-mesh quality is adequate and the mesh is unshifted.
- `pdos.in` energy window (`Emin`, `Emax`) should cover the reporting range actually needed.
- Job scripts copied from Berry/bands workflows commonly point to the wrong second stage; always check command lines.

## Related References

- `references/qe-pdos-input-audit.md` for PDOS-specific audit checklist and concrete fix snippets.
- `../references/QE.md` for shared QE conventions in this workspace.

## Available Scripts

| Script | Purpose | CLI Example |
|--------|---------|-------------|
| Local: `sum_states.py` | Sum PDOS contributions | `python sum_states.py` |
| Local: `plot_sum_dos.py` | Plot total DOS | `python plot_sum_dos.py` |
| `../scripts/qe_out_to_vasp.py` | Extract structure from QE output | `python qe_out_to_vasp.py scf.out` |
