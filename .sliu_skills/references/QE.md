---
name: qe-reference
description: Index for Quantum ESPRESSO workflows in Sandbox. Route structure extraction and symmetry cleanup to `qe-structure.md`, Phonopy finite-displacement workflows to `qe-phonopy-fd.md`, DFPT phonons to `qe-dfpt.md`, and workflow failures to `qe-troubleshooting.md`.
---

# Quantum ESPRESSO Reference Index

This file is now the entry point for QE workflows in `~/Sandbox/.sliu_skills/references/`.

Load only the document that matches the task instead of reading one large mixed guide.

## Route by Task

- Extract the last structure from `qe.out`, clean up symmetry, or prepare a supercell:
  `qe-structure.md`
- Run finite-displacement phonons with Phonopy and QE:
  `qe-phonopy-fd.md`
- Run DFPT phonons with `ph.x`, `q2r.x`, and `matdyn.x`:
  `qe-dfpt.md`
- Diagnose symmetry, environment, path, or parsing failures:
  `qe-troubleshooting.md`
- Check CLI details for helper scripts:
  `scripts.md`

## Quick Reference

| Task | Main Tool | Main Reference |
|------|-----------|----------------|
| QE relaxation | `pw.x` | `qe-structure.md` |
| Extract final structure | `qe_out_to_vasp.py` | `qe-structure.md` |
| Symmetry analysis | `find_sym.py` | `qe-structure.md` |
| Finite-displacement phonons | `phonopy --qe` + `pw.x` | `qe-phonopy-fd.md` |
| DFPT Gamma phonons | `ph.x` | `qe-dfpt.md` |
| DFPT dispersion | `ph.x` + `q2r.x` + `matdyn.x` | `qe-dfpt.md` |
| Plot phonon bands | `plot_phonon.py` | `qe-dfpt.md` or `scripts.md` |
| Workflow failures | varies | `qe-troubleshooting.md` |

## Shared Script Entry Points

These scripts are documented in `scripts.md` and are reused across the split QE references:

- `qe_out_to_vasp.py`
- `find_sym.py`
- `make_supercell_struct.py`
- `generate_vcrelax.py`
- `generate_phonon_workflow.py`
- `parse_phonon.py`
- `plot_phonon.py`
- `split_modes.py`
