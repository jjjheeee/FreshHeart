from rest_framework import serializers
from .models import Users

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
        model = model = Users
        fields = ('email','password','nickname','uuid')