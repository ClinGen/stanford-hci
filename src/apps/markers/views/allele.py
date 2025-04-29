"""Provide a view for adding a new allele."""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from apps.markers.clients.allele import AlleleClient
from apps.markers.forms.allele import AlleleForm
from apps.markers.services.allele import AlleleService
from base.views import EntityView


class AlleleView(EntityView):
    """Create, view all, or view an allele."""

    def new(self, request: HttpRequest) -> HttpResponse:
        """Return the view that provides a form that creates an allele."""
        if request.method == "POST":
            form = AlleleForm(request.POST)
            if form.is_valid():
                ipd_accession = form.cleaned_data["ipd_accession"]
                client = AlleleClient(ipd_accession)
                service = AlleleService(client)
                service.create(ipd_accession)
                return redirect("home")
        else:
            form = AlleleForm()
        return render(request, "markers/allele/new.html", {"form": form})

    def list(self, request: HttpRequest) -> None:
        """Return the searchable table page for an allele."""

    def details(self, request: HttpRequest, ipd_accession: str) -> None:
        """Return the details page for an allele."""
