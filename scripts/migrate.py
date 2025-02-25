"""This script provides a method for the developer to manually migrate the HCI's RDS
database."""

# pylint: disable=duplicate-code
# pylint: disable=inconsistent-return-statements
# pylint: disable=line-too-long

import re
import subprocess
import sys
from typing import List

import boto3
import click


def find_pattern_in_terraform_output(environment: str, pattern: str) -> List[str]:
    """Finds all instances of the given pattern in the Terraform output for the given
    environment.

    Args:
        environment: Either 'staging' or 'production'.
        pattern: A regular expression.
    Returns:
        A list of the matches.
    """
    cmd = "./run tf:output:"
    if environment == "staging":
        cmd += "stag"
    elif environment == "production":
        cmd += "prod"
    try:
        result = subprocess.run(
            cmd.split(" "), capture_output=True, check=True, text=True
        )
        if result.stdout:
            return re.findall(pattern, result.stdout)
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
    help="The HCI environment where you want to migrate (either 'staging' or 'production')",
    required=True,
)
def migrate(environment):
    """Migrate the HCI's RDS database."""

    if environment not in ("staging", "production"):
        print(f"Error: Environment '{environment}' not valid")
        print("Error: Environment should be either 'staging' or 'production'")
        sys.exit(1)

    # Create the variables we need for the task.
    ecs_cluster_name = f"hci_cluster_{environment}"
    ecs_db_migration_task_name = "hci_db_migration_task"

    # Extract the subnets and security groups from the Terraform output.
    subnets = find_pattern_in_terraform_output(environment, r"subnet-([a-z0-9]+)")
    security_groups = find_pattern_in_terraform_output(environment, r"sg-([a-z0-9]+)")

    # Run the migration.
    ecs_client = boto3.client("ecs")
    ecs_client.run_task(
        cluster=ecs_cluster_name,
        taskDefinition=ecs_db_migration_task_name,
        launchType="FARGATE",
        networkConfiguration={
            "awsvpcConfiguration": {
                "subnets": subnets,
                "securityGroups": security_groups,
                "assignPublicIp": "ENABLED",
            }
        },
    )


if __name__ == "__main__":
    migrate()  # pylint: disable=no-value-for-parameter
