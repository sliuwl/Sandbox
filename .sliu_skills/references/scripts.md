# Scripts Reference

This file documents the Python scripts stored in `~/Sandbox/.sliu_skills/scripts`.

For workflow routing, start with:

- `QE.md` for the top-level QE index
- `qe-bands.md` for QE band structures
- `qe-structure.md` for extraction and symmetry cleanup
- `qe-phonopy-fd.md` for Phonopy finite-displacement workflows
- `qe-dfpt.md` for `ph.x/q2r.x/matdyn.x`
- `qe-troubleshooting.md` for failures and fixes

## Workflow: Analyzing QE Optimized Structures

> **IMPORTANT**: When analyzing optimized structures from QE output files, always use these scripts in sequence.

### Prerequisites
```bash
pip3 install ase pymatgen
```

### Step 1: Extract VASP file from QE output

### Step 1: Extract VASP file from QE output
```bash
python3 ~/Sandbox/.sliu_skills/scripts/qe_out_to_vasp.py QE_OUTPUT -o output.vasp
```

### Step 2: Analyze symmetry
```bash
python3 ~/Sandbox/.sliu_skills/scripts/find_sym.py output.vasp -k conventional
```

This workflow automatically generates:
- VASP file (for visualization)
- CIF file (for detailed lattice parameters)
- QE structure file (`.struc.in`)
- Symmetry report (`.symmetry.txt`)

**Why use scripts?** Manual extraction misses symmetry analysis and proper format conversion.

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

## `qe_plot_bands.py`

Purpose:
- Read a QE `bands` output file produced by `pw.x`.
- Reconstruct the cumulative k-path and special-point boundaries.
- Export raw band data and save band-structure figures.

Dependencies:
- `numpy`
- `matplotlib`

Basic usage:

```bash
python3 ~/Sandbox/.sliu_skills/scripts/qe_plot_bands.py -o bands.out
```

Important arguments:
- `-o`, `--output`: QE output from `pw.x` with `calculation = 'bands'`.
- `-k`, `--klabels`: text file with one special-point label per boundary.
- `-n`, `--name`: tag appended to output filenames. Default: `pbe`.
- `-r`, `--raw`: export raw band data in addition to figures.
- `--no-plot`: skip figure generation and only parse or export data.
- `-s`, `--nspin`: one of `1`, `2`, `4`. Default: `1`.
- `-ne NUP NDN`: up/down electron counts when `nspin = 2`.
- `-e EMIN EMAX ESTEP`: energy window relative to the chosen Fermi reference.
- `-fe`: Fermi reference mode.

Fermi modes:
- `-fe 1`: use `(VBM + CBM) / 2`
- `-fe 2`: use `VBM`
- `-fe 3 VALUE`: use an explicit Fermi energy in eV

Generated files:
- `<bands.out>_<name>.png`
- `<bands.out>_<name>.eps`
- `<name>_bands.dat` when `-r` and `nspin = 1/4`
- `<name>_bands_up.dat` and `<name>_bands_dn.dat` when `-r` and `nspin = 2`
- `xklabel.dat` when `-r`

Notes:
- The raw data files are written next to the parsed QE output file.
- The script warns if the number of labels in `klabel` does not match the number of detected special-point boundaries.

Examples:

```bash
python3 ~/Sandbox/.sliu_skills/scripts/qe_plot_bands.py -o ./bands.out -k ./klabel -e 4 4 2 -n pbe -fe 1 -r
python3 ~/Sandbox/.sliu_skills/scripts/qe_plot_bands.py -o ./bands.out -k ./klabel --no-plot -r
```

## `make_supercell_struct.py`

Purpose:
- Read a VASP-format structure file.
- Create a repeated supercell with ASE.
- Export both a VASP file and a QE-compatible `struct.in`.

Dependencies:
- `ase`
- `numpy`

Basic usage:

```bash
python3 ~/Sandbox/.sliu_skills/scripts/make_supercell_struct.py INPUT_VASP -r NX NY NZ
```

Arguments:
- `input_vasp`: input VASP structure file such as `qe.vasp`.
- `-r`, `--repeat`: repetition along `a`, `b`, `c`. Default: `1 1 2`.
- `-o`, `--output`: output VASP filename. If omitted, uses `<input_stem>_<NX>x<NY>x<NZ>.vasp`.
- `--struct-output`: QE structure output filename. Default: `struct.in`.

Behavior:
- Reads the structure with ASE and creates the supercell with `atoms.repeat((NX, NY, NZ))`.
- Wraps atomic positions back into the cell.
- Preserves the original species ordering from the input file.
- Writes a QE structure block with `CELL_PARAMETERS (angstrom)` and `ATOMIC_POSITIONS (crystal)`.

Examples:

```bash
python3 ~/Sandbox/.sliu_skills/scripts/make_supercell_struct.py ./qe.vasp -r 1 1 2
python3 ~/Sandbox/.sliu_skills/scripts/make_supercell_struct.py ./qe.vasp -r 2 2 1 -o ./qe_2x2x1.vasp --struct-output ./struct_2x2x1.in
```

## `split_modes.py`

Purpose:
- Split a Quantum ESpresso `dynmat.axsf` file into separate XSF files, one for each phonon mode.
- Facilitates visualization of individual phonon eigenvectors using VESTA or XCrysDen.

Dependencies:
- Standard library only (no external dependencies)

Basic usage:

```bash
python3 ~/Sandbox/.sliu_skills/scripts/split_modes.py input.axsf [output_prefix]
```

Arguments:
- `input.axsf`: path to the AXSF file from QE phonon calculation (e.g., `dynmat.axsf`).
- `output_prefix`: (optional) prefix for output filenames. If omitted, uses the input filename stem.

Output:
- Generates separate `.xsf` files named `<prefix>_modeNN.xsf` where NN is the mode number (01-15).
- Each file contains a single phonon mode in standard XSF format (suitable for VESTA).

Behavior:
- Parses the AXSF file generated by QE's `dynmat` post-processing tool.
- Outputs single-structure XSF files (not animation format) for compatibility with VESTA.
- The displacement vectors in each file can be visualized using XCrysDen (`--xsf`) or VESTA.

Examples:

```bash
# Split dynmat.axsf in the current directory
python3 ~/Sandbox/.sliu_skills/scripts/split_modes.py ./dynmat.axsf

# Split and use custom prefix
python3 ~/Sandbox/.sliu_skills/scripts/split_modes.py ../000/dynmat.axsf pto_modes

# Then visualize a specific mode
xcrysden --xsf pto_modes_mode06.xsf
vesta pto_modes_mode06.xsf
```

Notes:
- Phonon mode 1-3 are typically acoustic modes (zero frequency).
- Mode 6 (152.9 cm⁻¹ in PbTiO₃) is the z-polarized E(1) soft mode.
- The XSF files use atomic displacements as displacement vectors for visualization.
