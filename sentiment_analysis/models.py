"""
    Sentiment analysis django model for.
"""
import time
from collections import deque
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_delete
from accounts.models import User
from producers.producers_sentiment_analysis import RabbitMQConnection

queue = deque()

rabbit_mq = RabbitMQConnection()

# Create your models here.

class Category(models.Model):
    """Models for storing Sentiment analysis data
       category from rabbitMQ.

    Args:
        models (models): django model.

    Returns:
        String: Will display category title in django admin panel.
    """
    id = models.CharField(primary_key=True)
    category_name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = models.Manager()

    class Meta:
        """Added custom model name."""
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return str(self.category_name)
    
@receiver(post_delete, sender=Category)
def delete_data_on_model_after_deleting_data_from_admin_panel(sender, instance, **kwargs):
    """Here signal is for publishing data to RabbitMQ after deleting
       data from the django admin panel, so data can get deleted
       from sentiment_analysis flask application.

    Args:
        sender (Parameter): Category model.
        instance (Parameter): Contains deleted object even after getting deleted.
    """
    time.sleep(1)
    if not Category.objects.exists():
        rabbit_mq.publish_sentiment_analysis("delete_sentiment_analysis_category_data_from_flask", instance.id)


class SentiMentAnalysis(models.Model):
    """Models for storing Sentiment analysis data.
       from rabbitMQ 

    Args:
        models (models): django model.

    Returns:
        String: Will display video title in django admin panel.
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

    class Meta:
        """Added custom model name."""
        verbose_name_plural = "Sentiment analysis"

    def __str__(self) -> str:
        return str(self.video_title)
    

@receiver(post_delete, sender=SentiMentAnalysis)
def delete_category_data_on_model_after_deleting_data_from_admin_panel(sender, instance, **kwargs):
    """Here signal is for publishing data to RabbitMQ after deleting
       data from the django admin panel, so data can get deleted
       from sentiment_analysis flask application.

    Args:
        sender (Parameter): SentiMentAnalysis model.
        instance (Parameter): Contains deleted object even after getting deleted.
    """
    queue.appendleft(rabbit_mq.publish_sentiment_analysis("delete_sentiment_analysis_data_from_flask", instance.id))
    if not SentiMentAnalysis.objects.exists():
        while queue:
            queue.pop()