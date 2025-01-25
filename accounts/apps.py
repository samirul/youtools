"""
    Django app accounts for adding inside settings.py.
"""

from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """Django accounts app config.

    Args:
        AppConfig (Django APP): Django app accounts config.
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "accounts"
