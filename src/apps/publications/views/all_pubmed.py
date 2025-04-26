"""Provide a view that shows all PubMed articles."""

from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from apps.publications.models.pubmed import PubMedArticle


def all_pubmed(request: HttpRequest) -> HttpResponse:
    """Return the all PubMed articles view."""
    query = request.GET.get("q", "")
    articles = PubMedArticle.objects.filter(
        Q(pubmed_id__icontains=query) | Q(title__icontains=query)
    )

    if request.htmx:
        template_name = "includes/pubmed_table.html"
    else:
        template_name = "publications/pubmed/all.html"

    return render(request, template_name, {"articles": articles})
