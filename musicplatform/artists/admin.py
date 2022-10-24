from xml.etree.ElementInclude import include
from django.contrib import admin
from django import forms
from .models import Artist
from albums.models import Album
# Register your models here.

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['stage_name','social_link']

class ArtistAdmin(admin.ModelAdmin):
    list_display = ['stage_name']
  #  def approved_albums(self, obj):
        # ret = obj.albums.filter(is_approved = True).count();
        # if(ret is None):
        #     ret = 0
   #     return 0;
    form = ArtistForm
admin.site.register(Artist,ArtistAdmin)
