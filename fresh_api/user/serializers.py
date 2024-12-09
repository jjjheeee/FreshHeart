from rest_framework import serializers
from .models import Users
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    def validate(self, attrs):
        data = super().validate(attrs)
        
        # 유저 정보 추가
        data['user'] = {
            'nickname': self.user.nickname,
            'email': self.user.email,
            'isLogin': True
            # 필요한 다른 유저 필드들 추가
        }
        
        return data



class SignupUserSerializer(serializers.ModelSerializer):
    
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    nickname = serializers.CharField()
    
    class Meta:
        model = Users
        fields = ('email','password','nickname')
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Users.objects.create(**validated_data)
        user.set_password(password)
        
        user.save()
        
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('email', 'password', 'nickname', 'uuid')
        extra_kwargs = {
            'password': {'write_only': True},
            'uuid': {'read_only': True},
            'nickname': {'read_only': True}
        }
    
    def validate(self, data):
        print("validate 메서드 실행")
        print(f"검증할 데이터: {data}")

        user = authenticate(email=data['email'], password=data['password'])
        if user and user.is_active:
            return user
        raise serializers.ValidationError("잘못된 로그인 정보입니다.")
    
    def update(self, instance, validated_data):
        if 'password' in validated_data:
            instance.set_password(validated_data.pop('password'))
        return super().update(instance, validated_data)