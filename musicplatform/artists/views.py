from django.shortcuts import render
from .forms import ArtistForm
from .models import Artist
from albums.models import Album
# Create your views here.

def add_artist(request):
    form = ArtistForm()
    if(request.method == 'POST'):
        form = ArtistForm(request.POST)
        if(form.is_valid()):
            form.save()          
    context = {'form':form}
    return render(request,'artists/add_artist.html',context)
def view_artists(request):
    artists = Artist.objects.all()
    albums=Album.objects.all()
    print(albums)
    args = {'artists':artists,'albums':albums}
    return render(request,'artists/view_artists.html',args)
