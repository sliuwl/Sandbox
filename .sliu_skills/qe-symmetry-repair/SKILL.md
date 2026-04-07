---
name: qe-symmetry-repair
description: "Use when a QE-relaxed structure or QE output has to be restored to a symmetry-consistent structure for further QE or phonopy work: extract the last structure, analyze the space group, write refined or conventional outputs, and rebuild QE-ready structure blocks or inputs."
---

# QE Symmetry Repair

`Repair` here means restoring a symmetry-consistent representation after relaxation noise, manual edits, or a low-symmetry intermediate. It does not mean file corruption repair.

## First Read

- Read `../references/qe-structure.md`.
- Use `../scripts/qe_out_to_vasp.py` to extract structures from QE outputs instead of copying coordinates manually.
- Use `../scripts/find_sym.py` to analyze symmetry and write symmetrized outputs.
- Open `../references/qe-troubleshooting.md` if symmetry detection fails or unexpectedly drops to P1.

## Core Workflow

1. Extract the last structure from `qe.out` with `qe_out_to_vasp.py`.
2. Analyze symmetry with `find_sym.py`.
3. Start with `refined` when the goal is to keep the same cell setting. Use `conventional` for reporting and supercell setup, and `primitive` for minimal-cell work.
4. Inspect the generated `.symmetry.txt`, `.vasp`, `.cif`, and `.struc.in` files.
5. Rebuild the QE input around the generated `.struc.in` when the user needs a QE-ready structure.
6. For phonopy or symmetry-enabled QE, test the symmetrized structure with `nosym = .false.` and iterate until QE no longer makes a meaningful ionic or cell move.

## Guardrails

- Do not symmetrize away a distortion that is physically intended.
- Record the chosen `symprec`, `angle_tolerance`, and structure kind when those settings matter.
- For phonopy workflows, the practical goal is a structure that QE and Phonopy classify consistently.

## Related References

- `../references/qe-phonopy-fd.md` for finite-displacement phonons
- `../references/qe-troubleshooting.md` for symmetry loss, P1 fallback, and environment issues
- `../references/scripts.md` for the shared script CLI details
