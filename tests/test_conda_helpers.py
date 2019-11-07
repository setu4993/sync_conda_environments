from typing import List
from ..helpers.conda import *


def test_list_envs():
    envs = list_envs()
    assert isinstance(envs, List)
    assert len(envs) >= 0
