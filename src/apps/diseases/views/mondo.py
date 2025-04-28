"""Provide a view for adding a new disease."""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from apps.diseases.clients.mondo import MondoClient
from apps.diseases.forms.disease import DiseaseForm
from apps.diseases.services.mondo import MondoService
from constants import MondoConstants


def new_disease(request: HttpRequest) -> HttpResponse:
    """Return the new disease form."""
    if request.method == "POST":
        form = DiseaseForm(request.POST)
        if form.is_valid():
            mondo_id = form.cleaned_data["mondo_id"]
            client = MondoClient(mondo_id)
            service = MondoService(client)
            service.create(mondo_id)
            return redirect("home")
    else:
        form = DiseaseForm()
    return render(
        request,
        "diseases/mondo/new.html",
        {"form": form, "mondo_search_url": MondoConstants.SEARCH_URL},
    )
