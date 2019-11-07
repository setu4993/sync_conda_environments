import logging
from copy import copy
from json import loads
from pathlib import Path
from typing import Generator, List

from .process import run_subprocess

BASE_CONDA_ENV_COMMAND = ["conda", "env"]


def _export_env(filename: Path, env_name: str) -> bytes:
    command = copy(BASE_CONDA_ENV_COMMAND)
    command += ["export", "-n", env_name]
    command += _file_command(filename)
    return run_subprocess(command)


_file_command = lambda x: ["-f", f"{x}"]


def _create_update_env(filename: Path, existing_envs: List[str]) -> bytes:
    name = filename.stem
    command = copy(BASE_CONDA_ENV_COMMAND)
    if name in existing_envs:
        command += ["update"]
    else:
        command += ["create"]
    command += _file_command(filename)
    return run_subprocess(command)


def export_envs(envs: List[str], output_path: Path):
    for env in envs:
        env_file = output_path.joinpath(f"{env}.yml")
        _export_env(filename=env_file, env_name=env)
        assert env_file.is_file(), f"Output file for env {env} not created."
        logging.info(f"Exported file {env_file} for env named {env}.")


def create_update_envs(envs: List[str], env_files: Generator[Path, None, None]):
    for env_file in env_files:
        _create_update_env(filename=env_file, existing_envs=envs)


def list_envs() -> List[str]:
    command = copy(BASE_CONDA_ENV_COMMAND)
    command += ["list", "--json"]
    proc_output = run_subprocess(command)
    proc_json = loads(proc_output)
    env_locations = proc_json["envs"]
    environments = []
    for env_location in env_locations:
        name = Path(env_location).stem
        if name.startswith("miniconda") or name.startswith("anaconda"):
            name = "base"
        environments.append(name)
    return environments
