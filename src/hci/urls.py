"""URL patterns for the HCI."""

# Third-party dependencies:
from django.urls import path, include

# In-house code:
from . import views

urlpatterns = [
    path("", views.index_view, name="index"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("affiliation/", views.affiliation_view, name="affiliation"),
    path("logout/", views.logout_view, name="custom_logout"),
]
