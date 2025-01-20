from rest_framework import serializers
from .models import (TopBanner, LinksFooterCategory, LinksFooter,
                     SocialLinksFooter, TitleFooter, CopyRightFooter)


class TopBannerViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopBanner
        fields = ['id', 'banner_image', 'banner_text']

class LinksFooterCategoryViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinksFooterCategory
        fields = ['id', 'category_name']

class LinksFooterViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinksFooter
        fields = ['id', 'links_title', 'links_url', 'category']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['category'] = instance.category.category_name
        return rep

class SocialLinksFooterViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLinksFooter
        fields = ['id', 'social_icon', 'social_url','social_label','category']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['category'] = instance.category.category_name
        return rep

class TitleFooterViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = TitleFooter
        fields = ['id', 'footer_title', 'footer_description','category']
        
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['category'] = instance.category.category_name
        return rep

class CopyRightFooterViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = CopyRightFooter
        fields = ['id', 'copyright_footer']
