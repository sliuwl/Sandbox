---
name: qe-dfpt-phonon
description: Use when work in Sandbox needs Quantum ESPRESSO DFPT phonons with `ph.x`, `q2r.x`, and `matdyn.x`, including reviewing inputs, choosing q-meshes, diagnosing imaginary modes, and plotting or interpreting QE phonon dispersions.
---

# QE DFPT Phonon

Use this skill for phonons from QE's native DFPT stack rather than finite-displacement Phonopy workflows.

## First Read

- Read `../references/qe-dfpt.md`.
- Use `../scripts/parse_phonon.py` and `../scripts/plot_phonon.py` before writing one-off parsing code.
- Open `../references/qe-troubleshooting.md` when phonon jobs fail, frequencies look unphysical, or interpolation results are inconsistent.

## Core Workflow

1. Start from a converged SCF run and keep `prefix` and `outdir` consistent across `pw.x`, `ph.x`, `q2r.x`, and `matdyn.x`.
2. For Gamma-only work, run `ph.x` at `q = 0 0 0`. For polar materials or LO-TO analysis, include `epsil = .true.`.
3. For a dispersion, run `ph.x` on a uniform q-grid with `ldisp = .true.` and explicit `nq1/nq2/nq3`.
4. Use `q2r.x` to build real-space force constants, then `matdyn.x` to interpolate along the high-symmetry path.
5. Keep `amass(...)`, `prefix`, `outdir`, and force-constant filenames consistent through the whole chain.
6. Plot or summarize the result only after checking that the DFPT stages finished cleanly and that the interpolation settings are physically consistent.

## Checks That Matter

- Acoustic sum rule handling in `q2r.x` and `matdyn.x` should be explicit, usually `asr = 'crystal'`.
- The q-grid must be dense enough for the dispersion you want to trust.
- Imaginary modes near Gamma can be physical, but they can also come from loose SCF/phonon convergence, bad k/q meshes, or an unstable starting structure.
- For polar materials, interpret LO-TO splitting only if dielectric and Born-charge data were computed consistently.

## Related References

- `../references/qe-dfpt.md` for the standard `pw.x -> ph.x -> q2r.x -> matdyn.x` route
- `../references/qe-troubleshooting.md` for convergence and parsing failures
- `../references/scripts.md` for the shared phonon parsing and plotting CLIs
