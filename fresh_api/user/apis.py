from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from .serializers import SignupUserSerializer, UserSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Users

class UserLoginAPI(APIView):

    def post(self, request, *args, **kwargs):
        
        serializer = TokenObtainPairSerializer(data=request.data)
        if serializer.is_valid():
            
            response_data = serializer.validated_data
            return Response(response_data, status=status.HTTP_200_OK)
        
        else:
            
            response_data = {
                'message':'잘못된 정보입니다.'
            }
            return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)
            
class UserAPI(APIView):
    
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        
        return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([AllowAny])
def signup_api(request):
    serializer = SignupUserSerializer(data = request.data)

    if serializer.is_valid():
        try:
            user = serializer.create(serializer.validated_data)
            serializer = UserSerializer(user)
            response_data = {
                'user' : serializer.data
            }
        except Exception as e:
            
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        return Response(response_data, status=status.HTTP_201_CREATED)
    else:
        
        response_data = {
            'message': serializer.errors
        }
        return Response(response_data, status=status.HTTP_400_BAD_REQUEST)