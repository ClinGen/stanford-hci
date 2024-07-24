"""Models of the data in the HCI."""

# Third-party dependencies:
from django.db import models


class Curation(models.Model):
    """Define the shape of an HLA curation."""

    disease: models.CharField = models.CharField()
    hla_allele: models.CharField = models.CharField()
