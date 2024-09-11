"""URL patterns for the HCI."""

# Third-party dependencies:
from django.urls import path, include

# In-house code:
from . import views

urlpatterns = [
    # One-off pages:
    path("", views.index_view, name="index"),
    path("affiliation/", views.affiliation_view, name="affiliation"),
    # Login/logout:
    path("accounts/", include("django.contrib.auth.urls")),
    path("logout/", views.logout_view, name="custom_logout"),
    # "New" pages:
    path(
        "allele_haplotype/new/",
        views.new_allele_haplotype_view,
        name="new_allele_haplotype",
    ),
    path("curation/new/", views.new_curation_view, name="new_curation"),
    path("disease/new/", views.new_disease_view, name="new_disease"),
    path("publication/new/", views.new_publication_view, name="new_publication"),
]
