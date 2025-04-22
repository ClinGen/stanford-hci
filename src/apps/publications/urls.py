"""Define the URLs for the publications app."""

from django.urls import path

from apps.publications.views.pubmed import new_pubmed_article

urlpatterns = [
    path("pubmed/new", new_pubmed_article, name="new_pubmed_article"),
]
