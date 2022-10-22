from xml.etree.ElementInclude import include
from django.contrib import admin
from django import forms
from .models import Artist
from albums.models import Album
# Register your models here.
def add_albums(modeladmin, request, queryset):
    print('here')
class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['stage_name','social_link']

class ArtistAdmin(admin.ModelAdmin):
    list_display = ('stage_name','approved_albums')
    def approved_albums(self, obj):
        return obj.albums.filter(is_approved = True).count();
    form = ArtistForm
    actions =[add_albums]
admin.site.register(Artist,ArtistAdmin)
