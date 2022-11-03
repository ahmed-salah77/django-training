from django.contrib.auth.models import User
from rest_framework import status
from .models import UserProfile
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .serializers import UserProfileSerializer,UserSerializer
from rest_framework.decorators import api_view
from rest_framework.generics import mixins
from rest_framework import generics
@api_view(['GET', 'PUT', 'PATCH'])
def get_user(request,pk):
    try: 
        user = User.objects.get(pk = pk)
        userProfile = UserProfile.objects.get(user=user) 
    except User.DoesNotExist: 
        return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET':
        userProfile_serializer = UserProfileSerializer(userProfile) 
        return JsonResponse(userProfile_serializer.data) 

    if request.method == 'PUT':
        userProfile_serializer = UserProfileSerializer(userProfile, data=request.data) 
        if userProfile_serializer.is_valid(): 
            userProfile_serializer.save() 
            return JsonResponse(userProfile_serializer.data) 
        return JsonResponse(userProfile_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    if request.method == 'PATCH':
        userProfile_serializer = UserProfileSerializer(userProfile, data=request.data) 
        if userProfile_serializer.is_valid(): 
            userProfile_serializer.save() 
            return JsonResponse(userProfile_serializer.data) 
        return JsonResponse(userProfile_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class UserProfileGenerics(generics.UpdateAPIView, generics.ListAPIView):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)



