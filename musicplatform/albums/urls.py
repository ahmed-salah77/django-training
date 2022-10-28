from django.urls import path
from . import views
urlpatterns = [
    path('create', views.AlbumView.add_album,name='add_album'),
]