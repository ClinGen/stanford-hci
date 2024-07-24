"""URL patterns for the HCI."""

# Third-party dependencies:
from django.urls import path, include

# In-house code:
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("accounts/", include("django.contrib.auth.urls")),
]
