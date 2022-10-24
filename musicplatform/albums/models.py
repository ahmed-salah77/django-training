from email.policy import default
from django.utils import timezone
from django.db import models

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
      
