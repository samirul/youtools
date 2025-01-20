from django.contrib import admin
from .models import TopBanner

# Register your models here.
@admin.register(TopBanner)
class OthersModelAdmin(admin.ModelAdmin):
    list_display = [
      'id','banner_text'
    ]