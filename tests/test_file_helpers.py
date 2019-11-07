from typing import List
from types import GeneratorType
from pathlib import Path

from ..helpers.file import *


def test_list_envs():
    path = Path('.')
    files = glob_env_files(path)
    assert isinstance(files, GeneratorType)
    files = [file for file in files]
    assert isinstance(files, List)
