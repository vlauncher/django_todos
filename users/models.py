from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from users.manager import CustomUserManager


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'