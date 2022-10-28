from django.db import models

# Create your models here.

class Artist(models.Model):
    stage_name = models.CharField(max_length=255,unique=True)
    social_link = models.URLField(max_length=255,default = "")
    def __str__(self):
      return self.stage_name
