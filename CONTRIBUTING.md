# Contributing to handwritten-calculator

What could make this demo application better? Suggestions and PR's welcome!

## Code Formatting

This code was formatted using `black`, `isort`, `flake8`, and `mypy`. See the [developer requirements](./requirements_dev.txt) to include those tools in a Python virtual environment.

### Sample Virtual Environment Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
python -m pip install -r requirements_dev.txt
...
```

After initial installation of `black`, `flake8`, and `isort` you may need to deactivate and reactivate the virtual environment to get access to the command-line tools.

To deactivate the virtual environment while you are in it, use

```bash
deactivate
```

`python -m pip install -r requirements_dev.txt`

## License

By contributing to handwritten-calculator, you agree that your contributions will be licensed
under the LICENSE file in the root directory of this source tree.
