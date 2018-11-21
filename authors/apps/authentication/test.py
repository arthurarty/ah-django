from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import User

class AccountTests(APITestCase):
    """handles user registration tests"""
    def test_new_user_registration(self):
        """check if new user can be registered"""
        url = reverse('authentication')
        data = {"user" : {"username": "Jac", "email": "jak@jake.jake", "password": "jakejake"}}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_login(self):
        """check if new user can be registered"""
        url = reverse('authentication')
        data = {"user" : {"username": "Jac", "email": "jak@jake.jake", "password": "jakejake"}}
        response = self.client.post(url, data, format='json')
        url = reverse('login')
        data = {"user":{"email": "jak@jake.jake","password": "jakejake"}}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.get().username, 'Jac')

    # def test_get_user(self)
    #     """
    #     Ensure we can create a new account object.
    #     """
    #     url = reverse('authentication')
    #     data = {"user":{"email": "arthurnangai","password": "qweArthur"}}
    #     response = self.client.post(url, data, format='json')
    #     response = self.client.get(url, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(User.objects.count(), 1)
    #     self.assertEqual(User.objects.get().username, 'arthurnangai')