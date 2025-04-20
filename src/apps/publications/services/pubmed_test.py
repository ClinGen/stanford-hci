"""Test PubMed services."""

from apps.publications.services.pubmed import PubMedArticleClient


def test_client() -> None:
    """Make sure we can get article info from PubMed."""
    pmid = "10446108"
    title = "HLA-DR and -DQ phenotypes in inflammatory bowel disease: a meta-analysis."
    article = PubMedArticleClient(pmid)
    assert isinstance(article.title, str)
    assert article.title == title
