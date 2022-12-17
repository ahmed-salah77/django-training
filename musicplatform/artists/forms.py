from django import forms

from artists.models import Artist
from django.core.exceptions import ValidationError


class ArtistCreateForm(forms.Form):
    stage_name = forms.CharField()
    social_link = forms.CharField()
    def stage_name(self):
        if Artist.objects.filter(stage_name = self.cleaned_data.get("stage_name")).count() > 0:
            raise ValidationError("This artist already exists")
        else:
            return self.cleaned_data.get("stage_name")