"""
  Added models from products app inside admin so can register inside control panel(can view data from
  django admin panel).
"""

from django.contrib import admin
from django.apps import apps
from .models import ProductList

# Register your models here.
@admin.register(ProductList)
class CategoryModelAdmin(admin.ModelAdmin):
    """Register ProductList model.

    Args:
      admin (class ModelAdmin): For registering in the admin panel.
    """
    list_display = [
      'id','product_name', 'product_description'
    ]

apps.get_app_config('products').verbose_name = "Flask Products Management"