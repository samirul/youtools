"""
    Django app BaseID for adding inside settings.py.
"""

from django.apps import AppConfig


class BaseidConfig(AppConfig):
    """Django BaseID app config.

    Args:
        AppConfig (Django APP): Django app accounts config.
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "BaseID"
