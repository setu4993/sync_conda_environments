from subprocess import run
from typing import List


def run_command(command: List[str]) -> str:
    proc = run(command, capture_output=True)
    assert proc.args == command, f"Command executed process different from the command passed."
    assert proc.returncode == 0, f"Error in running sub-process, sub-process returned with a non-zero exit code {proc.returncode}."
    return proc.stdout