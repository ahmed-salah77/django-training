from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import ArtistSerializer
from .forms import ArtistForm
from .models import Artist
from albums.models import Album
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

class ArtistView(View):
    @login_required(login_url='login')
    def add_artist(request):
        form = ArtistForm()
        if(request.method == 'POST'):
            form = ArtistForm(request.POST)
            if(form.is_valid()):
                form.save()
                messages.success(request, 'Artist added successfuly')          
        context = {'form':form}
        return render(request,'artists/add_artist.html',context)
    
    def view_artists(request):
        artists = Artist.objects.all()
        albums=Album.objects.all()
        args = {'artists':artists,'albums':albums}
        return render(request,'artists/view_artists.html',args)
    
    @csrf_exempt
    def artists_list(request):
        if request.method == 'GET':
            snippets = Artist.objects.all()
            serializer = ArtistSerializer(snippets, many=True)
            return JsonResponse(serializer.data, safe=False)

        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = ArtistSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)