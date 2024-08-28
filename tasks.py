"""Script for running any/all command line tasks for this project.

All command line tasks should be defined in this file. The only
exception to this is managing dependencies via Pipenv.
"""

# Invoke always requires a context parameter, even if it ends up going
# unused. As of this writing, there are a handful of tasks that don't
# use their context parameters.
# pylint: disable=unused-argument

# Built-in libraries:
import sys

# Third-party dependencies:
from dotenv import dotenv_values
from dotenv import load_dotenv
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
def fmt(c):
    """Format code and Markdown."""
    c.run("black .")
    c.run("mdformat README.md")
    c.run("mdformat doc")


@task
def lint(c):
    """Run the linter."""
    c.run("pylint src")
    c.run("pylint tasks.py")


@task
def types(c):
    """Check types."""
    c.run("mypy .")


@task
def env_same(c):
    """Ensure environment variable keys match."""
    if TEMPLATE_CONF.keys() != ACTUAL_CONF.keys():
        print(".env keys do not match. Check your .env files.")
        sys.exit(1)


@task(pre=[fmt, lint, types, env_same])
def check(c):
    """Run all code checks."""


@task
def dev(c):
    """Run the development server.

    TL;DR: This command works, but it doesn't show all output.

    There is some output that isn't immediately shown when you run this
    command. I looked at Django's code, and it looks like there's some
    weirdness with how the runserver command works. It looks like
    runserver (by default) has an auto-reload feature. This auto-reload
    feature logs some output. The runserver command itself writes
    directly to stdout using Python's API for writing to stdout. I think
    Invoke intercepts the log from the auto-reload code first, then it
    intercepts the runserver command's writes to stdout. It doesn't show
    the runserver command's writes to stdout until keyboard interrupt.
    """
    port = 8000
    print(f"http://127.0.0.1:{port}/")
    c.run(f"python ./src/manage.py runserver {port}")
