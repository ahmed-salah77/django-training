from django.utils import timezone
from django.db import models

# Create your models here.
class Album(models.Model):
   artist = models.ForeignKey("artists.Artist",related_name='albums' ,on_delete=models.CASCADE)
   name = models.CharField(max_length = 255,default = "New Album")
   creation_datetime =  models.DateTimeField(default = timezone.now)
   release_datetime =  models.DateTimeField()
   cost = models.FloatField()