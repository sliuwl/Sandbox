---
name: qe-troubleshooting-reference
description: Common Quantum ESPRESSO and Phonopy workflow failures in Sandbox, including symmetry, environment, path, and parsing issues.
---

# QE and Phonopy Troubleshooting

Use this reference when a QE or Phonopy workflow fails for symmetry, environment, parsing, or path reasons.

## Phonopy Interface Flag Changed

Problem:

- `phonopy --pwscf ...` no longer works

Fix:

- use `phonopy --qe ...`

## `spglib` Issue but Symmetry Is Required

Problem:

- Phonopy cannot use symmetry because `spglib` is missing or broken in the active environment

Fix:

- install `phonopy` and `spglib` into the same environment
- if the workflow uses the global conda base environment, keep both packages there
- verify with:

```bash
conda run -n base phonopy --version
conda run -n base python -c "import spglib; print(spglib.__version__)"
```

If `phonopy` runs but symmetry still looks wrong, the issue may be the structure rather than the package install.

## Phonopy Detects P1 or Generates Too Many Displacements

Likely causes:

- the relaxed structure is numerically noisy
- the structure was never re-symmetrized after relaxation
- the chosen cell is not the intended primitive or conventional setting

Fix:

1. extract the last structure from QE output
2. run `find_sym.py`
3. choose refined, conventional, or primitive output explicitly
4. test the symmetrized structure in QE with `nosym = .false.`
5. rerun Phonopy on the cleaned structure

If Phonopy suggests a better primitive setting, inspect whether `--pa auto` or a `PRIMITIVE_AXIS` setting is appropriate for the task.

## Displaced QE Inputs Fail to Run Correctly

Check:

- `nat` and `ntyp` in `head` match the generated supercell
- `pseudo_dir` points to the actual pseudopotential directory
- `outdir` is writable
- the job is launched from the directory those relative paths assume
- displaced calculations use `calculation = 'scf'`
- displaced calculations usually set `nosym = .true.`

## `phonopy --qe -f ...` Fails

Check:

- `phonopy_disp.yaml` is present in the working directory
- every displaced output file exists
- QE printed forces
- QE finished cleanly
- atom ordering in the outputs matches the original displaced inputs

## QE Output Exists but the Final Structure Is Hard to Extract

Do not copy the last coordinates manually. Use:

```bash
python3 ~/Sandbox/.sliu_skills/scripts/qe_out_to_vasp.py qe.out -o qe_last.vasp
```

The script already handles normal QE outputs and fallback parsing.

## Band Plot Does Not Match the Intended Brillouin Zone

Likely causes:

- the displacement calculation used a conventional cell but the band path assumes a primitive cell
- labels in `band.conf` do not match the actual path

Fix:

- inspect whether `PRIMITIVE_AXIS` is needed
- keep the path labels synchronized with the coordinates used in the file

## QE Loop Script Stops Early

Typical reasons:

- one input file is missing
- one output file is empty
- `JOB DONE` is missing because QE did not finish
- `tmp/` contents from a previous run contaminate the next run

Fix:

- check the first failing case, not the whole batch
- keep per-run cleanup of `tmp/`
- verify the launch directory and the MPI command line
