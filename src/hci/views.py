"""This module defines the views for the various pages of the HCI."""

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render


def home(request):
    """This is the view for the main page of the HCI.

    The home page can be thought of as the main hub of the HCI. It is where the user can
    view their curations and their affiliation's curations. It also has links to the
    other pages of the HCI.
    """
    if request.user.is_authenticated:
        context = {
            "is_authenticated": True,
            "email": request.user.email,
            "affiliation": "HLA Expert Panel",
            "username": request.user.username,
        }
    else:
        context = {
            "is_authenticated": False,
        }
    return render(request, "hci/home.html", context)


@login_required
def custom_logout(request):
    """This view logs the user out and redirects them to the home page."""
    logout(request)
    return redirect(home)


@login_required
def affiliation(request):
    """The affiliation page allows the user to configure their affiliation."""
    context = {"email": request.user.email, "affiliation": "HLA Expert Panel"}
    return render(request, "hci/affiliation.html", context)


@login_required
def new_curation(request):
    """The new curation page allows the user to start a new curation."""
    context = {"email": request.user.email, "affiliation": "HLA Expert Panel"}
    return render(request, "hci/new_curation.html", context)


@login_required
def new_disease(request):
    """The new disease page allows the user to add a new disease to the HCI."""
    context = {"email": request.user.email, "affiliation": "HLA Expert Panel"}
    return render(request, "hci/new_disease.html", context)


@login_required
def new_allele_haplotype(request):
    """The new allele/haplotype allows the user to add a new allele/haplotype to the
    HCI."""
    context = {"email": request.user.email, "affiliation": "HLA Expert Panel"}
    return render(request, "hci/new_allele_haplotype.html", context)


@login_required
def new_publication(request):
    """The new publication page allows the user to add a new publication to the HCI."""
    context = {"email": request.user.email, "affiliation": "HLA Expert Panel"}
    return render(request, "hci/new_publication.html", context)
