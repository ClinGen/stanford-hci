"""Define the URLs for the publications app."""

from django.urls import path

from apps.publications.views.all_pubmed import all_pubmed
from apps.publications.views.new_pubmed import new_pubmed

urlpatterns = [
    path("pubmed/all", all_pubmed, name="all_pubmed"),
    path("pubmed/new", new_pubmed, name="new_pubmed"),
]
