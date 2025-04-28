"""Provide base classes for clients."""

import json
import logging
from xml.etree import ElementTree as ET

import requests

from constants import RequestsConstants

logger = logging.getLogger(__name__)


class ClientError(Exception):
    """Raise when a client encounters an error."""


class Client:
    """Get data from an external source."""

    def __init__(
        self, base_url: str = "", timeout: int = RequestsConstants.DEFAULT_TIMEOUT
    ) -> None:
        """Set the base URL and timeout.

        Args:
             base_url: The base URL of the external source, e.g. "https://example.com".
             timeout: The timeout in seconds for the request.
        """
        self.base_url = base_url
        self.timeout = timeout
        self.headers = {}

    def _get(self, endpoint: str, params: dict | None = None) -> requests.Response:
        """Perform a GET request to the external source.

        Args:
            endpoint: The portion of the URL after the base, e.g. "path/to/resource".
            params: Query parameters to be included in the request.

        Raises:
            ClientError: If the request fails.

        Returns:
             The response from the external source.
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        try:
            logger.debug(f"GET {url} with params {params}")
            response = requests.get(
                url, params=params, headers=self.headers, timeout=self.timeout
            )
            response.raise_for_status()
        except requests.exceptions.RequestException as exc:
            error_message = f"Error during GET request to {url}: {exc}"
            raise ClientError(error_message) from exc
        return response

    def get_json(self, endpoint: str, params: dict | None = None) -> dict:
        """Perform a GET request to the external source and return the JSON response.

        Args:
            endpoint: The portion of the URL after the base, e.g. "path/to/resource".
            params: Query parameters to be included in the request.

        Raises:
             ClientError:
                 If the request fails or the response is not valid JSON.

        Returns:
            A dictionary representing the JSON response.
        """
        response = self._get(endpoint, params=params)
        try:
            data = response.json()
        except json.JSONDecodeError as exc:
            error_message = f"Failed to decode JSON from response: {exc}"
            raise ClientError(error_message) from exc
        return data

    def get_xml(self, endpoint: str, params: dict | None = None) -> ET.Element:
        """Perform a GET request to the external source and return the XML response.

        Args:
            endpoint: The portion of the URL after the base, e.g. "path/to/resource".
            params: Query parameters to be included in the request.

        Raises:
            ClientError: If the request fails or the response is not valid XML.

        Returns:
            An ET object representing the XML response.
        """
        response = self._get(endpoint, params=params)
        try:
            data = ET.fromstring(response.content)
        except ET.ParseError as exc:
            error_message = f"Failed to parse XML from response: {exc}"
            raise ClientError(error_message) from exc
        return data
