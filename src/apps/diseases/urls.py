"""Define the URLs for the diseases app."""

from django.urls import path

from apps.diseases.views.mondo import new_disease

urlpatterns = [
    path("mondo/new", new_disease, name="new_disease"),
]
