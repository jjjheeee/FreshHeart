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
        self.user_data = {
            'email': 'test@example.com',
            'password': 'testpassword123',
            'nickname': 'testuser'
        }
    
    """회원가입 성공 test"""    
    def test_signup_success(self):
        respons = self.client.post(self.signup_url,self.user_data)
        self.assertEqual(respons.status_code, status.HTTP_201_CREATED)
        self.assertEqual(respons.data['user']['email'], self.user_data['email'])
        self.assertIn('uuid',respons.data['user'])
        
    """잘못된 이메일 형식으로 회원가입 시도 test"""
    def test_create_account_with_invalid_email(self):
        self.user_data['email'] = 'invalid-email'
        response = self.client.post(self.signup_url, self.user_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    """중복된 이메일로 회원가입 test"""
    def test_signup_with_duplicate_email(self):
        self.client.post(self.signup_url,self.user_data)
        response = self.client.post(self.signup_url, self.user_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    