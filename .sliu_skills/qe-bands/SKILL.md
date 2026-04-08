---
name: qe-bands
description: Use when work in Sandbox needs a Quantum ESPRESSO band-structure workflow, including reviewing or creating `scf.in` and `bands.in`, choosing a high-symmetry k-path, explaining `K_POINTS {crystal_b}`, checking `klabel`, parsing `bands.out`, or plotting and interpreting QE band structures.
---

# QE Bands

Use this skill for the standard QE band-structure workflow driven by `pw.x` with `calculation = 'bands'`.

## First Read

- Read `../references/qe-bands.md`.
- If the band path should be generated from a nearly symmetric relaxed structure, also read `../references/qe-structure.md`.
- Use `../scripts/qe_plot_bands.py` as the shared plotting entry point instead of relying on example-local scripts.
- Open `../references/qe-troubleshooting.md` if the path, labels, parser, or Python environment fail.

## Core Workflow

1. Confirm that a converged SCF run already exists and that `prefix`, `outdir`, structure, and pseudopotentials are the same in `scf.in` and `bands.in`.
2. For the band-path run, use `calculation = 'bands'`, keep the same `prefix/outdir`, and usually set `nosym = .true.` so QE follows the explicit path instead of reducing it by symmetry.
3. Build or validate `K_POINTS {crystal_b}` carefully. The fourth number is the number of interpolated points to the next vertex, and `0` is how path discontinuities such as `Z|X` are encoded.
4. Keep `klabel` aligned with the special-point boundaries in the actual path, not just with the list of input vertices.
5. Run the `bands` calculation, check `JOB DONE`, confirm the expected number of k-points and bands, then plot with `qe_plot_bands.py`.
6. Choose the Fermi reference intentionally: midpoint of VBM/CBM, VBM, or a user-supplied value.

## Checks That Matter

- `nbnd` must be large enough to include the conduction bands of interest.
- The path should come from the symmetry you actually want to present. If the relaxed structure is numerically distorted, generate the path from a symmetrized structure first.
- `klabel` must match the number of high-symmetry boundaries detected by the plotting workflow.
- If the user needs projected bands, SOC-specific analysis, or `bands.x` post-processing, route that as follow-on work rather than forcing it into this first-pass skill.

## Related References

- `../references/qe-bands.md` for the workflow, k-path setup options, and plotting commands
- `../references/qe-structure.md` for extracting or symmetrizing the structure before building a path
- `../references/scripts.md` for the shared plotting CLI details
