import imp
from django.shortcuts import render
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
