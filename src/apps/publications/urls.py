"""Define the URLs for the publications app."""

from django.urls import path

from apps.publications.views.pubmed import new_pubmed

urlpatterns = [
    path("pubmed/new", new_pubmed, name="new_pubmed"),
]
