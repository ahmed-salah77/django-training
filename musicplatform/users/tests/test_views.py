import pytest
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from users.models import UserProfile
@pytest.mark.django_db
class TestUser(APITestCase):

    def test_get(self):
        user = User.objects.create(username = 'newUser',email='abc@gmail.com')
        user_profile = UserProfile.objects.create(user = user,bio='hello')
        response = self.client.get('/users/1/')
        assert response.status_code == 200 and response.json() == [{"user":{"username":"newUser","email":"abc@gmail.com"},"bio":"hello"}]

    def test_put(self):
        user = User.objects.create(username = 'newUser',email='abc@gmail.com')
        user_profile = UserProfile.objects.create(user = user,bio='hello')
        response = self.client.put('/users/1/',{"user":{"username":"newUser","email":"abc@gmail.com"},"bio":"hello man"})
        assert response.status_code == 200 and response.json() == {"user":{"username":"newUser","email":"abc@gmail.com"},"bio":"hello man"}

    def test_patch(self):
        user = User.objects.create(username = 'newUser',email='abc@gmail.com')
        user_profile = UserProfile.objects.create(user = user,bio='hello')
        response = self.client.patch('/users/1/',{"user":{"username":"newUser","email":"abc@gmail.com"},"bio":"hello man"})
        assert response.status_code == 200 and response.json() == {"user":{"username":"newUser","email":"abc@gmail.com"},"bio":"hello man"}

        
