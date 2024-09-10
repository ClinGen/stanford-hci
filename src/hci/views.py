"""Views for the HCI."""

# Third-party dependencies:
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


@login_required
def index_view(request):
    """Show basic info at the index route."""
    context = {
        "email": request.user.email,
        "affiliation": "HLA Expert Panel"
    }
    return render(request, "hci/index.html", context)


@login_required
def logout_view(request):
    """Log the user out."""
    logout(request)
    return redirect(index_view)


@login_required
def affiliation_view(request):
    """Show the user the affiliation configuration page."""
    context = {
        "email": request.user.email,
        "affiliation": "HLA Expert Panel"
    }
    return render(request, "hci/affiliation.html", context)
