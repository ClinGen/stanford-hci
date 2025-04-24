"""Provide services related to diseases."""

import requests

from constants import MondoConstants, RequestsConstants


class DiseaseClient:
    """Fetch a disease's info."""

    def __init__(self, mondo_id: str) -> None:
        """Get info the for disease."""
        self.mondo_id = mondo_id
        self._data = None
        self.label = None

        # Fetch data and populate members.
        self._set_data()
        self._set_label()

    def _set_data(self) -> None:
        """Fetch the data from the OLS Mondo API for the given disease."""
        url = f"{MondoConstants.API_URL}?iri={MondoConstants.IRI}/{self.mondo_id}"
        response = requests.get(url, timeout=RequestsConstants.DEFAULT_TIMEOUT)
        response.raise_for_status()
        json = response.json()
        if "_embedded" in json:
            embedded = json["_embedded"]
            if "terms" in embedded:
                terms = embedded["terms"]
                if len(terms) > 0:
                    self._data = terms[0]

    def _set_label(self) -> None:
        """Set the label of the disease."""
        self.label = self._data["label"]
