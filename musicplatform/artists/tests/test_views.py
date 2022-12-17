import pytest
from rest_framework.test import force_authenticate
from rest_framework.test import APIClient
from django.contrib.auth.models import User

@pytest.mark.django_db
class TestAddArtist:

    def test_authenticated_user(self,client):
        user = User.objects.create(username='somone')
        client = APIClient()
        client.force_authenticate(user=user)
        response = client.post('http://127.0.0.1:8000/artists/create/', {"stage_name":"ahmed_123","social_link":"https://www.facebook.com"})
        assert response.status_code == 201

    def test_not_authenticated_user(self,client):
        client = APIClient()
        response = client.post('http://127.0.0.1:8000/artists/create/', {"stage_name":"ahmed_123","social_link":"https://www.facebook.com"})
        assert response.status_code == 401