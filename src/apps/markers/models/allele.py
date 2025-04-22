"""Provide a model for alleles."""

from django.db import models


class Allele(models.Model):
    """An allele is one of two or more versions of DNA sequence at a given location.

    For more information on alleles, see:
    https://www.genome.gov/genetics-glossary/Allele.

    An allele is uniquely identified by its IPD-IMGT/HLA name. For more
    information on IPD-IMGT, see:
    https://www.ebi.ac.uk/ipd/imgt/hla
    """

    name: models.CharField = models.CharField(verbose_name="IPD-IMGT Name")
    ipd_accession: models.CharField = models.CharField(
        verbose_name="IPD Accession",
        help_text="A unique identifier for the allele, e.g. HLA00902.",
    )

    class Meta:
        """Define metadata options."""

        verbose_name = "Allele"
        verbose_name_plural = "Alleles"

    def __str__(self) -> str:
        """Return a string representation of the allele."""
        return f"{self.name} ({self.ipd_accession})"
