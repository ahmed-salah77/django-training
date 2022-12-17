from telnetlib import STATUS
from django.shortcuts import HttpResponse, render, redirect
from requests import Response
from .forms import ArtistCreateForm
from django.views.decorators.csrf import csrf_protect
from .models import Artist
from django.core.exceptions import ValidationError
from django.contrib import messages, contenttypes
from rest_framework import generics, permissions
from .serializers import ArtistSerializerCreation, ArtistSerializerView

# Create your views here.

class ArtistCreate(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ArtistSerializerCreation
    queryset = Artist.objects.all()

class ArtistView(generics.ListAPIView):
    
    serializer_class = ArtistSerializerView
    queryset = Artist.objects.all()
    