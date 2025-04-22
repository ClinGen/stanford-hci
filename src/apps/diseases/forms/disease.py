"""Provide a form for adding a disease to the database."""

from django.forms import ModelForm

from apps.diseases.models.disease import Disease


class DiseaseForm(ModelForm):
    """Add a disease to the database."""

    class Meta:
        """Define metadata options."""

        model = Disease
        fields = ["mondo_id"]
