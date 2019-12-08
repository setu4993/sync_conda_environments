# Standard libraries
from pathlib import Path
from typing import List


def glob_env_files(path: Path) -> List[Path]:
    return list(path.rglob("*.yml"))
