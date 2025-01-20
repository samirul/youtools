from rest_framework import serializers
from .models import TopBanner


class TopBannerViewSerializer(serializers.ModelSerializer):
    model = TopBanner
    fields = ['id', 'banner_image', 'banner_text']

    