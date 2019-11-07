from pathlib import Path
from typing import Generator


def glob_env_files(path: Path) -> Generator[Path, None, None]:
    return path.rglob("*.yml")
