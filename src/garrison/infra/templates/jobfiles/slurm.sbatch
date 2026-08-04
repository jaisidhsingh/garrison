#!/bin/bash
#SBATCH --nodes={nodes}
#SBATCH --ntasks={ntasks}
#SBATCH --cpus-per-task={cpus_per_task}
#SBATCH --mem={mem}
#SBATCH --gres=gpu:{num_gpus}
#SBATCH --time={time}
#SBATCH --account={account}
#SBATCH --job-name={job_name}
#SBATCH --output={logs_folder}/out/job-%A_%a.out
#SBATCH --error={logs_folder}/err/job-%A_%a.err
#SBATCH --array=0-{job_subarray_size}
#SBATCH {additional_constraints}
# --exclude=i8009

CONFIG={config}
DP={num_gpus}

# executable needs to be a full path
bash {executable} "$CONFIG" "$SLURM_ARRAY_TASK_ID" "$SLURM_JOB_ID" "$DP"
