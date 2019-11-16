from pathlib import Path
from typing import List

from ..helpers.file import glob_env_files


def test_list_envs():
    path = Path(".")
    files = glob_env_files(path)
    assert isinstance(files, List)
