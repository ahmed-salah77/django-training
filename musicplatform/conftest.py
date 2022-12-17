from rest_framework.test import APIClient
from django.contrib.auth.models import User
import pytest
# @pytest.fixture
# def auth_client(user = None):
#     if(user is None):
#         user = User.objects.create()
#     client = APIClient()
#     client.login(username=user.username, password=user.password)
#     client.force_authenticate(user=client)
#     return client
import factory
from factories import UserFactory
from faker import Faker


@pytest.fixture()
def auth_client(db):

    def _auth_client(user=None):
        client = APIClient()
        auth_user = user if user else UserFactory()
        client.force_login(user=auth_user)
        from django.contrib import auth
        user = auth.get_user(client)
        assert user.is_authenticated
        return client

    return _auth_client

@pytest.fixture()
def not_auth_client():
    return APIClient()