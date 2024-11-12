# Third-party dependencies:
from django.urls import path, include

# In-house code:
from pages import views
urlpatterns = [
    # Pages:
    path("", views.home, name="home"),
    # Login/logout:
    path("accounts/", include("django.contrib.auth.urls")),
]
