from .base import *


DEBUG = environ.get('DEBUG')

ALLOWED_HOSTS = ["*"]

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}