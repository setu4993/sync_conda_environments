from typing import List
from pathlib import Path

from ..helpers.file import *


def test_list_envs():
    path = Path('.')
    files = glob_env_files(path)
    assert isinstance(files, List)
