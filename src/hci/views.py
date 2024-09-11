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
        "affiliation": "HLA Expert Panel",
        "username": request.user.username,
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
    context = {"email": request.user.email, "affiliation": "HLA Expert Panel"}
    return render(request, "hci/affiliation.html", context)


@login_required
def new_curation_view(request):
    """Show the new curation page."""
    context = {"email": request.user.email, "affiliation": "HLA Expert Panel"}
    return render(request, "hci/new_curation.html", context)


@login_required
def new_disease_view(request):
    """Show the new curation page."""
    context = {"email": request.user.email, "affiliation": "HLA Expert Panel"}
    return render(request, "hci/new_disease.html", context)


@login_required
def new_allele_haplotype_view(request):
    """Show the new curation page."""
    context = {"email": request.user.email, "affiliation": "HLA Expert Panel"}
    return render(request, "hci/new_allele_haplotype.html", context)


@login_required
def new_publication_view(request):
    """Show the new curation page."""
    context = {"email": request.user.email, "affiliation": "HLA Expert Panel"}
    return render(request, "hci/new_publication.html", context)
