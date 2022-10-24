from django.shortcuts import render
from .forms import AlbumForm
# Create your views here.

def add_album(request):
    form = AlbumForm()
    if(request.method == 'POST'):
        form = AlbumForm(request.POST)
        if(form.is_valid()):
            form.save()          
    context = {'form':form}
    return render(request,'albums/add_album.html',context)
