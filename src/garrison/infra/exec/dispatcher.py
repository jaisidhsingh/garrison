import os
from pathlib import Path
import typing as tp
import subprocess

from infra.exec.config import BaseConfig

SUPPORTED_DISPATCH_BACKENDS = ["condor", "slurm"]


class Dispatcher:
    def __init__(self, config: BaseConfig, **kwargs):
        tmp_config = config
        for k, v in kwargs:
          tmp_config.__setattr__(k, v)

        assert tmp_config.backend is not None, "Found Dispatcher.config.backend = None. Please provide the dispatcher backend for your job submission."
        assert tmp_config.backend is in SUPPORTED_DISPATCH_BACKENDS, f"Found unsupported backend. Please use a backend in {SUPPORTED_DISPATCH_BACKENDS}."

        self.config = tmp_config
        self.backend = self.config.backend

    def prepare_submission(self):
        template_ext = "sh" if self.backend == "condor" else "sbatch"
        template_filename = self.backend + "." + template_ext
        template_path = Path.cwd() / "templates" / "jobfiles" / template_filename

        with open(template_path) as f:
            content = f.read()
            set_content = content.format(**vars(self.config))

        tempfile_path = self.config.config.replace(".yaml", template_ext)
        with open(tempfile_path, "w") as f:
            f.write(set_content)

        return tempfile_path

    def dispatch(self):
        jobfile = self.prepare_submission()

        if self.backend == "condor":
            cmdlist = ["condor_submit_bid", self.config.bid, jobfile]
        elif self.backend == "slurm":
            cmdlist = ["sbatch", jobfile]
        else:
            raise NotImplementedError(f"Dispatcher backend {self.backend} is not implemented.")

        result = subprocess.run(cmdlist, capture_output=True, text=True)
        if result.returncode == 0:
            print(results.stdout)
            print(f"Submitted experiment batch job from config {self.config.config}")
            os.remove(jobfile)
        else:
            raise Exception(f"Failed to submit experiment batch job. Error: {result.stderr}")
