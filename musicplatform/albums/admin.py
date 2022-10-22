from django.contrib import admin
from .models import Album

# Register your models here.
class AlbumAdmin(admin.ModelAdmin):
    list_display =('name','is_approved')
admin.site.register(Album,AlbumAdmin)
