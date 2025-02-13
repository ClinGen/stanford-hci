"""This module contains the Django configuration of the HCI app."""

import os

from django.apps import AppConfig
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from util.secrets import get_secret


class HCIConfig(AppConfig):
    """Configure the HCI Django app."""

    name = "hci"

    def ready(self):
        """Run code when Django starts."""
        # Make sure a superuser exists.
        host = os.getenv("HCI_HOST")
        if host in ("staging", "production"):
            username = get_secret(f"hci_django_superuser_username_{host}")
            try:
                User.objects.get(username=username)
            except ObjectDoesNotExist:
                User.objects.create_superuser(
                    username=username,
                    email=get_secret(f"hci_django_superuser_email_{host}"),
                    password=get_secret(f"hci_django_superuser_password_{host}"),
                )
