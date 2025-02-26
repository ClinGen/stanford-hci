"""Creates a superuser.

Useful when you've just created the infrastructure.
"""

# pylint: disable=line-too-long

import click

from scripts.util import run_ecs_task


@click.command()
@click.option(
    "--environment",
    help="The HCI environment where you want to create the superuser (either 'staging' or 'production')",
    required=True,
)
def createsuperuser(environment):
    """Create a superuser for the HCI."""
    run_ecs_task("hci_createsuperuser_task", environment)


if __name__ == "__main__":
    createsuperuser()  # pylint: disable=no-value-for-parameter
