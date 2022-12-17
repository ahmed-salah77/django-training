import pytest
from rest_framework.test import APITestCase

@pytest.mark.django_db
class TestAuthentication(APITestCase):

    def test_pass_register(self):
        response = self.client.post('/authentication/register/',
        {"username":"someone",
        "email":"abc@gmail.com",
        "password":"secret1234",
        "confirmation_password":"secret1234"})
        assert response.status_code == 200 and response.data['user'] == {'bio': '', 'email': 'abc@gmail.com', 'id': 1, 'username': 'someone'}
    
    def test_not_match_password_register(self):
        response = self.client.post('/authentication/register/',
        {"username":"someone",
        "email":"abc@gmail.com",
        "password":"secret1234",
        "confirmation_password":"secret12345"})
        assert response.status_code == 400

    def test_not_email_register(self):
        response = self.client.post('/authentication/register/',
        {"username":"someone",
        "email":"notEmail",
        "password":"secret1234",
        "confirmation_password":"secret1234"})
        assert response.status_code == 400  

    def test_password_with_len_less_than_8_register(self):
        response = self.client.post('/authentication/register/',
        {"username":"someone",
        "email":"abc@gmail.com",
        "password":"secret1",
        "confirmation_password":"secret1"})
        assert response.status_code == 400 

    def test_password_without_any_letter_register(self):
        response = self.client.post('/authentication/register/',
        {"username":"someone",
        "email":"abc@gmail.com",
        "password":"123456789",
        "confirmation_password":"123456789"})
        assert response.status_code == 400 

              
    def test_pass_login(self):
        self.client.post('/authentication/register/',
        {"username":"someone",
        "email":"abc@gmail.com",
        "password":"secret1234",
        "confirmation_password":"secret1234"})
        response = self.client.post('/authentication/login/',
        {
            "username":"someone",
            "password":"secret1234"
        })
        assert response.status_code == 200

    def test_fail_login(self):
        self.client.post('/authentication/register/',
        {"username":"someone",
        "email":"abc@gmail.com",
        "password":"secret1234",
        "confirmation_password":"secret1234"})
        response = self.client.post('/authentication/login/',
        {
            "username":"someone",
            "password":"secret123"
        })
        assert response.status_code == 400