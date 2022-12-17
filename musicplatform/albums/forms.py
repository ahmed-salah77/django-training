from django.forms import ModelForm
from .models import Album
from .models import Song
class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields ='__all__'
    
class SongForm(ModelForm):
    class Meta:
        model = Song
        fields ='__all__'

  
