"""Apps for the HCI."""

# Third-party dependencies:
from django.apps import AppConfig


class HCIConfig(AppConfig):
    """Configure the HCI app."""
    default_auto_field = "django.db.models.BigAutoField"
    name = "hci"
