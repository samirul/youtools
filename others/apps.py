"""
    Django app Others for adding inside settings.py.
"""
from django.apps import AppConfig

class OthersConfig(AppConfig):
    """Django Others app config.

    Args:
        AppConfig (Django APP): Django app Others config.
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "others"
