# Provide a simple way to run commands for this project. It also documents
# command line tasks for this project. In order to use it, you must install the
# `just` program: https://github.com/casey/just.
#
# The tasks in this file are grouped into sections. The sections should be in
# alphabetical order. The sections are delineated by comments with lots of
# equal signs. The tasks within a section have a prefix. For example, Python
# tasks have the prefix "py". If a section contain tasks related to a
# programming language, it's a good idea to use the file extension for that
# programming language.
#
# Each task should have a comment above it. When you run `just -l`, you will see
# each task and its corresponding comment. Prefix the task comment with the
# section name and a colon.

#===============================================================================
# Python
#===============================================================================

# Python: Format all files in the current directory and all subdirectories.
pyfmt:
    uv run ruff format

# Python: Lint all files in the current directory and all subdirectories.
pylint:
    uv run ruff check
