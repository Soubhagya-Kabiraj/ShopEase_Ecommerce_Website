"""
Accounts signals — Auto-create Profile when a User is created.
"""
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """Create a Profile automatically when a new User is registered."""
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """Save profile whenever user is saved."""
    instance.profile.save()
