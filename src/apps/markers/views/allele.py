"""Provide a view for adding a new allele."""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from apps.markers.clients.allele import AlleleClient
from apps.markers.forms.allele import AlleleForm
from apps.markers.models.allele import Allele


def new_allele(request: HttpRequest) -> HttpResponse:
    """Return the new allele form."""
    if request.method == "POST":
        form = AlleleForm(request.POST)
        if form.is_valid():
            ipd_accession = form.cleaned_data["ipd_accession"]
            client = AlleleClient(ipd_accession)
            Allele.objects.create(ipd_accession=client.ipd_accession, name=client.name)
            return redirect("home")
    else:
        form = AlleleForm()
    return render(request, "markers/allele/new.html", {"form": form})
