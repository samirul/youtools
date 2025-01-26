"""
    Serializer for views.
"""
from rest_framework import serializers

class GenerateImagesSerializers(serializers.Serializer): #pylint: disable=W0223
    """Serializer is for views to generate images.

    Args:
        serializers (Class): drf Serializer class
    """
    text = serializers.CharField(max_length=120, required=True, allow_blank=False, allow_null=False)


class GetCommentsAndAnalysisCommentsSerializers(serializers.Serializer): #pylint: disable=W0223
    """Serializer is for views to analyse youtube comments.

    Args:
        serializers (Class): drf Serializer class
    """
    url = serializers.CharField(max_length=200, required=True, allow_blank=False, allow_null=False)
    max_len = serializers.IntegerField(required=True)