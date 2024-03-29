from pathlib import Path
from typing import List

from sync_conda_environments.helpers.conda import (
    create_update_envs,
    export_envs,
    list_envs,
)


def test_list_envs():
    envs = list_envs()
    assert isinstance(envs, List)
    assert len(envs) >= 0


def test_export_envs(tmp_path):
    envs = ["base"]
    result = export_envs(envs, tmp_path)
    assert result


def test_create_update_envs(tmp_path):
    envs = ["base"]
    # Setup
    export_envs(envs, tmp_path)
    # Test
    env_files = [tmp_path.joinpath("base.yml")]
    result = create_update_envs(envs, env_files)
    assert result
