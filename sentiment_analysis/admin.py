from django.contrib import admin
from .models import SentiMentAnalysis

# Register your models here.

@admin.register(SentiMentAnalysis)
class ImagesModelAdmin(admin.ModelAdmin):
    list_display = [
      'id','video_title','main_result'
    ]
