# Scripts Reference

This file documents the Python scripts stored in `~/Sandbox/.sliu_skills/scripts`.

## `find_sym.py`

Purpose:
- Read a POSCAR-format structure file.
- Analyze symmetry with `pymatgen`.
- Write symmetrized structure outputs for VASP, CIF, and Quantum ESPRESSO.

Dependencies:
- `pymatgen`

Basic usage:

```bash
python3 ~/Sandbox/.sliu_skills/scripts/find_sym.py INPUT_FILE
```

Arguments:
- `input_file`: path to a POSCAR-format structure file. The filename can be arbitrary as long as the content is POSCAR/CONTCAR style.
- `-s`, `--symprec`: symmetry distance tolerance. Default: `0.005`.
- `-a`, `--angle-tolerance`: angle tolerance in degrees. Default: `5.0`.
- `-k`, `--structure-kind`: one of `conventional`, `refined`, `primitive`. Default: `conventional`.
- `-o`, `--output-dir`: output directory. Default: the input file directory.
- `-p`, `--prefix`: custom output filename prefix. Default: input filename stem.
- `--qe-coordinates`: QE coordinate style, `crystal` or `angstrom`. Default: `crystal`.
- `--skip-cif`: do not write the CIF file.
- `--skip-report`: do not write the symmetry report text file.

Generated files:
- `*_symmetrized_<structure_kind>_sgNNN_<space-group>.vasp`
- `*_symmetrized_<structure_kind>_sgNNN_<space-group>.cif` unless `--skip-cif` is used
- `*_symmetrized_<structure_kind>_sgNNN_<space-group>.struc.in`
- `*_symmetrized_<structure_kind>_sgNNN_<space-group>.symmetry.txt` unless `--skip-report` is used

Notes:
- The script prints a symmetry summary to the terminal even when the report file is skipped.
- Output filenames include the detected space-group number and symbol.

Examples:

```bash
python3 ~/Sandbox/.sliu_skills/scripts/find_sym.py ./POSCAR
python3 ~/Sandbox/.sliu_skills/scripts/find_sym.py ./qe.vasp -k primitive -o ./symmetry
python3 ~/Sandbox/.sliu_skills/scripts/find_sym.py ./CONTCAR --qe-coordinates angstrom --skip-cif
```

## `qe_out_to_vasp.py`

Purpose:
- Read the last structure from a Quantum ESPRESSO output file.
- Export that structure as a VASP-format `.vasp` file.

Dependencies:
- `ase`

Basic usage:

```bash
python3 ~/Sandbox/.sliu_skills/scripts/qe_out_to_vasp.py QE_OUTPUT
```

Arguments:
- `qe_output`: path to a Quantum ESPRESSO output file such as `qe.out`.
- `-o`, `--output`: output filename. If omitted, the script uses the input basename with a `.vasp` suffix.

Behavior:
- The script reads the last image from the QE output (`index=-1`), which is typically the final relaxed structure.
- Atomic positions are wrapped before writing.
- If the output filename does not end with `.vasp`, the script changes the suffix to `.vasp`.

Examples:

```bash
python3 ~/Sandbox/.sliu_skills/scripts/qe_out_to_vasp.py ./qe.out
python3 ~/Sandbox/.sliu_skills/scripts/qe_out_to_vasp.py ./relax.out -o ./final_structure.vasp
```
