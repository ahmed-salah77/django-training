from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.ArtistView.view_artists,name='artists'),
    path('create', views.ArtistView.add_artist,name='add_artist'),
]