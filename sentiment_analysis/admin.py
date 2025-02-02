"""
  Added models from sentiment analysis app inside admin so can register inside control panel(can view data from
  django admin panel).
"""

from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import SentiMentAnalysis, Category

# Register your models here.

@admin.register(SentiMentAnalysis)
class ImagesModelAdmin(ModelAdmin):
    """Register SentiMentAnalysis model.

    Args:
      admin (class ModelAdmin): For registering in the admin panel.
    """
    list_display = [
      'id','video_title','main_result'
    ]

@admin.register(Category)
class CategoryModelAdmin(ModelAdmin):
    """Register Category model.

    Args:
      admin (class ModelAdmin): For registering in the admin panel.
    """
    list_display = [
      'id','category_name'
    ]

