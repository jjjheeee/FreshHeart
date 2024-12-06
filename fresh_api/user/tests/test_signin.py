from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken
from user.models import Users
class SigninTestCase(APITestCase):
    
    def setUp(self):
        self.signup_url = reverse('signup')
        self.signin_url = reverse('token_obtain_pair')
        self.user_data = {
            'email': 'test@example.com',
            'password': 'testpassword123',
            'nickname': 'testuser'
        }
        self.login_data = {
            'email': 'test@example.com',
            'password': 'testpassword123',
        }
        
        self.user = Users.objects.create_user(
            email=self.user_data['email'],
            password=self.user_data['password'],
            nickname=self.user_data['nickname']
        )

    ''' 로그인 성공 '''
    def test_signin_success(self):
        login_response = self.client.post(self.signin_url, self.login_data)
        self.assertEqual(login_response.status_code, status.HTTP_200_OK)
        self.assertIn('access', login_response.data)
        self.assertIn('refresh', login_response.data)

    ''' 로그인 실패 '''
    def test_user_login_wrong_credentials(self):
        wrong_data = {
            'email': 'testuser@example.com',
            'password': 'wrongpass'
        }
        login_response = self.client.post(self.signin_url, wrong_data)
        self.assertEqual(login_response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    ''' 토큰인증 api 호출 성공 '''
    def test_access_protected_endpoint_with_token(self):
        # 보호된 엔드포인트 URL (예: 사용자 상세 정보)
        protected_url = reverse('user')
        
        # 토큰 생성
        refresh = RefreshToken.for_user(self.user)
        access_token = str(refresh.access_token)
        
        # 헤더에 토큰 추가
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        
        response = self.client.get(protected_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    ''' 토큰인증 api 호출 실패~ '''
    def test_access_protected_endpoint_without_token(self):
        protected_url = reverse('user')
        response = self.client.get(protected_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    ''' 토큰 재발급 '''
    def test_token_refresh(self):
        # 먼저 로그인하여 토큰 얻기
        login_response = self.client.post(self.signin_url, self.login_data)
        refresh_token = login_response.data['refresh']
        
        # refresh 토큰으로 새로운 access 토큰 얻기
        refresh_url = reverse('token_refresh')
        response = self.client.post(
            refresh_url,
            {'refresh': refresh_token},
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)





        