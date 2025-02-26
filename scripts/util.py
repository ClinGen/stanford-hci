"""Provides utility functions for the scripts."""

# pylint: disable=inconsistent-return-statements

import re
import subprocess
import sys
from typing import List

import boto3


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
        print(f"  Error: Command {cmd} failed with return code {err.returncode}")
        if err.stdout:
            print(f"    stdout: {err.stdout}")
        if err.stderr:
            print(f"    stderr: {err.stderr}")
        print("Exiting")
        sys.exit(1)


def run_ecs_task(ecs_task_name: str, environment: str):
    """Migrate the HCI's RDS database."""

    if environment not in ("staging", "production"):
        print(f"  Error: Environment '{environment}' not valid")
        print("  Error: Environment should be either 'staging' or 'production'")
        sys.exit(1)

    ecs_cluster_name = f"hci_cluster_{environment}"

    # Extract the subnets and security groups from the Terraform output.
    subnets = find_pattern_in_terraform_output(environment, r"subnet-[a-z0-9]+")
    security_groups = find_pattern_in_terraform_output(environment, r"sg-[a-z0-9]+")

    # Run the migration.
    ecs_client = boto3.client("ecs")
    ecs_client.run_task(
        cluster=ecs_cluster_name,
        taskDefinition=ecs_task_name,
        launchType="FARGATE",
        networkConfiguration={
            "awsvpcConfiguration": {
                "subnets": subnets,
                "securityGroups": security_groups,
                "assignPublicIp": "ENABLED",
            }
        },
    )
