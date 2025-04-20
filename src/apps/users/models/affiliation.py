"""Provide a model for affiliations."""

from django.db import models

from apps.users.constants.models import FieldLengths


class Affiliation(models.Model):
    """An affiliation is a group of curators working on the same project."""

    affiliation_id: models.CharField = models.CharField(
        max_length=FieldLengths.AFFILIATION_ID,
        primary_key=True,
        verbose_name="Affiliation ID",
    )
    affiliation_name: models.CharField = models.CharField(
        max_length=FieldLengths.DEFAULT_CHAR_FIELD,
        verbose_name="Affiliation Name",
    )

    def __str__(self) -> str:
        """Return a string representation of the affiliation."""
        return f"{self.affiliation_name} ({self.affiliation_id})"
