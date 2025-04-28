"""Provide views related to PubMed publications."""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from apps.publications.clients.pubmed import PubMedArticleClient
from apps.publications.forms.pubmed import PubMedArticleForm
from apps.publications.selectors.pubmed import PubMedArticleSelector
from apps.publications.services.pubmed import PubMedArticleService


def new_pubmed(request: HttpRequest) -> HttpResponse:
    """Return the new PubMed article form."""
    if request.method == "POST":
        form = PubMedArticleForm(request.POST)
        if form.is_valid():
            pubmed_id = form.cleaned_data["pubmed_id"]
            client = PubMedArticleClient(pubmed_id)
            service = PubMedArticleService(client)
            service.create(pubmed_id)
            return redirect("home")
    else:
        form = PubMedArticleForm()
    return render(request, "publications/pubmed/new.html", {"form": form})


def all_pubmed(request: HttpRequest) -> HttpResponse:
    """Return the all PubMed articles view."""
    query = request.GET.get("q", None)
    selector = PubMedArticleSelector()
    articles = selector.list(query)

    if request.htmx:
        template_name = "publications/includes/pubmed_table.html"
    else:
        template_name = "publications/pubmed/all.html"

    return render(request, template_name, {"articles": articles})
