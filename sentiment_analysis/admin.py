"""
  Added models from sentiment analysis app inside admin so can register inside control panel(can view data from
  django admin panel).
"""

from django.contrib import admin
from django.apps import apps
from .models import SentiMentAnalysis, Category

# Register your models here.

@admin.register(SentiMentAnalysis)
class ImagesModelAdmin(admin.ModelAdmin):
    """Register SentiMentAnalysis model.

    Args:
      admin (class ModelAdmin): For registering in the admin panel.
    """
    list_display = [
      'id','video_title','main_result'
    ]

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    """Register Category model.

    Args:
      admin (class ModelAdmin): For registering in the admin panel.
    """
    list_display = [
      'id','category_name'
    ]


apps.get_app_config('sentiment_analysis').verbose_name = "Flask Sentiment Analysis management"