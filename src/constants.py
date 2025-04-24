"""Provide constants used in the project.

We organize constants into classes to keep things organized. The classes themselves
should be sorted alphabetically. Within each class, the constants should be sorted
alphabetically.
"""


class AffiliationsConstants:
    """Define constants related to affiliations."""

    DEFAULT_ID = "10119"
    DEFAULT_NAME = "HLA Expert Panel"
    MAX_LENGTH_ID = 5


class IPDConstants:
    """Define constants related to the IPD-IMGT/HLA Database."""

    API_URL = "https://www.ebi.ac.uk/cgi-bin/ipd/api/allele"


class ModelsConstants:
    """Define constants related to models."""

    MAX_LENGTH_NAME = 255


class MondoConstants:
    """Define constants related to the Mondo Disease Ontology."""

    API_URL = "https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms"
    IRI = "http://purl.obolibrary.org/obo"
    SEARCH_URL = "https://www.ebi.ac.uk/ols4/ontologies/mondo"


class PubMedConstants:
    """Define constants related to PubMed."""

    API_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"


class RequestsConstants:
    """Define constants related to the requests library."""

    DEFAULT_TIMEOUT = 5  # In seconds.
