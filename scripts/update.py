"""This script provides a method for the developer to manually update the HCI's ECS
Fargate service."""

import os
import sys

import boto3
import click

# These variables should match what they are in the Terraform code.
CPU = "256"
MEMORY = "512"
NETWORK_MODE = "awsvpc"
COMPATIBILITIES = ["FARGATE"]
EXECUTION_ROLE = "hci_ecs_task_execution_role"
TASK_ROLE = "hci_ecs_task_execution_role"


@click.command()
@click.option(
    "--environment",
    help="The Terraform workspace (either 'staging' or 'production')",
    required=True,
)
def update(environment):
    """Update the HCI's Fargate service."""

    if environment == "staging":
        cluster = "hci_cluster_staging"
        service = "hci_service_staging"
        registry_name = "hci_registry_staging"
    elif environment == "production":
        cluster = "hci_cluster_production"
        service = "hci_service_production"
        registry_name = "hci_registry_production"
    else:
        print(
            f"  Error: Environment {environment} must be either 'staging' or 'production'"
        )
        sys.exit(1)

    client = boto3.client("ecs")

    # Get the task definition.
    response = client.describe_services(cluster=cluster, services=[service])
    current_task_arn = response["services"][0]["taskDefinition"]

    # Get the container definition.
    response = client.describe_task_definition(taskDefinition=current_task_arn)
    container_definition = response["taskDefinition"]["containerDefinitions"][0].copy()

    # Update the image.
    image = f"{os.getenv('AWS_ACCOUNT_ID')}.dkr.ecr.us-west-2.amazonaws.com/{registry_name}:latest"
    container_definition["image"] = image

    # Register a new task definition.
    response = client.register_task_definition(
        family=response["taskDefinition"]["family"],
        volumes=response["taskDefinition"]["volumes"],
        containerDefinitions=[container_definition],
        cpu=CPU,
        memory=MEMORY,
        networkMode=NETWORK_MODE,
        requiresCompatibilities=COMPATIBILITIES,
        executionRoleArn=f"{EXECUTION_ROLE}_{environment}",
        taskRoleArn=f"{TASK_ROLE}_{environment}",
    )
    new_task_arn = response["taskDefinition"]["taskDefinitionArn"]

    # Update the service with the new task definition.
    client.update_service(
        cluster=cluster,
        service=service,
        taskDefinition=new_task_arn,
    )


if __name__ == "__main__":
    update()  # pylint: disable=no-value-for-parameter
