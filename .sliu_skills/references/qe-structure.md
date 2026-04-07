---
name: qe-structure-reference
description: Structure preparation, extraction, symmetry cleanup, and supercell preparation for Quantum ESPRESSO workflows in Sandbox.
---

# QE Structure Preparation and Symmetry Cleanup

Use this reference for `vc-relax`, extracting the last QE structure, checking symmetry, and preparing a clean structure for further QE or Phonopy work.

## Preferred Workflow

1. Run a full QE relaxation for the target structure.
2. Extract the last structure from the QE output with `qe_out_to_vasp.py`.
3. Analyze and symmetrize that structure with `find_sym.py`.
4. Rebuild the next QE input around the generated `.struc.in`.
5. For symmetry-sensitive work, test the symmetrized structure with `nosym = .false.` and keep iterating until QE makes no meaningful ionic or cell update.

That final state is the practical meaning of symmetry `repair` in this workspace: restore a structure that is both DFT-relaxed and numerically consistent with the symmetry you want Phonopy or QE to use.

## Structure Optimization Notes

For the first unconstrained optimization, it is acceptable to relax with symmetry disabled if the structure is far from equilibrium. A common QE pattern is:

```text
&CONTROL
  calculation    = 'vc-relax'
  tstress        = .true.
  tprnfor        = .true.
/

&SYSTEM
  ibrav          = 0
  nosym          = .true.
/
```

After the structure is relaxed, the recommended follow-up is:

1. Extract the last structure.
2. Symmetrize it.
3. Run QE again with `nosym = .false.`.
4. Repeat until the symmetry-clean structure is effectively accepted in one step.

That is the preferred starting point for phonons.

## Extract the Last Structure

Always prefer the script over manual copy/paste:

```bash
python3 ~/Sandbox/.sliu_skills/scripts/qe_out_to_vasp.py qe.out -o qe_last.vasp
```

Useful variants:

```bash
python3 ~/Sandbox/.sliu_skills/scripts/qe_out_to_vasp.py qe.out --both
python3 ~/Sandbox/.sliu_skills/scripts/qe_out_to_vasp.py qe.out -o qe_last.cif -f cif
```

Why use the script:

- it handles standard QE outputs directly
- it falls back to the last `CELL_PARAMETERS` and `ATOMIC_POSITIONS` block when needed
- it preserves species ordering correctly when writing VASP output

## Analyze and Symmetrize

Run:

```bash
python3 ~/Sandbox/.sliu_skills/scripts/find_sym.py qe_last.vasp -k refined
```

Generated files include:

- `*_symmetrized_<kind>_sgNNN_<symbol>.vasp`
- `*_symmetrized_<kind>_sgNNN_<symbol>.cif`
- `*_symmetrized_<kind>_sgNNN_<symbol>.struc.in`
- `*_symmetrized_<kind>_sgNNN_<symbol>.symmetry.txt`

### Which structure kind to use

- `refined`: best default when you want to stay close to the existing cell setting
- `conventional`: best for reporting, comparing to standard settings, and building supercells
- `primitive`: best when you need the smallest symmetry-standard cell

Useful options:

```bash
python3 ~/Sandbox/.sliu_skills/scripts/find_sym.py qe_last.vasp -k conventional
python3 ~/Sandbox/.sliu_skills/scripts/find_sym.py qe_last.vasp -k primitive -s 0.01
python3 ~/Sandbox/.sliu_skills/scripts/find_sym.py qe_last.vasp --qe-coordinates angstrom
```

## Rebuild QE Inputs

Once the `.struc.in` file looks correct, use it as the structural block for the next QE input.

If you need a fresh relaxation template, reuse:

```bash
python3 ~/Sandbox/.sliu_skills/scripts/generate_vcrelax.py --help
```

The shared script is useful for consistent QE headers, but the structural block should come from the extracted or symmetrized structure that you actually intend to run.

## Build Repeated Supercells

When you already have a cleaned VASP structure and need a repeated cell plus a QE-ready structure block:

```bash
python3 ~/Sandbox/.sliu_skills/scripts/make_supercell_struct.py qe_last.vasp -r 2 2 1
```

Outputs:

- repeated VASP structure
- QE-style `struct.in`

## Guardrails

- Do not manually copy the final coordinates out of QE if the script can read the file.
- Do not force symmetry onto a structure when the distortion is the physics of interest.
- If Phonopy still detects P1 after symmetrization, treat that as a workflow problem and check the troubleshooting reference rather than assuming the script is wrong.
