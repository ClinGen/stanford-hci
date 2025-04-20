"""Provide services related to alleles."""

import requests

from apps.core.constants.third_party import Requests
from apps.markers.constants.services import URLs


class AlleleClient:
    """Fetch an HLA allele's info."""

    def __init__(self, ipd_accession: str) -> None:
        """Get info for the allele."""
        self.ipd_accession = ipd_accession
        self._data = None
        self.name = None
        self.version = None

        # Fetch and populate the members.
        self._set_data()
        self._set_name()
        self._set_version()

    def _set_data(self) -> None:
        """Fetch the data from the IPD API for the given allele."""
        url = f"{URLs.IPD_API}/{self.ipd_accession}"
        response = requests.get(url, timeout=Requests.DEFAULT_TIMEOUT)
        response.raise_for_status()
        self._data = response.json()

    def _set_name(self) -> None:
        """Set the name of the allele."""
        self.name = self._data["name"]

    def _set_version(self) -> None:
        """Set the version of the allele."""
        self.version = self._data["release_version"]
