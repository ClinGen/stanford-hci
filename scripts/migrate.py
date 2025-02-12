"""This script provides a method for the developer to manually migrate the HCI's RDS
database."""

import boto3
import click


@click.command()
@click.option("--cluster", help="Name of the ECS cluster", required=True)
@click.option("--task", help="Name of the migration task", required=True)
@click.option("--sn", help="Comma-separated subnet IDs", required=True)
@click.option("--sg", help="Comma-separated security group IDs", required=True)
def migrate(cluster, task, sn, sg):
    """Migrate the HCI's RDS database."""
    ecs_client = boto3.client("ecs")
    response = ecs_client.run_task(
        cluster=cluster,
        taskDefinition=task,
        launchType="FARGATE",
        networkConfiguration={
            "awsvpcConfiguration": {
                "subnets": sn.split(","),
                "securityGroups": sg.split(","),
                "assignPublicIp": "ENABLED",
            }
        },
    )
    print(response)


if __name__ == "__main__":
    migrate()  # pylint: disable=no-value-for-parameter
