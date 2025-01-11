from django.contrib import admin
from .models import ProductList

# Register your models here.
@admin.register(ProductList)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = [
      'id','product_name', 'product_description'
    ]