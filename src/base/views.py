"""Provide base classes for views."""

from abc import ABC, abstractmethod

from django.http import HttpResponse


class EntityView(ABC):
    """Create, view all, or view a specific entity.

    Here an entity refers to a model in the HCI that has a new page, an all page,
    and an overview page. Some examples include: curations, diseases, markers (alleles
    and haplotypes), and publications.
    """

    @abstractmethod
    def new(self) -> HttpResponse:
        """View the page that provides a form that creates a new entity."""

    @abstractmethod
    def list(self) -> HttpResponse:
        """View the searchable table page for an entity."""

    @abstractmethod
    def details(self, human_readable_id: str) -> HttpResponse:
        """View the details page for an entity.

        Args:
             human_readable_id: The human-readable ID of the model for the entity.
        """
