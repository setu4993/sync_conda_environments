from copy import copy
from json import loads
from pathlib import Path
from typing import List

from loguru import logger

from .process import run_subprocess

BASE_CONDA_ENV_COMMAND = ["conda", "env"]
_file_command = lambda x: ["-f", f"{x}"]


def _export_env(filename: Path, env_name: str) -> bytes:
    """
    Export a single environment to a file.

    Parameters
    ----------
    filename : Path
        Path to file where the environment should be stored.
    env_name : str
        Name of environment.

    Returns
    -------
    bytes
        Output from the export subprocess.
    """
    command = copy(BASE_CONDA_ENV_COMMAND)
    command.extend(["export", "-n", env_name])
    command.extend(_file_command(filename))
    return run_subprocess(command)


def _create_update_env(filename: Path, existing_envs: List[str]) -> bytes:
    """
    If the specified environment exists locally, update it, else, create it.

    Parameters
    ----------
    filename : Path
        Path to the conda environment file.
    existing_envs : List[str]
        List of existing environments.

    Returns
    -------
    bytes
        Output from the create / update subprocess
    """
    name = filename.stem
    command = copy(BASE_CONDA_ENV_COMMAND)
    if name in existing_envs:
        command.extend(["update"])
    else:
        command.extend(["create"])
    command.extend(_file_command(filename))
    return run_subprocess(command)


def export_envs(envs: List[str], output_path: Path) -> bool:
    """
    Given a list of environment names, export and dump them to the specificed directory.

    Parameters
    ----------
    envs : List[str]
        List of environment names.
    output_path : Path
        The directory where the environment files should be stored in.

    Returns
    -------
    Boolean
        Returns True if successful.
    """
    for env in envs:
        env_file = output_path.joinpath(f"{env}.yml")
        _export_env(filename=env_file, env_name=env)
        assert env_file.is_file(), f"Output file for env {env} not created."
        logger.info(f"Exported environment {env} to {env_file}.")
    return True


def create_update_envs(envs: List[str], env_files: List[Path]) -> bool:
    """
    Given a list of environemnts and environment files, create new or update existing environments.

    Parameters
    ----------
    envs : List[str]
        List of existing environments.
    env_files : List[Path]
        List of paths of environment files to load.

    Returns
    -------
    Boolean
        Returns True if successful.
    """
    for env_file in env_files:
        _create_update_env(filename=env_file, existing_envs=envs)
        logger.info(f"Created / updated environment {env_file.stem} from {env_file}.")
    return True


def list_envs() -> List[str]:
    """
    Return a list of conda environments' names.

    Returns
    -------
    List[str]
        List of conda environments.
    """
    logger.info(f"Listing conda environments...")
    command = copy(BASE_CONDA_ENV_COMMAND)
    command.extend(["list", "--json"])
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
