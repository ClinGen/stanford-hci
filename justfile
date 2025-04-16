# Provide a simple way to run commands for this project.
#
# This file also documents command line "recipes" for this project. In order to use it,
# you must install the `just` program: https://github.com/casey/just.
#
# The command line recipes in this file are divided into public and private recipes.
# Public recipes are not prefixed with an underscore. Private recipes are prefixed with
# an underscore.
#
# The recipes in this file are grouped into sections. The first section in the file is
# the "Public" section. The private sections should follow in alphabetical order. The
# sections are delineated by comments with lots of equal signs. Recipes within a private
# section have a prefix. For example, private Python recipes have the prefix "_py". If a
# section contains recipes related to a programming language, it's a good idea to use
# the file extension for that programming language.
#
# Each recipe should have a comment above it. When you run `just -l`, you will see each
# public recipe and its corresponding comment. (Private recipes are hidden.)
#
# NOTE: For the sake of simplicity, we assume the user of this justfile is invoking the
# recipes from the root of the repository.

#=======================================================================================
# Public Recipes
#=======================================================================================

# Format Python code.
fmt: _py_fmt

# Check Python code for common mistakes that can be identified by static analysis.
lint: _py_lint

# Check Python code for problems with type hints.
type: _py_type

# Run the test suite.
test: _dj_makemigrations _dj_migrate
    cd src && python manage.py test

# Run all code quality checks.
check: fmt lint type test _dj_check

# Run the development server.
dev: _dj_makemigrations _dj_migrate
    cd src && python manage.py runserver

#=======================================================================================
# Django Recipes
#=======================================================================================

# Use the system check framework to inspect the project for common problems.
_dj_check:
    cd src && python manage.py check

# Make migrations.
_dj_makemigrations:
    cd src && python manage.py makemigrations

# Apply migrations.
_dj_migrate:
    cd src && python manage.py migrate

# Run the development server.
_dj_runserver:
    cd src && python manage.py runserver

# Enter the shell.
_dj_shell:
    cd src && python manage.py shell

#=======================================================================================
# Python Code Quality Recipes
#=======================================================================================

# Format all files in the current directory and all subdirectories.
_py_fmt:
    uv run ruff format

# Check all files in the current directory and all subdirectories for formatting issues.
_py_fmt_check:
    uv run ruff format --check

# Lint all files in the current directory and all subdirectories.
_py_lint:
    uv run ruff check

# Try to fix lint errors in current directory and all subdirectories.
_py_lint_fix:
    uv run ruff check --fix

# Check type hints in the `src` directory and all subdirectories.
_py_type:
    cd src && uv run mypy .
