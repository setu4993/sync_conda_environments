from .conda_operations import list_envs, create_update_envs, export_envs
from .file_operations import glob_env_files


if __name__ == '__main__':
    # TODO: Handle args.
    export = True
    update = False

    output_dir = '.'

    envs = list_envs()

    if export:
        export_envs(envs=envs, output_path=output_dir)

    if update:
        env_files = glob_env_files(output_dir)
        create_update_envs(envs=envs, env_files=env_files)
