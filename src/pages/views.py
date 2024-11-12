"""This module defines the views for the various pages of the HCI."""

# Third-party dependencies:
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def home(request):
    """This is the view for the main page of the HCI.

    The home page can be thought of as the main hub of the HCI. It is where the
    user can view their curations and their affiliation's curations. It also
    has links to the other pages of the HCI.
    """
    return render(request, "pages/home.html")
