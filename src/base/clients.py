"""Provide base classes for clients."""

from abc import ABC, abstractmethod


class Client(ABC):
    """Get data from an external source."""

    @abstractmethod
    def get_data(self, url: str) -> str:
        """Get the contents of a URL.

        Args:
             url: The URL to get data from.

        Returns:
            The string contents of the data.
        """
