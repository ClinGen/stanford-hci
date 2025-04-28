"""Provide services for alleles."""

from apps.markers.clients.allele import AlleleClient
from apps.markers.models import Allele
from base.services import EntityService


class AlleleServiceError(Exception):
    """Raise when an allele service encounters an error."""


class AlleleService(EntityService):
    """Create or update an allele."""

    def __init__(self, client: AlleleClient) -> None:
        """Set the allele client."""
        self.client = client

    def create(self, ipd_accession: str) -> Allele:
        """Create an allele.

        Args:
             ipd_accession: The IPD-IMGT accession, e.g., HLA00902.

        Returns:
            The newly created allele.
        """
        return Allele.objects.create(ipd_accession=ipd_accession, name=self.client.name)

    def update(self, ipd_accession: str, name: str) -> Allele:
        """Update an allele.

        Args:
            ipd_accession: The IPD-IMGT accession, e.g., HLA00902.
            name: The allele name we want to update.

        Raises:
            AlleleServiceError: When the allele to update does not exist.

        Returns:
            The updated allele.
        """
        try:
            allele = Allele.objects.get(ipd_accession=ipd_accession)
            allele.name = name
            allele.save()
        except Allele.DoesNotExist as exc:
            error_message = f"The allele with accession {ipd_accession} does not exist"
            raise AlleleServiceError(error_message) from exc
        return allele
