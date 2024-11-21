"""
    Sentiment analysis django model.
"""

from django.db import models
from accounts.models import User

# Create your models here.
class SentiMentAnalysis(models.Model):
    """Models for storing Sentiment analysis data
       from rabbitMq 

    Args:
        models (models): django model

    Returns:
        _type_: Will display video title in django admin pannel
    """
    id = models.CharField(primary_key=True)
    video_title = models.CharField(max_length=255)
    video_url = models.CharField(max_length=255)
    comment = models.TextField(max_length=500)
    main_result = models.CharField(max_length=100)
    other_result = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self) -> str:
        return str(self.video_title)