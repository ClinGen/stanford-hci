"""URL patterns for the HCI."""

# Third-party dependencies:
from django.urls import path

# In-house code:
from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
