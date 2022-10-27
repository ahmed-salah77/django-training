from email.policy import default
from django.utils import timezone
from django.db import models
from imagekit.models import ImageSpecField
from django.core.exceptions import ValidationError

# Create your models here.
                        

class Album(models.Model):
   artist = models.ForeignKey("artists.Artist",related_name='albums' ,on_delete=models.CASCADE)
   name = models.CharField(max_length = 255,default = "New Album")
   created_at = models.DateTimeField(auto_now_add=True)
   release_datetime =  models.DateTimeField()
   cost = models.FloatField()
   is_approved = models.BooleanField(default = False,help_text = "Approve the album if its name is not explicit")
   def __str__(self):
      return self.name
class Song(models.Model):
   album = models.ForeignKey(Album, on_delete=models.CASCADE,related_name = 'songs')
   name = models.CharField(max_length = 255,default = album.name)
   audio = models.FileField(upload_to='songs/',help_text=("Allowed type - .mp3, .wav"))
   image = models.ImageField(upload_to='songs/',default='images/def.jpg')
   def delete(self, *args, **kwargs):
      if Song.objects.filter(album = self.album).count() == 1:
         raise Exception('You can`t delete song "'+ self.name +'" because it`s only song on her album "' + self.album.name+'"')  # or you can throw your custom exception here.
      super(Song, self).delete(*args, **kwargs)
   
      
