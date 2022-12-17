import pytest
from django.urls import reverse
from factories import AlbumFactory
from django.forms.models import model_to_dict


@pytest.mark.django_db
class TestAddAlbum:
    def test_not_authenticated_user(self, not_auth_client):
        url = reverse('add_album')
        login_url = reverse('login')
        album = AlbumFactory()
        response = not_auth_client.post(url, model_to_dict(
            album), content_type='application/json')
        assert response.status_code == 302
        assert response.url == login_url + '?next=' + url

    def test_authenticated_user(self, auth_client):
        client = auth_client()
        url = reverse('add_album')
        album = AlbumFactory()
        response = client.post(url, model_to_dict(
            album), content_type='application/json')
        assert response.status_code == 200