from django.urls import path
from .apis import signup_api, UserLoginAPI, UserAPI
from rest_framework_simplejwt.views import (
    TokenObtainPairView, # 토큰을 생성해주는 뷰
    TokenRefreshView, # refresh 토큰으로 access 토큰을 재발급하는 뷰
    TokenVerifyView, # 토큰 유효성 확인 뷰
)

urlpatterns = [
    path('', UserAPI.as_view(), name='user'),
    path('token', UserLoginAPI.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup', signup_api, name='signup'),
]