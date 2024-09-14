"""Models of the data in the HCI."""

# Third-party dependencies:
from django.contrib.auth.models import User
from django.db import models

# Constants:
DECIMAL_PLACES = 5
DECIMAL_MAX_DIGITS = 5


class Disease(models.Model):
    """Define the shape of a disease."""

    mondo_id: models.CharField = models.CharField()


class Allele(models.Model):
    """Define the shape of an allele."""

    imgt_name: models.CharField = models.CharField()
    car_id: models.CharField = models.CharField()


class Haplotype(models.Model):
    """Define the shape of a haplotype."""

    chromosome_mapping_order: models.CharField = models.CharField()
    constituent_alleles: models.ManyToManyField = models.ManyToManyField(Allele)


class Publication(models.Model):
    """Define the shape of a publication."""

    publication_id: models.CharField = models.CharField()
    publication_type: models.CharField = models.CharField()
    author: models.CharField = models.CharField()
    year: models.CharField = models.CharField()
    title: models.CharField = models.CharField()


class Curator(models.Model):
    """Define the shape of curator."""

    affiliation_id: models.IntegerField = models.IntegerField()
    affiliation_name: models.CharField = models.CharField()
    user: models.OneToOneField = models.OneToOneField(User, on_delete=models.CASCADE)


class Association(models.Model):
    """Define the shape of an association."""

    # Study info:
    study_type: models.CharField = models.CharField()
    cohort_type: models.CharField = models.CharField()
    label: models.CharField = models.CharField()

    allele_field_resolution: models.CharField = models.CharField()
    is_haplotype: models.BooleanField = models.BooleanField()
    zygosity: models.CharField = models.CharField()

    # Allele identification methods:
    allele_name_in_publication: models.CharField = models.CharField()
    serological: models.BooleanField = models.BooleanField()
    imputation: models.BooleanField = models.BooleanField()
    array_data: models.BooleanField = models.BooleanField()
    low_resolution_typing_ssop: models.BooleanField = models.BooleanField()
    sanger_sequencing: models.BooleanField = models.BooleanField()
    whole_exome_sequencing: models.BooleanField = models.BooleanField()
    whole_genome_sequencing: models.BooleanField = models.BooleanField()
    high_resolution_typing: models.BooleanField = models.BooleanField()
    other: models.BooleanField = models.BooleanField()
    unknown: models.BooleanField = models.BooleanField()
    reference_panel: models.TextField = models.TextField()
    typing_methods_description: models.TextField = models.TextField()

    # Demographic info (phenotypes):
    phenotypes_in_common: models.CharField = models.CharField()
    common_free_text: models.TextField = models.TextField()
    not_phenotypes: models.CharField = models.CharField()
    not_phenotypes_free_text: models.TextField = models.TextField()
    age_range_type: models.CharField = models.CharField()
    age_range_value_from: models.PositiveIntegerField = models.PositiveIntegerField()
    age_range_value_to: models.PositiveIntegerField = models.PositiveIntegerField()
    age_range_unit: models.CharField = models.CharField()

    # Demographic info (ancestry):
    reported_ancestry: models.CharField = models.CharField()
    biogeographical_category: models.CharField = models.CharField()
    country_or_countries: models.CharField = models.CharField()
    num_males: models.PositiveIntegerField = models.PositiveIntegerField()
    num_females: models.PositiveIntegerField = models.PositiveIntegerField()

    # Statistics (power):
    num_cases_with_variant: models.PositiveIntegerField = models.PositiveIntegerField()
    num_cases_genotyped_or_sequenced: models.PositiveIntegerField = (
        models.PositiveIntegerField()
    )
    case_frequency: models.CharField = models.CharField()
    num_controls_with_variant: models.PositiveIntegerField = (
        models.PositiveIntegerField()
    )
    num_controls_genotyped_or_sequenced: models.PositiveIntegerField = (
        models.PositiveIntegerField()
    )
    control_frequency: models.CharField = models.CharField()
    total_cohort_size: models.PositiveIntegerField = models.PositiveIntegerField()

    # Statistics (value):
    test_statistic: models.CharField = models.CharField()
    value: models.IntegerField = models.IntegerField()
    confidence_interval_from: models.IntegerField = models.IntegerField()
    confidence_interval_to: models.IntegerField = models.IntegerField()
    standard_error: models.DecimalField = models.DecimalField(
        decimal_places=DECIMAL_PLACES, max_digits=DECIMAL_MAX_DIGITS
    )

    # Statistics (significance):
    p_value: models.DecimalField = models.DecimalField(
        decimal_places=DECIMAL_PLACES, max_digits=DECIMAL_MAX_DIGITS
    )
    p_value_type: models.CharField = models.CharField()
    is_conditional: models.BooleanField = models.BooleanField()
    condition_on: models.TextField = models.TextField()

    direction_of_effect: models.CharField = models.CharField()
    comments: models.TextField = models.TextField()
    score: models.DecimalField = models.DecimalField(
        decimal_places=DECIMAL_PLACES, max_digits=DECIMAL_MAX_DIGITS
    )


class Classification(models.Model):
    """Define the shape of a classification."""

    publication: models.ForeignKey = models.ForeignKey(
        Publication, on_delete=models.PROTECT
    )
    curator: models.ForeignKey = models.ForeignKey(Curator, on_delete=models.PROTECT)
    association: models.ManyToManyField = models.ManyToManyField(Association)


class Curation(models.Model):
    """Define the shape of an HLA curation."""

    disease: models.ForeignKey = models.ForeignKey(Disease, on_delete=models.PROTECT)
    allele: models.ForeignKey = models.ForeignKey(Allele, on_delete=models.PROTECT)
    haplotype: models.ForeignKey = models.ForeignKey(
        Haplotype, on_delete=models.PROTECT
    )
    classifications: models.ManyToManyField = models.ManyToManyField(Classification)
