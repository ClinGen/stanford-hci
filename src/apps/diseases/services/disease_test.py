"""Test the disease service."""

from apps.diseases.services.disease import DiseaseClient


def test_client() -> None:
    """Test the client."""
    mondo_id = "0005052"
    label = "irritable bowel syndrome"
    disease = DiseaseClient(mondo_id)
    assert disease.label == label
