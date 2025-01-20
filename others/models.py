from django.db import models
from BaseID.models import BaseIdModel

# Create your models here.
class TopBanner(BaseIdModel):
    banner_image = models.ImageField(upload_to='media/homepage')
    banner_text = models.TextField(max_length=500)
    objects = models.Manager()

    def __str__(self):
        return str(self.banner_text)