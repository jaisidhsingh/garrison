from dataclasses import dataclass


@dataclass(kw_only=True)
class BaseConfig:
    executable: str
    config: str
    num_gpus: int
    job_subarray_size: int
    logs_folder: str
    additional_constraints: str
    backend: str | None


@dataclass(kw_only=True)
class CondorConfig(BaseConfig):
    bid: int
    memory: str
    num_cpus: int
    additional_constraints: str = """(TARGET.CUDADeviceName == "NVIDIA A100-SXM4-80GB" || TARGET.CUDADeviceName == "NVIDIA H100 80GB HBM3" || TARGET.CUDADeviceName == "NVIDIA H100") && (Machine != "g174.internal.cluster.is.localnet")"""
    backend: str = "condor"


@dataclass(kw_only=True)
class SlurmConfig(BaseConfig):
    mem: str
    nodes: int
    ntasks: int
    cpus_per_task: int
    account: str
    job_name: str
    additional_constraints: str = """--exclude=i8009"""
    backend: str = "slurm"


DISPATCH_BACKEND_CONFIG_MAP = {"condor": CondorConfig, "slurm": SlurmConfig}
