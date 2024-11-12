from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class CustomUserCreateSerializer(UserCreateSerializer):
    
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
        extra_kwargs = {
            'first_name': {'error_messages': {'required': 'First name is required', 'blank': 'First name cannot be blank'}},
            'last_name': {'error_messages': {'required': 'Last name is required', 'blank': 'Last name cannot be blank'}},
            'email': {'error_messages': {'required': 'Email is required', 'invalid': 'Invalid email address'}},
            'password': {'write_only': True, 'error_messages': {'required': 'Password is required'}}
        }
