from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(first_name=first_name, last_name=last_name, email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, first_name, last_name, email, password):
        user = self.create_user(first_name, last_name, email, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user
    