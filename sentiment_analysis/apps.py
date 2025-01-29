"""
    Django app sentiment Analysis for adding inside settings.py.
"""

from django.apps import AppConfig


class SentimentAnalysisConfig(AppConfig):
    """Django sentiment Analysis app config.

    Args:
        AppConfig (Django APP): Django app Sentiment Analysis config.
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "sentiment_analysis"