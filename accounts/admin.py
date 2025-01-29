"""
  Added models from accounts app inside admin
  so can register inside control panel(can view data from
  django admin panel).
"""

from django.contrib import admin
from accounts.models import User

# Register your models here.

@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    """Register User model.

    Args:
        admin (class ModelAdmin): For registering in the admin panel.
    """
    list_display = [
      'id', 'username','email','is_active','is_admin'
    ]