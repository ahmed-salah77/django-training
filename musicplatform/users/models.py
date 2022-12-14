from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    bio  = models.CharField(max_length = 256,default = "",blank = True)
    def __str__(self):
        return self.user.username

# @receiver(post_save,sender=User)
# def create_user_profile(sender,instance,created,**kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)

        