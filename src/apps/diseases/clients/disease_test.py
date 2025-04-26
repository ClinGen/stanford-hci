"""Test the disease service."""

import pytest

from apps.diseases.clients.disease import DiseaseClient


@pytest.mark.contract
def test_client() -> None:
    """Test the client."""
    mondo_id = "MONDO_0005052"
    label = "irritable bowel syndrome"
    disease = DiseaseClient(mondo_id)
    assert disease.label == label
