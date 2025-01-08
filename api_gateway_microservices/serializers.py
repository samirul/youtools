from rest_framework import serializers

class GenerateImagesSerializers(serializers.Serializer):
    text = serializers.CharField(max_length=120, required=True, allow_blank=False, allow_null=False)


class GetCommentsAndAnalysisCommentsSerializers(serializers.Serializer):
    url = serializers.CharField(max_length=200, required=True, allow_blank=False, allow_null=False)
    max_len = serializers.IntegerField(required=True)
