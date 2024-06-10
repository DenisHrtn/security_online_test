from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from django.urls import reverse
from django.core.management import call_command

from users.models.user import User


class LoginTestCase(APITestCase):
    def setUp(self):
        fixture_path = ['users/fixtures/users.json']
        call_command('loaddata', fixture_path)
        self.user = User.objects.get(id=9)
        self.client = APIClient()

    def test_login_success(self):
        url = reverse('login')
        post_data = {'email': 'super_employee@gmail.com', 'password': 'super_employee'}
        response = self.client.post(url, post_data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_fail(self):
        url = reverse('login')
        post_data = {'email': 'blabla@gmail.com', 'password': "blablabla"}
        resp = self.client.post(url, post_data, format='multipart')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
