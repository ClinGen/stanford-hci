"""Configure the admin page for the allele model."""

from django.contrib import admin

from apps.diseases.models.disease import Disease

admin.site.register(Disease)
