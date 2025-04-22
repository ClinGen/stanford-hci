"""Define the URLs for the diseases app."""

from django.urls import path

from apps.diseases.views.disease import new_disease

urlpatterns = [
    path("disease/new", new_disease, name="new_disease"),
]
