---
name: check-gpu-status
description: Check SLURM job status and submit QE jobs to remote GPU clusters (gpu/sai)
trigger: check job status, check gpu status, check sai status, check slurm, gpu jobs, sai jobs, job status, submit gpu job, submit sai job
---

# Check GPU Cluster Job Status & Submit Jobs

SSH to remote GPU clusters (gpu or sai) and manage SLURM jobs.

## Usage

**Check job status on specific server:**
```bash
ssh gpu "squeue -u $USER"
ssh sai "squeue -u $USER"
```

**Check specific job:**
```bash
ssh gpu "squeue -j <JOB_ID>"
ssh sai "squeue -j <JOB_ID>"
```

## Submit Jobs to GPU Cluster

### Step 1: Create project folder locally

```
ProjectName/
├── vc-relax.in
├── gpu_qe.sbatch         # For gpu server
├── gpu_qe_sai.sbatch     # For sai server
└── psps/
    ├── *.UPF
    └── *.UPF
```

### Step 2: Copy files to remote (IMPORTANT: copy each file separately)

```bash
# For gpu server
ssh gpu "mkdir -p ProjectName/psps"
scp ProjectName/vc-relax.in gpu:~/ProjectName/
scp ProjectName/gpu_qe.sbatch gpu:~/ProjectName/
scp ProjectName/psps/* gpu:~/ProjectName/psps/
```

```bash
# For sai server
ssh sai "mkdir -p ProjectName/psps"
scp ProjectName/vc-relax.in sai:~/ProjectName/
scp ProjectName/gpu_qe_sai.sbatch sai:~/ProjectName/
scp ProjectName/psps/*.UPF sai:~/ProjectName/psps/
```

**Note:** Always copy `.UPF` files explicitly with `psps/*.UPF` pattern to ensure all pseudopotential files are transferred.

### Step 3: Submit job

```bash
# For gpu server
ssh gpu "cd ProjectName && mkdir -p tmp/ && sbatch gpu_qe.sbatch"

# For sai server
ssh sai "cd ProjectName && mkdir -p tmp/ && sbatch gpu_qe_sai.sbatch"
```

### Step 4: Monitor

```bash
ssh gpu "squeue -j <JOB_ID>"
ssh sai "squeue -j <JOB_ID>"
```

## Batch Script Templates

### For gpu server (8V100)

```bash
#!/bin/bash
#SBATCH --job-name=ProjectName
#SBATCH --partition=8V100
#SBATCH --nodes=1
#SBATCH --ntasks=4
#SBATCH --gpus-per-node=4
#SBATCH --qos=rush-gpu

source /etc/profile
source ~/.bashrc 2>/dev/null || true

source /opt/sai_config/mps_mapping.d/${SLURM_JOB_PARTITION}.bash 2>/dev/null || true

nvidia-smi dmon -s pucvmte -o T > nvdmon_job-$SLURM_JOB_ID.log &
module load qe/7.3-nvhpc24.3-ompi5.0.8-auto
mpirun -np $SLURM_NTASKS --map-by $MAP_OPT -mca coll_hcoll_enable 0 pw.x -i vc-relax.in -nk 4  >& qe.out

exit
```

### For sai server (4V100)

```bash
#!/bin/bash
#SBATCH --job-name=ProjectName
#SBATCH --partition=4V100
#SBATCH --nodes=1
#SBATCH --ntasks=4
#SBATCH --gpus-per-node=4
#SBATCH --qos=rush-gpu

source /etc/profile
source ~/.bashrc 2>/dev/null || true

source /opt/sai_config/mps_mapping.d/${SLURM_JOB_PARTITION}.bash 2>/dev/null || true

nvidia-smi dmon -s pucvmte -o T > nvdmon_job-$SLURM_JOB_ID.log &
module load qe/7.3-nvhpc24.3-ompi5.0.8
mpirun -np $SLURM_NTASKS --map-by $MAP_OPT -mca coll_hcoll_enable 0 pw.x -i vc-relax.in -nk 4  >& qe.out

exit
```

**Key Differences between gpu and sai:**

| Setting | gpu | sai |
|---------|-----|-----|
| Partition | 8V100 | 4V100 |
| Module | qe/7.3-nvhpc24.3-ompi5.0.8-auto | qe/7.3-nvhpc24.3-ompi5.0.8 |
| Script name | gpu_qe.sbatch | gpu_qe_sai.sbatch |

## Important: Environment Sourcing

The GPU cluster requires sourcing the environment before running modules. Always include these lines:

```bash
source /etc/profile
source ~/.bashrc 2>/dev/null || true
```

**Without this, the job will fail with:**
- `module: command not found`
- `mpirun: command not found`

## Common SLURM States

| State | Meaning |
|-------|---------|
| RUNNING (R) | Job is currently executing |
| PD | Pending (waiting for resources) |
| COMPLETED | Job finished successfully |
| FAILED | Job failed |
| TIMEOUT | Job reached time limit |
| CANCELLED | Job was cancelled |

## Check Job Output

```bash
# View output file
ssh gpu "cat ProjectName/qe.out"
ssh sai "cat ProjectName/qe.out"

# View last 50 lines (real-time)
ssh gpu "tail -f ProjectName/qe.out"
ssh sai "tail -f ProjectName/qe.out"

# Check error output
ssh gpu "cat ProjectName/slurm-<JOB_ID>.out"
ssh sai "cat ProjectName/slurm-<JOB_ID>.out"
```

## Detailed Job Info

```bash
ssh gpu "scontrol show job <JOB_ID>"
ssh sai "scontrol show job <JOB_ID>"
```