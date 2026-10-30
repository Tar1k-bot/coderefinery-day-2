# CodeRefinery Day 2 starter

**A small Python teaching project for the NLTU workshop with Yuriy Paslavskyi.
It is a hands-on starting point for practicing Python, automated tests with
pytest, Git branches and pull requests, and GitHub Actions.**

## **Project files**

- **`example.py` contains simple addition and subtraction functions and their tests.**
- **`requirements-dev.txt` lists the development dependency, pytest.**
- **`.github/workflows/ci.yml` defines the GitHub Actions test workflow.**
- **`LICENSE` contains the project's MIT license.**
- **`README.md` explains how to set up and use the project.**

**The requested `recipes.py` and `tests/test_recipes.py` files are not present in
the current checkout. The commands below document how to run them once those
files are available; their recipe behavior and tests cannot be described from
this checkout.**

## **Set up on Windows with Git Bash**

**Install Git for Windows and Python 3.13, then open Git Bash in the repository
folder. Create and activate a virtual environment:**

```bash
python -m venv .venv
source .venv/Scripts/activate
```

**Install the development dependencies:**

```bash
python -m pip install -r requirements-dev.txt
```

**To run the recipe script:**

```bash
python recipes.py
```

**To run all tests in `example.py` and the `tests` directory:**

```bash
python -m pytest -v example.py tests
```

**These last two commands require `recipes.py` and `tests/test_recipes.py`, which
are not currently included in this checkout.**

## **Continuous integration**

**The project uses a simple GitHub Actions workflow defined in
`.github/workflows/ci.yml`. It runs on an Ubuntu runner, sets up Python 3.13,
installs the dependencies from `requirements-dev.txt`, and runs
`python -m pytest -v example.py`.**

**A push to `main` and a pull request targeting `main` start this check. The
workflow can also be started manually with `workflow_dispatch`. Under the
current branch filter, a push to a feature branch without a pull request does
not start the check.**

**To see a run's result, open the repository on GitHub, select Actions, open
the Python tests workflow, and choose a run. The job and step logs show the
test output and whether the check passed.**

## Start your own project

1. Select **Use this template → Create a new repository** on GitHub.
2. Create the repository in your own account; include only the default branch.
3. Clone **your new repository** and open its folder in VS Code.

## License and sources

**This teaching adaptation is distributed under the [MIT License](LICENSE).
See `LICENSE` for the license terms; the license and its copyright notice are
unchanged.**

**This project follows the learning pattern of
[CodeRefinery testing](https://coderefinery.github.io/testing/) and
[full-cycle collaboration](https://coderefinery.github.io/testing/full-cycle-ci/).**
Prepared with AI assistance; the local test checkpoints were checked separately.
