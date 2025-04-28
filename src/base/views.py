"""Provide base classes for views."""

from abc import ABC, abstractmethod
from typing import Any


class EntityView(ABC):
    """Create, view all, or view a specific entity.

    Here an entity refers to a model in the HCI that has a new page, an all page,
    and an overview page. Some examples include: curations, diseases, markers (alleles
    and haplotypes), and publications.
    """

    @abstractmethod
    def new(self) -> Any:  # noqa: ANN401 (We don't care about this for abstract methods.)
        """View the page that provides a form that creates a new entity."""

    @abstractmethod
    def list(self) -> Any:  # noqa: ANN401 (We don't care about this for abstract methods.)
        """View the searchable table page for an entity."""

    @abstractmethod
    def details(self, human_readable_id: str) -> Any:  # noqa: ANN401 (We don't care about this for abstract methods.)
        """View the details page for an entity.

        Args:
             human_readable_id: The human-readable ID of the model for the entity.
        """
