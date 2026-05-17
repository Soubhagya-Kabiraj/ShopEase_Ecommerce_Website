"""
Accounts admin configuration.
"""
from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'city', 'state', 'created_at']
    list_filter = ['city', 'state']
    search_fields = ['user__username', 'user__email', 'phone']
