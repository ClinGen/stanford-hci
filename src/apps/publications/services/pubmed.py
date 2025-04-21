"""Provide services related to PubMed."""

import os
from xml.etree import (  # noqa: S405 (If we can't trust XML from NCBI we have bigger problems.)
    ElementTree,
)

import requests

from apps.core.constants.third_party import Requests
from apps.publications.constants.services import URLs


class PubMedArticleClient:
    """Fetch a PubMed article's info."""

    def __init__(self, pmid: str) -> None:
        """Get info for the article."""
        self.pmid = pmid
        self._data = None
        self.title = None

        # Fetch data populate the members.
        self._set_data()
        self._set_title()

    def _set_data(self) -> None:
        """Fetch the data from the PubMed API."""
        params = {
            "db": "pubmed",
            "id": self.pmid,
            "retmode": "xml",
            "api_key": os.getenv("PUBMED_API_KEY"),
        }
        response = requests.get(
            url=URLs.PUBMED_API, params=params, timeout=Requests.DEFAULT_TIMEOUT
        )
        response.raise_for_status()
        self._data = ElementTree.fromstring(response.text)  # noqa: S314 (If we can't trust XML from NCBI we have bigger problems.)

    def _set_title(self) -> None:
        """Extract the authors from the XML and set them."""
        self.title = self._data.find(
            ".//PubmedArticle/MedlineCitation/Article/ArticleTitle"
        ).text
