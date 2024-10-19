from rest_framework import serializers
from users.models import User
from djoser.serializers import UserCreateSerializer


class CustomUserCreateSerializer(UserCreateSerializer):
    
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('email', 'first_name', 'last_name')
