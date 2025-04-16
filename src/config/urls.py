"""Configure URLs for the project."""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # path("", include("apps.curations.urls")),
    # path("", include("apps.diseases.urls")),
    # path("", include("apps.markers.urls")),
    # path("", include("apps.publications.urls")),
    # path("", include("apps.users.urls")),
    path("admin/", admin.site.urls),
]
