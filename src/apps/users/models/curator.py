"""Provide a model for curators."""

from django.contrib.auth.models import User
from django.db import models

from apps.users.constants.model_constants import DefaultValues
from apps.users.models.affiliation import Affiliation


class Curator(models.Model):
    """A curator is a user with at least one affiliation."""

    user: models.OneToOneField = models.OneToOneField(User, on_delete=models.CASCADE)
    affiliations: models.ManyToManyField = models.ManyToManyField(Affiliation)
    active_affiliation: models.ForeignKey = models.ForeignKey(
        Affiliation,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="active_curators",
        default=DefaultValues.AFFILIATION_ID,
        verbose_name="Active Affiliation",
    )

    def __str__(self) -> str:
        """Return a string representation of the curator."""
        return f"{self.user.first_name} {self.user.last_name} ({self.user.email})"
