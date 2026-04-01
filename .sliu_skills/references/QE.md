# Quantum Espresso (QE) Reference

This file documents Quantum Espresso related tools and workflows in the skills system.

## Phonon Visualization Scripts

See [scripts.md](scripts.md) for detailed documentation on:

- `split_modes.py` — Split QE `dynmat.axsf` into separate XSF files for visualization
- `qe_out_to_vasp.py` — Extract final structure from QE output to VASP format
- `find_sym.py` — Analyze and symmetrize crystal structures

## Phonon Analysis Workflow

1. Run phonon calculation in QE (e.g., `ph.x`)
2. Post-process with `dynmat.x` to generate `dynmat.axsf`
3. Use `split_modes.py` to extract individual modes:

   ```bash
   python3 ~/Sandbox/.sliu_skills/scripts/split_modes.py dynmat.axsf
   ```

4. Visualize with VESTA or XCrysDen:

   ```bash
   xcrysden --xsf dynmat_mode06.xsf
   ```

## LO-TO Splitting Analysis

See [LO-TO-splitting-analysis.md](../LO-TO/LO-TO-splitting-analysis.md) for PbTiO₃ case study.

## Relevant Files

- Input: `dyn.in` — QE dynmat input
- Output: `dynmat.out` — phonon frequencies
- Output: `dynmat.axsf` — eigenvector animations
- Output: `dyn.out` — summary table with IR activities