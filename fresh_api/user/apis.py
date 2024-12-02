from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from .serializers import SignupUserSerializer, UserSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def signup_api(request):
    serializer = SignupUserSerializer(data = request.data)
    if serializer.is_valid():
        user = serializer.create(serializer.validated_data)
        serializer = UserSerializer(user)
        response_data = {
            'user' : serializer.data
        }
        
        return Response(response_data, status=status.HTTP_201_CREATED)
    else:
        print(serializer.errors)
        response_data = {
            'message': serializer.errors
        }
        return Response(response_data, status=status.HTTP_400_BAD_REQUEST)