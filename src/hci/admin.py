"""Admin config for the HCI."""

# Third-party dependencies:
from django.contrib import admin

# In-house code:
from .models import Curation

# Add models we want to be able to edit in the admin interface.
admin.site.register(Curation)
