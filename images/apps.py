"""
    Django app Images for adding inside settings.py.
"""
from django.apps import AppConfig

class ImagesConfig(AppConfig):
    """Django Images app config.

    Args:
        AppConfig (Django APP): Django app Images config.
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "images"
