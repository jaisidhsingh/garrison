# Executable needs to be a full path
executable={executable}

# Experiment config
config={config}
job_subarray_size={job_subarray_size}
dp={num_gpus}
LOGS_DIR={logs_folder}

# Pass arguments to the executable
arguments = $(config) $(Process) $(Cluster) $(dp)

# Logging
error = $(LOGS_DIR)/err/job.$(Cluster).$(Process).err
output = $(LOGS_DIR)/out/job.$(Cluster).$(Process).out
log = $(LOGS_DIR)/log/job.$(Cluster).$(Process).log

# Job requirements
request_memory = {memory}
request_cpus = {num_cpus}
request_gpus = {num_gpus}
requirements = {additional_constraints}

queue $(job_subarray_size)
