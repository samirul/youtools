"""
    Added model for image app.
"""

from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_delete
from accounts.models import User
from producers.producers_text2image import publish_text2_image

# Create your models here.
class Images(models.Model):
    """Created Images model for saving
       data from RabbitMQ.

    Args:
        models (module): For creating django Model.

    Returns:
        String: return image name to show in the django admin panel.
    """
    id = models.CharField(primary_key=True)
    image_data = models.ImageField(upload_to="images")
    image_name = models.CharField(max_length=120)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self) -> str:
        return str(self.image_name)
     
@receiver(post_delete, sender=Images)
def delete_data_on_model_after_deleting_data_from_admin_pannel(sender, instance, **kwargs):
    """Here signal is for publishing data to RabbitMQ after deleting
       data from the django admin panel, so data can get deleted
       from text2image flask application.

    Args:
        sender (Parameter): Images model.
        instance (Parameter): Contains deleted object even after getting deleted.
    """
    if not Images.objects.exists():
        publish_text2_image("delete_images_from_database", instance.id)
