from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ 'first_name', 'last_name']
    
    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.email