# QE Supercell Generator

Generate VASP POSCAR supercells and QE structure blocks from a base POSCAR/VASP file.

## Script

Use:
`/Users/sliutheory/Sandbox/.sliu_skills/scripts/qe_supercell.py`

## Requirements

- Input POSCAR must be VASP 5 format (species line present).
- Coordinates must be `Direct`.
- Optional QE template must contain the `__STRUCTURE__` placeholder.

## Commands

2x2x1 supercell:

```bash
python3 /Users/sliutheory/Sandbox/.sliu_skills/scripts/qe_supercell.py \
  --input /path/to/qe.vasp \
  --supercell 2 2 1 \
  --out-dir /path/to/output
```

1x1x2 supercell with vc-relax template:

```bash
python3 /Users/sliutheory/Sandbox/.sliu_skills/scripts/qe_supercell.py \
  --input /path/to/qe.vasp \
  --supercell 1 1 2 \
  --out-dir /path/to/output \
  --vc-relax-template /path/to/vc-relax.in-t
```

## Template Format

Your template must include `__STRUCTURE__`, which gets replaced by:

```
CELL_PARAMETERS (angstrom)
...

ATOMIC_POSITIONS (crystal)
...
```
