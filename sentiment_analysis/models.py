"""
    Sentiment analysis django model.
"""
import time
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_delete
from accounts.models import User
from producers.producers_sentiment_analysis import RabbitMQConnection

rabbit_mq = RabbitMQConnection()

# Create your models here.

class Category(models.Model):
    """Models for storing Sentiment analysis data
       category from rabbitMq

    Args:
        models (models): django model

    Returns:
        _type_: Will display category title in django admin pannel
    """
    id = models.CharField(primary_key=True)
    category_name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self) -> str:
        return str(self.category_name)
    
@receiver(post_delete, sender=Category)
def delete_data_on_model_after_deleting_data_from_admin_pannel(sender, instance, **kwargs):
    time.sleep(1)
    if not Category.objects.exists():
        rabbit_mq.publish_sentiment_analysis("delete_sentiment_analysis_category_data_from_flask", instance.id)


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
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self) -> str:
        return str(self.video_title)
    

@receiver(post_delete, sender=SentiMentAnalysis)
def delete_category_data_on_model_after_deleting_data_from_admin_pannel(sender, instance, **kwargs):
    time.sleep(1)
    if not SentiMentAnalysis.objects.exists():
        rabbit_mq.publish_sentiment_analysis("delete_sentiment_analysis_data_from_flask", instance.id)