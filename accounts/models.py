"""
Accounts models — User Profile extending Django's built-in User model.
"""
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Extended user profile with additional fields."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png', blank=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    zipcode = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
