"""
  Added models from Images app inside admin so can register inside control panel(can view data from
  django admin panel).
"""

from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Images

# Register your models here.

@admin.register(Images)
class ImagesModelAdmin(ModelAdmin):
    """Register Images model.

    Args:
        admin (class ModelAdmin): For registering in the admin panel.
    """
    list_display = [
      'id','image_name','image_data'
    ]
