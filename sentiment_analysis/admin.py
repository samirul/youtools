from django.contrib import admin
from .models import SentiMentAnalysis, Category

# Register your models here.

@admin.register(SentiMentAnalysis)
class ImagesModelAdmin(admin.ModelAdmin):
    list_display = [
      'id','video_title','main_result'
    ]

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = [
      'id','category_name'
    ]

