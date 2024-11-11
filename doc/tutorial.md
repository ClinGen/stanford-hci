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