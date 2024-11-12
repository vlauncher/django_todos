# todos/serializers.py

from rest_framework import serializers
from .models import User, Todo

class TodoSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'completed', 'slug', 'user']

class TodoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'completed']
