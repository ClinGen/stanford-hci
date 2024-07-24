"""Views for the HCI."""

# Third-party dependencies:
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    """Show basic info at the index route."""
    return render(request, "hci/index.html")
