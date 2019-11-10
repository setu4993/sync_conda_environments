from pathlib import Path
from typing import List

from ..helpers.conda import *


def test_list_envs():
    envs = list_envs()
    assert isinstance(envs, List)
    assert len(envs) >= 0


def test_export_envs():
    envs = ["base"]
    output_path = Path(".")
    result = export_envs(envs, output_path)
    assert result


def test_create_update_envs():
    envs = ["base"]
    env_files = [Path(".").joinpath("base.yml")]
    result = create_update_envs(envs, env_files)
    assert result
