from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArtistView.artists_list,name='artists'),
    #path('', views.ArtistView.view_artists,name='artists'),
    path('create', views.ArtistView.add_artist,name='add_artist'),
]