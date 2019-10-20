import glob


def glob_env_files(path: str):
    return glob.glob(path, "**", "*.yml")
