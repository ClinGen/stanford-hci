"""Run command line tasks for this project.

Assuming you've activated the virtual environment for this project,
here's how to format the code:
    inv fmt

To see a list of available tasks:
    inv --list
"""

# Invoke always requires a context parameter, even if it ends up going
# unused. There are two tasks that don't use their context parameters.
# pylint: disable=unused-argument

import sys

from dotenv import dotenv_values, load_dotenv
from invoke import task

# Set environment variables.
load_dotenv()

# Environment variable files:
ENV_TEMPLATE = ".env.template"
ENV_ACTUAL = ".env"

# Configs:
TEMPLATE_CONF = dotenv_values(ENV_TEMPLATE)
ACTUAL_CONF = dotenv_values(ENV_ACTUAL)


@task
def envsame(c):
    """Ensure environment variable keys match."""
    if TEMPLATE_CONF.keys() != ACTUAL_CONF.keys():
        print(".env keys do not match. Check your .env files.")
        sys.exit(1)


@task
def fmt(c):
    """Format source code and docstrings, and sort imports."""
    c.run("black .")
    c.run("docformatter .")
    c.run("isort .")


@task
def lint(c):
    """Lint source code."""
    c.run("pylint .")


@task
def check_types(c):
    """Check types of the source code."""
    c.run("mypy .")


@task
def test(c):
    """Run the whole test suite."""
    c.run("")


@task(pre=[envsame, fmt, lint, check_types, test])
def check(c):
    """Run all code checks."""
