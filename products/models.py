from django.db import models
from BaseID.models import BaseIdModel

# Create your models here.
class ProductList(BaseIdModel):
    product_name = models.CharField(max_length=150, null=False, blank=False)
    product_description = models.TextField(max_length=255, null=False, blank=False)
    product_url = models.CharField(max_length=255)
    objects = models.Manager()

    def __str__(self):
        return str(self.product_name)


