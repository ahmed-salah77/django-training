from django.forms import ModelForm
from .models import Artist
from django import forms

class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        fields ='__all__'
    def clean_stage_name(self):
        artists = Artist.objects.all();
        for artist in artists:
            if(artist.stage_name == self.cleaned_data.get('stage_name')):
                raise forms.ValidationError("this stage name of the artist already exist")
        return self.cleaned_data.get('stage_name')