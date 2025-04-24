"""Test the allele service."""

import pytest

from apps.markers.clients.allele import AlleleClient


@pytest.mark.contract
def test_client() -> None:
    """Make sure we can get info about an allele from IPD."""
    accession = "HLA00902"
    name = "DRB3*03:01:01:01"
    version = "3.60.0"
    allele = AlleleClient(accession)
    assert allele.name == name
    assert allele.version == version
