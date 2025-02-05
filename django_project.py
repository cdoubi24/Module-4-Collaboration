# Django Project Setup - Combined File

# models.py - Defining the Post model
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# admin.py - Registering the model in Django admin
from django.contrib import admin
from .models import Post

admin.site.register(Post)

# settings.py - Basic settings (snippet)
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',  # Registering the blog app
]

TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'en-us'

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'

ALLOWED_HOSTS = ['localhost', '127.0.0.1']
