from .models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from django.http import Http404

class UserProfileGenerics(generics.UpdateAPIView, generics.ListAPIView):
    serializer_class = UserProfileSerializer
    def get_queryset(self):
        try: 
            user = User.objects.get(pk = self.kwargs['pk'])
            userProfile = UserProfile.objects.filter(user = user)
            return userProfile
        except:
            raise Http404  



