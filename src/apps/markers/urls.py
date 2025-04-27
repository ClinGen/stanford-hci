"""Define the URLs for the markers app."""

from django.urls import path

from apps.markers.views.allele import new_allele

urlpatterns = [
    path("allele/new", new_allele, name="new_allele"),
]
