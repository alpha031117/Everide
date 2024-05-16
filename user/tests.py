from django.contrib.auth.hashers import make_password
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import MyUser, Driver

class DisplayUserTestCase(APITestCase):
    def setUp(self):
        # Create some test users
        self.user1 = MyUser.objects.create(username='user1', email='user1@example.com', password='password1', phoneNumber='1234567890')
        self.user2 = MyUser.objects.create(username='user2', email='user2@example.com', password='password2', phoneNumber='0987654321')
    
    def test_display_user(self):
        # Simulate a GET request to retrieve all users
        url = reverse('user')  # Assuming the name of the user list endpoint is 'user-list'
        response = self.client.get(url)
        
        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Check if the response contains the correct number of users
        self.assertEqual(len(response.data), 2)  # Assuming there are only two users created
        
        # Check if user1's username is in the response
        self.assertIn('user1', [user['username'] for user in response.data])
        
        # Check if user2's username is in the response
        self.assertIn('user2', [user['username'] for user in response.data])

class GetDriverAPITestCase(APITestCase):
    def setUp(self):
        # Create some test drivers
        self.driver1 = Driver.objects.create(name='John', car_model='Toyota Camry', plate_number='ABC123', rating=4.5, active=True, service_duration_year=3)
        self.driver2 = Driver.objects.create(name='Jane', car_model='Honda Accord', plate_number='XYZ456', rating=4.2, active=True, service_duration_year=2)

    def test_get_driver(self):
        # Simulate a GET request to retrieve all drivers
        url = reverse('driver')  # Assuming the name of the get_driver view is 'get_driver'
        response = self.client.get(url)

        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the response data contains the correct number of drivers
        self.assertEqual(len(response.data), 2)  # Assuming there are only two drivers created

        # Check if the response data contains the expected driver details
        expected_data = [
            {'name': 'John', 'car_model': 'Toyota Camry', 'plate_number': 'ABC123', 'rating': 4.5, 'active': True, 'service_duration_year': 3},
            {'name': 'Jane', 'car_model': 'Honda Accord', 'plate_number': 'XYZ456', 'rating': 4.2, 'active': True, 'service_duration_year': 2}
        ]
        self.assertEqual(response.data, expected_data)


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
        response = self.client.post(url, data, format='json')

        # Assert response status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class AddFriendAPITestCase(APITestCase):
    def setUp(self):
        # Create some users for testing
        self.user1 = MyUser.objects.create(username='user1', email='user1@example.com', password='password1', phoneNumber='1234567890')
        self.user2 = MyUser.objects.create(username='user2', email='user2@example.com', password='password2', phoneNumber='0987654321')

    def test_add_friend(self):
        # Simulate a POST request to add a friend
        url = reverse('add_friend')  # Assuming the name of the add_friend view is 'add_friend'
        data = {'username': 'user1', 'friend': 'user2'}
        response = self.client.post(url, data, format='json')

        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the friend has been added to the user's friends list
        user1 = MyUser.objects.get(username='user1')
        user2 = MyUser.objects.get(username='user2')
        self.assertIn(user2, user1.friends.all())
