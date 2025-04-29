"""Provide views for PubMed publications."""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from apps.publications.clients.pubmed import PubMedArticleClient
from apps.publications.forms.pubmed import PubMedArticleForm
from apps.publications.selectors.pubmed import PubMedArticleSelector
from apps.publications.services.pubmed import PubMedArticleService
from base.views import EntityView


class PubMedView(EntityView):
    """Create, view all, or view a PubMed publication."""

    def new(self, request: HttpRequest) -> HttpResponse:
        """Return the view that provides a form that creates a PubMed publication."""
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

    def list(self, request: HttpRequest) -> HttpResponse:
        """Return the searchable table page for a PubMed publication."""
        query = request.GET.get("q", None)
        selector = PubMedArticleSelector()
        articles = selector.list(query)

        if request.htmx:
            template_name = "publications/includes/pubmed_table.html"
        else:
            template_name = "publications/pubmed/all.html"

        return render(request, template_name, {"articles": articles})

    def details(self, request: HttpRequest, pubmed_id: str) -> HttpResponse:
        """Return the details page for a PubMed publication."""
