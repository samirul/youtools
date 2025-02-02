"""
  Added models from products app inside admin so can register inside control panel(can view data from
  django admin panel).
"""

from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import ProductList

# Register your models here.
@admin.register(ProductList)
class CategoryModelAdmin(ModelAdmin):
    """Register ProductList model.

    Args:
      admin (class ModelAdmin): For registering in the admin panel.
    """
    list_display = [
      'id','product_name', 'product_description'
    ]