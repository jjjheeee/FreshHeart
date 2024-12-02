from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from user.models import Users
from django.conf import settings

# Create your tests here.
class SignupTestCase(APITestCase):
    
    def setUp(self):
        settings.DEBUG = True
        self.signup_url = reverse('signup')
        
    def test_signup_success(self):
        data = {
            "email" : "test@test.com",
            "nickname" : "testUser",
            "password" : "test1234"
        }
        
        respons = self.client.post(self.signup_url,data)
        self.assertEqual(respons.status_code, status.HTTP_201_CREATED)
        self.assertEqual(respons.data['user']['email'], data['email'])
        self.assertIn('uuid',respons.data['user'])