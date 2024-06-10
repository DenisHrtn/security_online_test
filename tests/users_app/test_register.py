from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from django.urls import reverse


class RegisterTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('register')

    def test_register(self):
        post_data = {
            'email': 'test@gmail.com',
            'phone_number': '+375445556677',
            'username': 'testik',
            'password': 'somepassword',
            'password_confirmation': 'somepassword'
        }
        response = self.client.post(self.register_url, post_data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_register_with_bad_creeds(self):
        post_data = {
            'email': 'test@gmail.com',
            'phone_number': '+375445556677',
            'username': 'testik',
            'password': 'rrr',
            'password_confirmation': 'rrr'
        }
        response = self.client.post(self.register_url, post_data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_without_phone_number_and_username(self):
        post_data = {
            'email': 'test@gmail.com',
            'phone_number': '',
            'username': '',
            'password': 'somepassword',
            'password_confirmation': 'somepassword'
        }
        response = self.client.post(self.register_url, post_data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
