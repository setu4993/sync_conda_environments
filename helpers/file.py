from pathlib import Path


def glob_env_files(path: Path):
    return path.rglob('*.yml')
