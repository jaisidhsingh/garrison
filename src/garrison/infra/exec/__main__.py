import argparse

import yaml

from infra.exec.config import DISPATCH_BACKEND_CONFIG_MAP
from infra.exec.dispatcher import Dispatcher


def setup_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--config",
        required=True,
        help="Path of the yaml config that drives the experiment",
    )
    return parser.parse_args()


def extract_submission_params(config_path: str):
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)

    exec_params = config.pop("exec")
    exec_params["config"] = config_path.replace(".yaml", "_temp.yaml")

    with open(exec_params["config"], "w") as f:
        yaml.safe_dump(f, config)

    dispatch_config_ref = DISPATCH_BACKEND_CONFIG_MAP.get(exec_params["backend"], None)
    assert dispatch_config_ref is not None, (
        f"Dispatcher backend {exec_params['backend']} is not implemented."
    )
    dispatch_config = dispatch_config_ref(**exec_params)

    return dispatch_config


if __name__ == "__main__":
    args = setup_args()
    dispatch_config = extract_submission_params(args.config)
    dispatcher = Dispatcher(dispatch_config)
    dispatcher.submit()
