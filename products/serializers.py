"""
    Serializer for Products app models so can validate and send json to the frontend,
    (Product page and Home Page).
"""

from rest_framework import serializers
from .models import ProductList

class ProductViewsSerializer(serializers.ModelSerializer):
    """Serializer for ProductViews in the views.

    Args:
        serializers (ModelSerializer): DRF model serializer class for serialization.
    """
    class Meta:
        """Required meta class for serialization."""
        model = ProductList
        fields = ['id', 'product_image', 'product_name', 'product_description', 'product_url']