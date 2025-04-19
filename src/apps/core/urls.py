"""Define the URLs for the core app."""

from django.urls import path

from apps.core.views.home import home

urlpatterns = [
    path("", home, name="home"),
]
