import pathlib

from helpers.conda import create_update_envs, export_envs, list_envs
from helpers.file import glob_env_files

if __name__ == "__main__":
    # TODO: Handle args.
    export = True
    update = False
    output_dir = "."

    output_path = pathlib.Path(output_dir)

    assert output_path.exists(), "Output directory doesn't exist"

    envs = list_envs()

    if export:
        export_envs(envs=envs, output_path=output_path)

    if update:
        env_files = glob_env_files(output_path)
        create_update_envs(envs=envs, env_files=env_files)
