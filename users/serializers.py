from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class CustomUserCreateSerializer(UserCreateSerializer):
    password2 = serializers.CharField(write_only=True)
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'password2']
        
    
    def validate(self, attrs):
        data = super().validate(attrs)
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError('Passwords do not match')
        return data