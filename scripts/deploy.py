"""Deploys the HCI.

Note: This script assumes you're running it from the root of the HCI repo.

Example staging deployment from the root of the HCI repo:
    python ./scripts/deploy.py --environment=staging

Alternatively, you could use the run script wrapper:
    run deploy:stag
"""

# pylint: disable=duplicate-code
# pylint: disable=inconsistent-return-statements
# pylint: disable=line-too-long

import subprocess
import sys

import click


def run(cmd: str, silent: bool = False):
    """Runs a command and prints a friendly error message if necessary."""
    try:
        if not silent:
            print(f"Running command: {cmd}")
        result = subprocess.run(
            cmd.split(" "), capture_output=True, check=True, text=True
        )
        if result.returncode == 0 and not silent:
            print("Done")
    except subprocess.CalledProcessError as err:
        print(f"Error: Command {cmd} failed with return code {err.returncode}")
        if err.stdout:
            print(f"    stdout: {err.stdout}")
        if err.stderr:
            print(f"    stderr: {err.stderr}")
        print("Exiting")
        sys.exit(1)


@click.command()
@click.option(
    "--environment",
    help="Where to deploy the HCI (either 'staging' or 'production')",
    required=True,
)
@click.option(
    "--silent",
    help="Whether to prompt the user for a yes/no response about deploying (either 'true' or 'false')",
    required=False,
)
def deploy(environment: str, silent: str):
    """Deploys the HCI to the given environment."""

    if environment not in ("staging", "production"):
        print(f"Error: Environment '{environment}' not valid")
        print("Error: Environment should be either 'staging' or 'production'")
        sys.exit(1)

    if not silent or silent.lower() in ("false", "f", "no", "n"):
        ans = input(
            f"This will deploy the HCI to the {environment} environment. Do you wish to proceed? (y/n): "
        )
        if ans.lower() in ("no", "n"):
            sys.exit(1)

    # Set up commands.
    if environment == "staging":
        env_abbrev = "stag"
    else:
        env_abbrev = "prod"
    migrate_db = f"./run db:migrate:{env_abbrev}"
    print(migrate_db)
    authenticate_to_ecr = "./run ecr:auth"
    print(authenticate_to_ecr)
    build_new_docker_image = f"./run ecr:build:{env_abbrev}"
    print(build_new_docker_image)
    push_image_to_ecr = f"./run ecr:push:{env_abbrev}"
    print(push_image_to_ecr)
    update_ecs = f"./run ecs:update:{env_abbrev}"
    print(update_ecs)


if __name__ == "__main__":
    deploy()  # pylint: disable=no-value-for-parameter
