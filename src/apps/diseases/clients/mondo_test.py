"""Test the Mondo client.

This module contains tests for the `MondoClient` class, which is responsible
for fetching and processing disease data from the Mondo Disease Ontology API.
"""

from unittest.mock import Mock

import pytest

from apps.diseases.clients.mondo import MondoClient, MondoClientError
from base.clients import EntityClientError, HTTPClient
from constants import MondoConstants


@pytest.fixture
def json_data_valid() -> dict:
    """Return valid JSON data from the Mondo API.

    This is the expected format of the JSON data returned by the Mondo API.
    """
    # fmt: off
    return {
        "_embedded": {
            "terms": [
                {
                    "label": "disease label",
                    "other": "info"
                }
            ]
        }
    }
    # fmt: on


@pytest.fixture
def json_data_no_embedded() -> dict:
    """Return JSON data with no `_embedded` key from the Mondo API."""
    # fmt: off
    return {
        "no_embedded": {
            "terms": [
                {
                    "label": "disease label",
                    "other": "info"
                }
            ]
        }
    }
    # fmt: on


@pytest.fixture
def json_data_no_terms() -> dict:
    """Return JSON data with no `terms` key from the Mondo API."""
    # fmt: off
    return {
        "_embedded": {
            "no_terms": [
                {
                    "label": "disease label",
                    "other": "info"
                }
            ]
        }
    }
    # fmt: on


@pytest.fixture
def json_data_empty_terms() -> dict:
    """Return JSON data with an empty `terms` list from the Mondo API."""
    # fmt: off
    return {
        "_embedded": {
            "terms": []
        }
    }
    # fmt: on


@pytest.fixture
def expected_extracted_data() -> dict:
    """Return the JSON data that should be extracted from the Mondo API response."""
    # fmt: off
    return {
        "label": "disease label",
        "other": "info"
    }
    # fmt: on


class TestMondoClientExtractData:
    """Make sure the `_extract_data` static method works as expected.

    This class contains tests for various scenarios when extracting data from Mondo API
    responses.
    """

    @pytest.mark.unit
    def test_extract_data_success(
        self, json_data_valid: dict, expected_extracted_data: dict
    ) -> None:
        """Test successful data extraction from a valid response."""
        actual_extracted_data = MondoClient._extract_data(json_data_valid)  # noqa: SLF001 (We want to access the private member to test it.)
        assert actual_extracted_data == expected_extracted_data

    @pytest.mark.unit
    def test_extract_data_no_embedded(self, json_data_no_embedded: dict) -> None:
        """Test handling of responses missing the `_embedded` key."""
        extracted = MondoClient._extract_data(json_data_no_embedded)  # noqa: SLF001 (We want to access the private member to test it.)
        assert extracted is None

    @pytest.mark.unit
    def test_extract_data_no_terms(self, json_data_no_terms: dict) -> None:
        """Test handling of responses missing the `terms` list in `_embedded`."""
        extracted = MondoClient._extract_data(json_data_no_terms)  # noqa: SLF001 (We want to access the private member to test it.)
        assert extracted is None

    @pytest.mark.unit
    def test_extract_data_empty_terms(self, json_data_empty_terms: dict) -> None:
        """Test handling of responses with an empty `terms` list."""
        extracted = MondoClient._extract_data(json_data_empty_terms)  # noqa: SLF001 (We want to access the private member to test it.)
        assert extracted is None


@pytest.fixture
def mondo_id() -> str:
    """Return a Mondo ID to be used in tests."""
    return "MONDO_0000001"


@pytest.fixture
def mock_response_valid_data(json_data_valid: dict) -> Mock:
    """Return a mocked response from the Mondo API with valid data."""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = json_data_valid
    return mock_response


@pytest.fixture
def mock_response_invalid_data(json_data_no_embedded: dict) -> Mock:
    """Return a mocked response from the Mondo API with invalid data."""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = json_data_no_embedded
    return mock_response


@pytest.fixture
def mock_client_valid_data(
    mock_response_valid_data: Mock, mondo_id: str
) -> MondoClient:
    """Return a `MondoClient` whose response has valid data."""
    mock_http_client = Mock(spec=HTTPClient)
    mock_http_client.get.return_value = mock_response_valid_data
    client = MondoClient(mondo_id=mondo_id)
    client._http_client = mock_http_client  # noqa: SLF001 (We want to access the private member to inject the mock client.)
    return client


@pytest.fixture
def mock_client_invalid_data(
    mock_response_invalid_data: Mock, mondo_id: str
) -> MondoClient:
    """Return a `MondoClient` whose response has invalid data."""
    mock_http_client = Mock(spec=HTTPClient)
    mock_http_client.get.return_value = mock_response_invalid_data
    client = MondoClient(mondo_id=mondo_id)
    client._http_client = mock_http_client  # noqa: SLF001 (We want to access the private member to inject the mock client.)
    return client


@pytest.fixture
def mock_client_http_error(mondo_id: str) -> MondoClient:
    """Return a `MondoClient` that raises an HTTP error."""
    mock_http_client = Mock(spec=HTTPClient)
    mock_http_client.get.side_effect = EntityClientError("HTTP Error")
    client = MondoClient(mondo_id=mondo_id)
    client._http_client = mock_http_client  # noqa: SLF001 (We want to access the private member to inject the mock client.)
    return client


class TestMondoClient:
    """Make sure `MondoClient` works as expected.

    This class tests initialization, data fetching, and data population.
    """

    @pytest.mark.unit
    def test_initialization(self, mondo_id: str) -> None:
        """Test proper initialization of `MondoClient`."""
        client = MondoClient(mondo_id=mondo_id)
        assert client.base_url == MondoConstants.API_URL
        assert client.mondo_id == mondo_id
        assert client._data is None  # noqa: SLF001 (We want to access the private member to test it.)
        assert client.label is None

    @pytest.mark.unit
    def test_fetch_success(
        self, mock_client_valid_data: Mock, expected_extracted_data: dict
    ) -> None:
        """Test successful API data fetching."""
        client = mock_client_valid_data
        client.fetch()
        assert client.label == expected_extracted_data["label"]

    @pytest.mark.unit
    def test_fetch_failure_request(
        self, mock_client_http_error: MondoClient, mondo_id: str
    ) -> None:
        """Test handling of HTTP request failures."""
        client = mock_client_http_error
        with pytest.raises(MondoClientError) as exc:
            client.fetch()
        error_message = f"Error fetching Mondo data for {mondo_id}"
        assert error_message in str(exc.value)
        assert client._data is None  # noqa: SLF001 (We want to access the private member to test it.)
        assert client.label is None

    @pytest.mark.unit
    def test_fetch_failure_extract_data(
        self, mondo_id: str, mock_client_invalid_data: MondoClient
    ) -> None:
        """Test handling of data extraction failures."""
        client = mock_client_invalid_data
        with pytest.raises(MondoClientError) as exc:
            client.fetch()
        error_message = f"Unable to extract data from Mondo API response for {mondo_id}"
        assert error_message in str(exc.value)
        assert client._data is None  # noqa: SLF001 (We want to access the private member to test it.)
        assert client.label is None
