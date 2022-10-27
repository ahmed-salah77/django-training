from django.shortcuts import render
from .forms import AlbumForm
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
class AlbumView(View):
    @login_required(login_url='login')
    def add_album(request):
        form = AlbumForm()
        if(request.method == 'POST'):
            form = AlbumForm(request.POST)
            if(form.is_valid()):
                form.save()          
                messages.success(request, 'Album added successfuly')          
        context = {'form':form}
        return render(request,'albums/add_album.html',context)
