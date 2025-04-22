"""Provide a view for adding a new PubMed article."""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from apps.publications.forms.pubmed import PubMedArticleForm
from apps.publications.models.pubmed import PubMedArticle
from apps.publications.services.pubmed import PubMedArticleClient


def new_pubmed(request: HttpRequest) -> HttpResponse:
    """Return the new PubMed article form."""
    if request.method == "POST":
        form = PubMedArticleForm(request.POST)
        if form.is_valid():
            pubmed_id = form.cleaned_data["pubmed_id"]
            client = PubMedArticleClient(pubmed_id)
            PubMedArticle.objects.create(pubmed_id=client.pubmed_id, title=client.title)
            return redirect("home")
    else:
        form = PubMedArticleForm()
    return render(request, "publications/pubmed.html", {"form": form})
