"""Define views for the HCI."""

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from hci.forms import CustomSignUpForm


def signup(request: HttpRequest) -> HttpResponse:
    """Provide the signup form for new users."""
    if request.method == "POST":
        form = CustomSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = CustomSignUpForm()
    return render(request, "registration/signup.html", {"form": form})


def home(request: HttpRequest) -> HttpResponse:
    """View the home page of the HCI.

    The home page can be thought of as the main hub of the HCI. It is where the user can
    view their curations and their affiliation's curations. It also has links to the
    other pages of the HCI.
    """
    if request.user.is_authenticated and isinstance(request.user, User):
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
def custom_logout(request: HttpRequest) -> HttpResponse:
    """Log the user out and redirect them to the home page."""
    logout(request)
    return redirect(home)


@login_required
def affiliation(request: HttpRequest) -> HttpResponse:
    """Allow the user to configure their affiliation."""
    if isinstance(request.user, User):
        context = {"email": request.user.email, "affiliation": "HLA Expert Panel"}
    else:
        context = {"affiliation": "HLA Expert Panel"}
    return render(request, "hci/affiliation.html", context)


def all_curations(request: HttpRequest) -> HttpResponse:
    """Allow the user to browse existing curations."""
    return render(request, "hci/all_curations.html")


@login_required
def new_curation(request: HttpRequest) -> HttpResponse:
    """Allow the user to start a new curation."""
    if isinstance(request.user, User):
        context = {"email": request.user.email, "affiliation": "HLA Expert Panel"}
    else:
        context = {"affiliation": "HLA Expert Panel"}
    return render(request, "hci/new_curation.html", context)


@login_required
def new_disease(request: HttpRequest) -> HttpResponse:
    """Allow the user to add a new disease to the HCI."""
    if isinstance(request.user, User):
        context = {"email": request.user.email, "affiliation": "HLA Expert Panel"}
    else:
        context = {"affiliation": "HLA Expert Panel"}
    return render(request, "hci/new_disease.html", context)


@login_required
def new_allele_haplotype(request: HttpRequest) -> HttpResponse:
    """Allow the user to add a new allele/haplotype to the HCI."""
    if isinstance(request.user, User):
        context = {"email": request.user.email, "affiliation": "HLA Expert Panel"}
    else:
        context = {"affiliation": "HLA Expert Panel"}
    return render(request, "hci/new_allele_haplotype.html", context)


@login_required
def new_publication(request: HttpRequest) -> HttpResponse:
    """Allow the user to add a new publication to the HCI."""
    if isinstance(request.user, User):
        context = {"email": request.user.email, "affiliation": "HLA Expert Panel"}
    else:
        context = {"affiliation": "HLA Expert Panel"}
    return render(request, "hci/new_publication.html", context)
