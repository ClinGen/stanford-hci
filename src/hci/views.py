"""Views for the HCI."""

# Third-party dependencies:
from django.http import HttpResponse


def index(request):
    """Show basic info at the index route."""
    return HttpResponse("HCI Index")
