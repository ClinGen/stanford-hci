"""Provide a view for adding a new disease."""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from apps.diseases.clients.disease import DiseaseClient
from apps.diseases.forms.disease import DiseaseForm
from apps.diseases.models.disease import Disease
from constants import MondoConstants


def new_disease(request: HttpRequest) -> HttpResponse:
    """Return the new disease form."""
    if request.method == "POST":
        form = DiseaseForm(request.POST)
        if form.is_valid():
            mondo_id = form.cleaned_data["mondo_id"]
            client = DiseaseClient(mondo_id)
            Disease.objects.create(mondo_id=client.mondo_id, label=client.label)
            return redirect("home")
    else:
        form = DiseaseForm()
    return render(
        request,
        "diseases/disease.html",
        {"form": form, "mondo_search_url": MondoConstants.SEARCH_URL},
    )
