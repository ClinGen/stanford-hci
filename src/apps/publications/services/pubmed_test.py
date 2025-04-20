"""Test PubMed services."""

from apps.publications.services.pubmed import PubMedArticleClient


def test_get_article_info() -> None:
    """Make sure we can get article info from PubMed."""
    pmid = "37704778"
    article = PubMedArticleClient(pmid)
    assert isinstance(article.title, str)
