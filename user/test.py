import os
from django.test import TestCase
from django.conf import settings
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import User  # Import your User model if needed
from .serializer import LoginSerializer

class LoginViewTestCase(TestCase):
    def setUp(self):
        # Set up Django settings module
        os.environ['DJANGO_SETTINGS_MODULE'] = 'everide.settings'  # Replace 'your_project.settings' with your actual settings module

        # Other setup code goes here
        # Create test user
        self.user = User.objects.create(username='testuser', email='test@example.com')
        self.user.set_password('testpassword')
        self.user.save()

        # Initialize DRF APIClient
        self.client = APIClient()

    def test_login_view(self):
        # Define test data
        data = {
            'username': 'testuser',
            'password': 'testpassword'
        }

        # Make POST request to the login view
        url = reverse('login')  # Assuming you've set up a URL for your login view with the name 'login'
        response = self.client.post(url, data, format='json')

        # Assert response status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert response data
        expected_data = LoginSerializer(instance=self.user).data
        self.assertEqual(response.data, expected_data)
