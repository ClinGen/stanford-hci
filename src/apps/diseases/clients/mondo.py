"""Provide a client for getting data from the Mondo Disease Ontology API."""

from base.clients import EntityClient, EntityClientError
from constants import MondoConstants


class MondoClientError(Exception):
    """Raise when a Mondo client encounters an error."""


class MondoClient(EntityClient):
    """Get data from the Mondo Disease Ontology API."""

    def __init__(self, mondo_id: str) -> None:
        """Set up the Mondo client."""
        super().__init__(base_url=MondoConstants.API_URL)
        self.mondo_id = mondo_id
        self._data = None
        self.label = None

    @staticmethod
    def _extract_data(json_data: dict) -> dict | None:
        """Extract the data we're interested in from the Mondo API response.

        Returns:
            The data we're interested in, or `None` if the data is not found.
        """
        if "_embedded" in json_data:
            embedded = json_data["_embedded"]
            if "terms" in embedded:
                terms = embedded["terms"]
                if len(terms) > 0:
                    return terms[0]
        return None

    def fetch(self) -> None:
        """Fetch data from the Mondo API and populate the members.

        Raises:
             MondoClientError: If the request fails, or we can't extract the data from
                 the response.
        """
        try:
            endpoint = f"{self.base_url}?iri={MondoConstants.IRI}/{self.mondo_id}"
            json_data = self.get_json(endpoint)
            extracted_data = self._extract_data(json_data)
            if extracted_data is None:
                error_message = f"Unable to extract data from Mondo API response for {self.mondo_id}"  # noqa: E501 (Breaking to another line would decrease readability.)
                raise MondoClientError(error_message)
            self._data = extracted_data
            self.label = self._data["label"]
        except EntityClientError as exc:
            error_message = f"Error fetching Mondo data for {self.mondo_id}: {exc}"
            raise MondoClientError(error_message) from exc
