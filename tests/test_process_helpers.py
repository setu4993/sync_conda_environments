from ..helpers.process import run_subprocess


def test_run_subprocess():
    output = run_subprocess(["pwd"])
    assert output is not None
    assert isinstance(output, bytes)
