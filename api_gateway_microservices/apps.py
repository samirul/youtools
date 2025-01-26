"""
    Django app api_gateway_microservices for adding inside settings.py.
"""
from django.apps import AppConfig

class ApiGatewayMicroservicesConfig(AppConfig):
    """Django api_gateway_microservices app config.

    Args:
        AppConfig (Django APP): Django app api_gateway_microservices config.
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "api_gateway_microservices"
