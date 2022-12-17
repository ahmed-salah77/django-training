from django.contrib import admin
from .models import Album
from .models import Song
from django.core.exceptions import ValidationError
from django import forms
from .forms import SongForm
class SongAdmin(admin.ModelAdmin):
    exclude = ['']
    form = SongForm

class AlbumInlineFormset(forms.models.BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            try:
                if form.cleaned_data:
                    count += 1
            except AttributeError:
                pass
        if count < 1:
            raise forms.ValidationError('Album must have at least one song')

class AlbumInline(admin.StackedInline):
    model = Song    
    exclude = ['']
    formset = AlbumInlineFormset

class AlbumAdmin(admin.ModelAdmin):
    exclude = ['']
    inlines= (AlbumInline,)
    def clean(self):
        raise ValidationError("Album should has atleast one song")

admin.site.register(Album,AlbumAdmin)
admin.site.register(Song,SongAdmin)
