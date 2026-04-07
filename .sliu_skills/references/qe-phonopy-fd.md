---
name: qe-phonopy-fd-reference
description: Phonopy finite-displacement workflows using Quantum ESPRESSO supercell force calculations in Sandbox.
---

# QE Phonopy Finite-Displacement Workflow

Use this reference for phonon spectra obtained from Phonopy finite displacements and QE SCF force calculations.

This is distinct from the DFPT `ph.x/q2r.x/matdyn.x` workflow. If the user asks for finite-displacement phonons, read this file first.

## Required Files

- reference QE input such as `M.in`
- `phonopy`
- `pw.x`
- QE pseudopotentials
- printed forces in QE outputs

Optional:

- `BORN` for non-analytic corrections in polar materials

## Step 1: Prepare the Reference Structure

The best starting point is:

1. fully optimized
2. symmetrized to the target space group
3. accepted by QE with `nosym = .false.` without a meaningful further relaxation step

That state minimizes false symmetry breaking and keeps the number of displaced supercells small.

If the relaxed structure is noisy or falls to P1, first use the structure cleanup workflow from `qe-structure.md`.

## Step 2: Generate Displaced Supercells

Run Phonopy with the QE interface:

```bash
phonopy --qe -d --dim="2 2 2" -c M.in -v
```

Important:

- use `--qe`, not the removed `--pwscf`
- `-d` generates finite displacements
- `--dim` sets the supercell
- `-c M.in` points to the reference QE input

Typical outputs:

- `phonopy_disp.yaml`
- `supercell.in`
- `supercell-001.in`, `supercell-002.in`, ...

The number of displaced files depends on symmetry. A good symmetry-clean structure can reduce the workload dramatically.

## Step 3: Build QE SCF Inputs for Each Displacement

Phonopy’s `supercell-XXX.in` files contain structure data only. They are not complete QE inputs.

Create a `head` file containing the non-structural QE settings:

- `calculation = 'scf'`
- `tprnfor = .true.`
- `tstress = .true.`
- correct `nat` and `ntyp` for the supercell
- `nosym = .true.` for the displaced calculations
- suitable `K_POINTS`, often `Gamma` for large supercells

Then concatenate `head` with every displaced supercell file. In this workspace the usual helper is a local `scan.bash` script.

The result should be a set of full QE inputs such as:

- `QE/QE001.in`
- `QE/QE002.in`
- `QE/QE003.in`

## Step 4: Run the Displaced QE Calculations

Run one SCF calculation per displaced supercell.

Rules:

- do not relax the displaced structures
- keep atom ordering unchanged
- produce one output file per displaced input
- make sure forces are printed

If the project uses relative paths like `pseudo_dir = './psps'` and `outdir = './tmp'`, launch the loop from the directory those paths are written for, not from a nested folder that breaks them.

## Step 5: Build `FORCE_SETS`

After all displaced SCF jobs finish:

```bash
phonopy --qe -f QE/QE*.out
```

Phonopy reads:

- `phonopy_disp.yaml`
- the forces from the QE outputs

and writes:

- `FORCE_SETS`

This step fails if outputs are missing, forces were not printed, or the atom order changed.

## Step 6: Phonon Bands and NAC

For the band structure:

```bash
phonopy --qe -c M.in -p band.conf
```

For polar materials with a valid `BORN` file:

```bash
phonopy --qe --nac -c M.in -p band.conf
```

Typical `band.conf` responsibilities:

- `DIM = ...` consistent with the displacement supercell
- band path
- labels
- optional `PRIMITIVE_AXIS`

Use `PRIMITIVE_AXIS` when the displacement calculation was built from a conventional cell but you want the band plot in the primitive Brillouin zone.

## Workspace Conventions

- Reuse the project-local `head` and `scan.bash` when they already exist.
- Reuse existing loop scripts such as `gpu_qe_loop.sbatch` patterns when the user asks for batch execution.
- Prefer materialized scripts over large one-off shell loops.

## Common Failure Modes

- Phonopy falls to P1 and generates too many displacements.
- `spglib` is unavailable in the Phonopy environment.
- `nat` or `ntyp` in `head` does not match the generated supercell.
- QE outputs cannot be parsed because the run did not finish or forces were missing.
- The QE loop was launched from the wrong directory for the chosen `pseudo_dir` or `outdir`.

See `qe-troubleshooting.md` for fixes.
