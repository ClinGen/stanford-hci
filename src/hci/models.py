"""This module contains ORM models of the data in the HCI."""

from django.contrib.auth.models import User
from django.db import models

DECIMAL_PLACES = 5
DECIMAL_MAX_DIGITS = 5


class Disease(models.Model):
    """A disease is uniquely identified by its Mondo ID.

    The Mondo Disease Ontology (Mondo) aims to harmonize disease definitions across the
    world. A Mondo ID is a unique identifier for a disease. For more information, see:
    https://mondo.monarchinitiative.org
    """

    mondo_id: models.CharField = models.CharField()


class Allele(models.Model):
    """An allele is one of two or more versions of DNA sequence (a single base
    or a segment of bases) at a given genomic location. For more information,
    see:
    https://www.genome.gov/genetics-glossary/Allele

    An allele is uniquely identified by its IPD-IMGT/HLA name. For more
    information, see:
    https://www.ebi.ac.uk/ipd/imgt/hla
    """

    imgt_name: models.CharField = models.CharField()
    car_id: models.CharField = models.CharField()


class Haplotype(models.Model):
    """A haplotype is a physical grouping of genomic variants (or
    polymorphisms) that tend to be inherited together. A specific haplotype
    typically reflects a unique combination of variants that reside near each
    other on a chromosome. For more information,
    see:
    https://www.genome.gov/genetics-glossary/haplotype

    A haplotype is characterized by its chromosome mapping order and its
    constituent alleles.
    """

    chromosome_mapping_order: models.CharField = models.CharField()
    constituent_alleles: models.ManyToManyField = models.ManyToManyField(Allele)


class Publication(models.Model):
    """A publication is a scientific article.

    A publication is uniquely identified by its ID and type. For example, a PubMed
    publication has a PubMed ID, and a "pubmed" type.
    """

    publication_id: models.CharField = models.CharField()
    publication_type: models.CharField = models.CharField()
    author: models.CharField = models.CharField()
    year: models.CharField = models.CharField()
    title: models.CharField = models.CharField()


class Curator(models.Model):
    """A curator is a user with an affiliation."""

    affiliation_id: models.IntegerField = models.IntegerField()
    user: models.OneToOneField = models.OneToOneField(User, on_delete=models.CASCADE)


class Association(models.Model):
    """An association is a relationship between a disease and an allele."""

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
    """A classification is a set of associations for a given publication."""

    publication: models.ForeignKey = models.ForeignKey(
        Publication, on_delete=models.PROTECT
    )
    curator: models.ForeignKey = models.ForeignKey(Curator, on_delete=models.PROTECT)
    association: models.ManyToManyField = models.ManyToManyField(Association)


class Curation(models.Model):
    """A curation is a set of classifications for a given disease and allele or
    haplotype."""

    disease: models.ForeignKey = models.ForeignKey(Disease, on_delete=models.PROTECT)
    allele: models.ForeignKey = models.ForeignKey(Allele, on_delete=models.PROTECT)
    haplotype: models.ForeignKey = models.ForeignKey(
        Haplotype, on_delete=models.PROTECT
    )
    classifications: models.ManyToManyField = models.ManyToManyField(Classification)
