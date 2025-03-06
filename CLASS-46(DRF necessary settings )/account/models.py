from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_verified = models.BooleanField(default=False)
    veirification_token = models.CharField(max_length=32, blank=True, null=True)
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    