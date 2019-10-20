from os.path import join, splitext, basename, isfile
from typing import List
import json
import logging

from .process import run_command

BASE_CONDA_ENV_COMMAND = ['conda', 'env']


def _export_env(filename: str) -> str:
    command = BASE_CONDA_ENV_COMMAND
    command += ['export']
    command += _file_command(filename)
    return run_command(command)


_file_command = lambda x: ['-f', f'{x}']


def _create_update_env(filename: str, existing_envs: List[str]) -> str:
    name, _ = splitext(basename(filename))
    command = BASE_CONDA_ENV_COMMAND
    if name in existing_envs:
        command += ['update']
    else:
        command += ['create']
    command += _file_command(filename)
    return run_command(command)


def export_envs(envs: List[str], output_path: str):
    for env in envs:
        env_file = join(output_path, env) + '.yml'
        _export_env(filename=env_file)
        assert isfile(env_file), f"Output file for env {env} not created."
        logging.info(f'Exported file {env_file} for env named {env}.')


def create_update_envs(envs: List[str], env_files: List[str]):
    for env_file in env_files:
        _create_update_env(filename=env_file, existing_envs=envs)


def list_envs() -> List[str]:
    command = BASE_CONDA_ENV_COMMAND
    command += ['list', '--json']
    proc_output = run_command(command)
    proc_json = json.loads(proc_output)
    env_locations = proc_json['envs']
    environments = []
    for env_location in env_locations:
        name = basename(env_location)
        if name.startswith('miniconda') or name.startswith('anaconda'):
            name = 'base'
        environments.append(name)
    return environments
