"""Test allele services."""

import pytest

from apps.markers.models.allele import Allele
from apps.markers.services.allele import AlleleService, AlleleServiceError


class MockAlleleClient:
    """Mock the allele client."""

    def __init__(self, ipd_accession: str) -> None:
        """Initialize the mock client."""
        self.ipd_accession = ipd_accession
        self.name = "allele name"


@pytest.mark.component
@pytest.mark.django_db
def test_create_allele() -> None:
    """Make sure we can create an allele."""
    ipd_accession = "HLA00123"
    client = MockAlleleClient(ipd_accession)
    service = AlleleService(client)  # type: ignore (We are using a mock client for our test.)
    allele = service.create(ipd_accession)
    assert allele is not None
    assert allele.ipd_accession == client.ipd_accession
    assert allele.name == client.name


@pytest.mark.component
@pytest.mark.django_db
def test_update_allele() -> None:
    """Make sure we can update an allele."""
    ipd_accession = "HLA00543"
    Allele.objects.create(ipd_accession=ipd_accession, name="allele name")
    client = MockAlleleClient(ipd_accession)
    service = AlleleService(client)  # type: ignore (We are using a mock client for our test.)
    service.update(ipd_accession, "new allele name")
    allele = Allele.objects.get(ipd_accession=ipd_accession)
    assert allele is not None
    assert allele.ipd_accession == client.ipd_accession
    assert allele.name == "new allele name"


@pytest.mark.component
@pytest.mark.django_db
def test_update_non_existent_allele() -> None:
    """Make sure we can't update a non-existent allele."""
    ipd_accession = "HLA00678"
    client = MockAlleleClient(ipd_accession)
    service = AlleleService(client)  # type: ignore (We are using a mock client for our test.)
    with pytest.raises(AlleleServiceError):
        service.update(ipd_accession, "new allele name")
