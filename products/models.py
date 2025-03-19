"""
    Required models for products app (ORM) so can make databases in PostgresDB (migrate)
    without writing raw SQL commands.
"""

from django.db import models
from BaseID.models import BaseIdModel

# Create your models here.
class ProductList(BaseIdModel):
    """ORM model for ProductList database.

    Args:
        BaseIdModel (Custom abstract Django model): Custom BaseID django abstract model
        for needing some attributes to inherit(BaseIdModel will not migrate in the database,
        will be just abstract class).

    Returns:
        String: Will return string product name so can view in the admin control panel.
    """
    product_image = models.ImageField(upload_to='media/products/images/')
    product_name = models.CharField(max_length=150, null=False, blank=False)
    product_description = models.TextField(max_length=255, null=False, blank=False)
    product_url = models.CharField(max_length=255)
    objects = models.Manager()

    class Meta:
        """Added custom model name."""
        verbose_name_plural = "Product list"

    def __str__(self):
        return str(self.product_name)


