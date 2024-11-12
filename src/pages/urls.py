from django.urls import include
from django.urls import path

from pages import views

urlpatterns = [
    # Pages:
    path("", views.home, name="home"),
    path(
        "allele_haplotype/new/",
        views.new_allele_haplotype,
        name="new_allele_haplotype",
    ),
    path("curation/new/", views.new_curation, name="new_curation"),
    path("disease/new/", views.new_disease, name="new_disease"),
    path("publication/new/", views.new_publication, name="new_publication"),
    # Login/logout:
    path("accounts/", include("django.contrib.auth.urls")),
]
