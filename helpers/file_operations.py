from glob import glob
from os.path import join


def glob_env_files(path: str):
    return glob(join(path, "*.yml"))
