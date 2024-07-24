"""Views for the HCI."""

# Third-party dependencies:
from django.shortcuts import render


def index(request):
    """Show basic info at the index route."""
    return render(request, "hci/index.html")
