# Overview

For verifying the issue here https://github.com/Microsoft/vscode-python/issues/170

This issue was reproduced in the following environment.

    VS Code version: 1.22.2
    Python Extension version: 2018.3.1
    Python Version: 3.6.4
    OS and version: MacOS 10.13.4

## Reproducing

- Install the requirements in `requirements.txt`
- Setup the database with `./manage.py migrate`
- Set a breakpoint in `exampleproject/views.py` on line 5
- Launch the `Python: Django` debug configuration
- Make a post request to `http://localhost:8000`
