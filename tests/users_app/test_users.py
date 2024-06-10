from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from django.urls import reverse
from django.core.management import call_command

from users.models.user import User


class UsersTestCase(APITestCase):
    def setUp(self):
        fixtures_path = ['users/fixtures/users.json']
        call_command('loaddata', fixtures_path)
        self.client = APIClient()
        self.user = User.objects.get(id=9)
        self.client.force_authenticate(user=self.user)

    def test_users_get(self):
        url = reverse('users-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_users_me_get(self):
        url = reverse('users-me')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
