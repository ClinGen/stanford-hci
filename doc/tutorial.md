# Tutorials

Tutorials are lessons that take the reader by the hand through a series
of steps to complete a project of some kind. Unlike how-to guides,
tutorials don't assume lots of prerequisite knowledge.

## Getting started

- Clone the repository to your local machine.
- Install Docker Desktop.
- Create an environment variables file: `cp .env.example .env`.
- Build everything: `docker compose up --build`.
- In another terminal window, set up the database: `./run manage migrate`.
- Visit http://localhost:8000 in your favorite browser.
- To stop the server, press `Ctrl+C` in the terminal window where you
  ran `docker compose up --build`.
- Read through the `run` script to see what other tasks you can run.

## Using the `run` script

You'll notice in the root of this repository, there's a Bash script
call `run`. It can be used to run most command line tasks we need for
this repository. To see the tasks available to run, invoke `./run help`.

## Updating and installing dependencies

You can run `./run pip3:outdated` to get a list of outdated dependencies based
on what you currently have installed. Once you've figured out what you want to
update, go make those updates in your `requirements.txt` file.

As for the `requirements-lock.txt` file, this ensures that the same exact
versions of every package you have (including dependencies of dependencies) get
used the next time you build the project. This file is the output of
running `pip3 freeze`. You can check how it works by looking at
[`bin/pip3-install`](../bin/pip3-install).

You should never modify the lock files by hand. Add your top level Python
dependencies to `requirements.txt`, then run `./bin/pip3-install`. Then remember
to `docker compose up --build` to see the changes reflected in your Docker
container.