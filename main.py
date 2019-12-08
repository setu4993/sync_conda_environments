# Standard libraries
import argparse
import pathlib

from helpers.conda import create_update_envs, export_envs, list_envs
from helpers.file import glob_env_files

try:
    from loguru import logger
except ImportError:
    import logging
    logger = logging.getLogger(__name__)



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-u",
        "--update",
        help="Should the conda environments be updated?",
        action="store_true",
        default=False,
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        help="Output directory to store or load environment files from.",
        type=str,
        default=".",
    )

    args, _ = parser.parse_known_args()

    if not args.update:
        export, update = True, False
    else:
        export, update = False, True

    output_path = pathlib.Path(args.output_dir)
    assert (
        output_path.exists() and output_path.is_dir()
    ), "Output directory doesn't exist."
    logger.info(f"Using directory {output_path}.")

    envs = list_envs()
    logger.info(f"{len(envs)} environments found. They are: {envs}.")

    if export:
        logger.info("Executing export of conda environments.")
        result = export_envs(envs=envs, output_path=output_path)
        assert result, "Export didn't complete successfully."

    if update:
        logger.info("Executing update of conda environments.")
        env_files = glob_env_files(output_path)
        result = create_update_envs(envs=envs, env_files=env_files)
        assert result, "Create / update didn't complete successfully."


if __name__ == "__main__":
    main()
