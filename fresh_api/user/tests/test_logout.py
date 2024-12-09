from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken
from user.models import Users

class LogoutTestCase(APITestCase):
    
    def setUp(self):
        self.logout_url = reverse('logout')
        self.user_data = {
            'email': 'test@test.com',
            'password': 'testpass123'
        }
        self.user = Users.objects.create_user(
            email=self.user_data['email'],
            password=self.user_data['password']
        )

    ''' 로그아웃 성공 '''
    # def logout_success(self):
        
    ''' 잘못된 토근으로 로그아웃 '''
    
    ''' 토큰 없이 로그아웃 '''





        