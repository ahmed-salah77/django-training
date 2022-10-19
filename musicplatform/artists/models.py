from ast import Mod
from email.policy import default
from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Artist(models.Model):
    stage_name = models.CharField(max_length=255,unique=True)
    social_link = models.URLField(max_length=255,default = "")
    approved_albums = models.IntegerField(default = 0)
