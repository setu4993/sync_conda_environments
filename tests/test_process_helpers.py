from ..helpers.process import run_subprocess


def test_run_subprocess():
    output = run_subprocess(['man'])
    assert output is not None
    assert output is b''
