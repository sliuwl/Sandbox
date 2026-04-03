#!/bin/bash
#SBATCH --job-name=CaF2_TiO2_vcrelax
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
mpirun -np $SLURM_NTASKS --map-by $MAP_OPT -mca coll_hcoll_enable 0 pw.x -i vc-relax.in -nk 4 > qe.out

exit