"""This script provides a method for the developer to manually migrate the HCI's RDS
database."""

import click

from scripts.util import run_ecs_task


@click.command()
@click.option(
    "--environment",
    help="The HCI environment where you want to migrate (either 'staging' or 'production')",
    required=True,
)
def migrate(environment):
    """Migrate the HCI's RDS database."""
    run_ecs_task("hci_db_migration_task", environment)


if __name__ == "__main__":
    migrate()  # pylint: disable=no-value-for-parameter
