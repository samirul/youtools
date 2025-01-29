"""
    Django app products for adding inside settings.py.
"""
from django.apps import AppConfig


class ProductsConfig(AppConfig):
    """Django products app config.

    Args:
        AppConfig (Django APP): Django app products config.
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "products"
