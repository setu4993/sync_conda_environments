# Sync Conda Environments

![!GitHub Action: Run Test](https://github.com/setu4993/sync_conda_environments/workflows/Tests/badge.svg) | [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Sync **all** your Conda environments across multiple computers. I found myself struggling to recreate my multiple virtual environments across multiple machines, so wrote this fairly simple project.

This can only be used on the same OS (MacOS, Windows, etc.) and architecture (x64, x32) because of the way conda creates binaries for packages. (Unless your whole environemnt is no-arch.)

## Requirements

Tested on Python 3.7, doesn't require any other dependency for execution. Does require `pytest` for testing only (`requirements-tests.txt`).
