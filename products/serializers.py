from rest_framework import serializers
from .models import ProductList

class ProductViewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductList
        fields = ['id', 'product_image', 'product_name', 'product_description', 'product_url']