from rest_framework import serializers
from .models import Images

class GenerateImagesSerializers(serializers.Serializer):
    text = serializers.CharField(max_length=120, required=True, allow_blank=False, allow_null=False)
