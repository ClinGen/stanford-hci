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

# Make sure we load the `.env` file before we run commands.
set dotenv-load := true

#=======================================================================================
# Public Recipes
#=======================================================================================

# Run all code quality checks.
check: format lint type _dj_check test coverage

# Show test coverage.
coverage: _py_coverage

# Run the development server.
dev: _dj_makemigrations _dj_migrate _dj_runserver

# Build the developer documentation site.
docs: _sp_build_html

# Format Python code.
format: _py_format

# Check Python code for common mistakes that can be identified by static analysis.
lint: _py_lint

# Run all tests.
test: _dj_makemigrations _dj_migrate _py_test

# Check Python code for problems with type hints.
type: _py_type

#=======================================================================================
# Django Recipes
#=======================================================================================

# Use the system check framework to inspect the project for common problems.
_dj_check:
    cd src && uv run manage.py check

# Make migrations.
_dj_makemigrations:
    cd src && uv run manage.py makemigrations

# Apply migrations.
_dj_migrate:
    cd src && uv run manage.py migrate

# Run the development server.
_dj_runserver:
    cd src && uv run manage.py runserver

# Enter the shell.
_dj_shell:
    cd src && uv run manage.py shell

#=======================================================================================
# Python Code Quality Recipes
#=======================================================================================

# Format all files in the current directory and all subdirectories.
_py_format:
    cd src && uv run ruff format

# Check all files in the current directory and all subdirectories for formatting issues.
_py_format_check:
    cd src && uv run ruff format --check

# Lint all files in the current directory and all subdirectories.
_py_lint:
    cd src && uv run ruff check

# Try to fix lint errors in current directory and all subdirectories.
_py_lint_fix:
    cd src && uv run ruff check --fix

# Check type hints in the `src` directory and all subdirectories.
_py_type:
    cd src && uv run mypy .

# Run test suite and collect coverage stats.
_py_test:
    cd src && uv run coverage run -m pytest

# Report the test coverage stats.
_py_coverage:
    cd src && uv run coverage report

# Build the test coverage report site.
_py_build_coverage_html:
    cd src && uv run coverage html

#=======================================================================================
# Sphinx Documentation Recipes
#=======================================================================================

# Build the developer documentation site.
_sp_build_html:
    cd docs && uv run make html