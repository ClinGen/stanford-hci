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


def run(cmd: str):
    """Runs a command and prints a friendly error message if necessary."""
    try:
        print(f"Running command: {cmd}")
        result = subprocess.run(
            cmd.split(" "), capture_output=True, check=True, text=True
        )
        if result.returncode == 0:
            print("Done")
        else:
            print(f"Done with return code {result.returncode}")
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
def deploy(environment: str):
    """Deploys the HCI to the given environment."""

    if environment not in ("staging", "production"):
        print(f"Error: Environment '{environment}' not valid")
        print("Error: Environment should be either 'staging' or 'production'")
        sys.exit(1)

    ans = input(
        f"This will deploy the HCI to the {environment} environment. Do you wish to proceed? (y/n): "
    )
    if ans.lower() != "y":
        sys.exit(1)

    # We need the abbreviation for our run script commands.
    if environment == "production":
        env_abbrev = "prod"
    else:
        env_abbrev = "stag"

    ans = input(f"Migrate the {environment} database? (y/n): ")
    if ans.lower() == "y":
        migrate_db = f"./run db:migrate:{env_abbrev}"
        run(migrate_db)

    ans = input(
        "Authenticate to ECR? This might be necessary if you haven't done it recently.) (y/n): "
    )
    if ans.lower() == "y":
        authenticate_to_ecr = "./run ecr:auth"
        run(authenticate_to_ecr)

    ans = input("Build new container image? (y/n): ")
    if ans.lower() == "y":
        build_new_docker_image = f"./run ecr:build:{env_abbrev}"
        run(build_new_docker_image)

    ans = input("Push the new container image to ECR? (y/n): ")
    if ans.lower() == "y":
        push_image_to_ecr = f"./run ecr:push:{env_abbrev}"
        run(push_image_to_ecr)

    ans = input("Update the ECS service? (y/n): ")
    if ans.lower() == "y":
        update_ecs = f"./run ecs:update:{env_abbrev}"
        run(update_ecs)


if __name__ == "__main__":
    deploy()  # pylint: disable=no-value-for-parameter
