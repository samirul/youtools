from django.contrib import admin
from .models import Images

# Register your models here.

@admin.register(Images)
class ImagesModelAdmin(admin.ModelAdmin):
    list_display = [
      'id','image_name','image_data'
    ]
