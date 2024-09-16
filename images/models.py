from django.db import models

# Create your models here.
class Images(models.Model):
    id = models.CharField(primary_key=True)
    image_data = models.ImageField(upload_to="images")
    image_name = models.CharField(max_length=120)
    objects = models.Manager()

    def __str__(self) -> str:
        return str(self.image_name)