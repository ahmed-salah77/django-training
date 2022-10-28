from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('users/', include('users.urls')),
    path('admin/', admin.site.urls),
    path('artists/', include('artists.urls')),
    path('albums/', include('albums.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
