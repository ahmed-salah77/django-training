from django.urls import path,include
from . import views
urlpatterns = [
    path('create', views.AlbumView.add_album,name='add_album'),
]