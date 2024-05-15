from django.contrib.auth.hashers import make_password
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import MyUser

class LoginViewTestCase(APITestCase):
    def setUp(self):
        # Create a test user 
        self.user = MyUser.objects.create(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )

    def test_valid_login(self):
        # Define valid login credentials
        data = {
            'username': 'testuser',
            'password': 'testpassword'
        }

        # Make a POST request to the login view
        url = reverse('login')  # Assuming you've set up a URL for your login view with the name 'login'
        print(url)
        response = self.client.post(url, data, format='json')

        # Assert response status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)