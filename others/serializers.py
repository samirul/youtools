"""
    Serializer for Others app models so can validate and send jsons to the frontend,
    (frontend top banner and footer).
"""

from rest_framework import serializers
from .models import (TopBanner, LinksFooterCategory,
                     TitleFooter, CopyRightFooter, SocialLinksFooterCategory, AboutUs,
                     PrivacyPolicy)


class TopBannerViewSerializer(serializers.ModelSerializer):
    """Serializer for TopBannerView in the views.

    Args:
        serializers (ModelSerializer): DRF model serializer class for serialization.
    """
    class Meta:
        """Required meta class for serialization."""
        model = TopBanner
        fields = ['id', 'banner_image', 'banner_text']


class LinksFooterViewSerializer(serializers.ModelSerializer):
    """Serializer for LinksFooterView in the views.

    Args:
        serializers (ModelSerializer): DRF model serializer class for serialization.

    Returns:
        Returns: to_representation is build in DRF function for modifying data the way we need
        before serializing it to the json format.
    """
    class Meta:
        """Required meta class for serialization."""
        model = LinksFooterCategory
        fields = ['id', 'category_name']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['name'] = [
            {
                "id": footer.id,
                "links_title": footer.links_title,
                "links_url": footer.links_url
            }
            for footer in instance.links_footer.all()
        ]
        return rep

class SocialLinksFooterViewSerializer(serializers.ModelSerializer):
    """Serializer for SocialLinksFooterView in the views.

    Args:
        serializers (ModelSerializer): DRF model serializer class for serialization.

    Returns:
        Returns: to_representation is build in DRF function for modifying data the way we need
        before serializing it to the json format.
    """
    class Meta:
        """Required meta class for serialization."""
        model = SocialLinksFooterCategory
        fields = ['id', 'social_category_name']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['social_data'] = [
            {
                "id": social.id,
                "social_icon": social.social_icon,
                "social_url": social.social_url,
                "social_label": social.social_label
            }
            for social in instance.sociallinks_footer.all()
        ]
        return rep

class TitleFooterViewSerializer(serializers.ModelSerializer):
    """Serializer for TitleFooterView in the views.

    Args:
        serializers (ModelSerializer): DRF model serializer class for serialization.
    """
    class Meta:
        """Required meta class for serialization."""
        model = TitleFooter
        fields = ['id', 'footer_title', 'footer_description']


class CopyRightFooterViewSerializer(serializers.ModelSerializer):
    """Serializer for CopyRightFooterView in the views.

    Args:
        serializers (ModelSerializer): DRF model serializer class for serialization.
    """
    class Meta:
        """Required meta class for serialization."""
        model = CopyRightFooter
        fields = ['id', 'copyright_footer']

class AboutUsViewsSerializer(serializers.ModelSerializer):
    """Serializer for AboutUsViews in the views.

    Args:
        serializers (ModelSerializer): DRF model serializer class for serialization.
    """
    class Meta:
        """Required meta class for serialization."""
        model = AboutUs
        fields = ['id', 'title', 'description']


class PrivacyPolicyViewsSerializer(serializers.ModelSerializer):
    """Serializer for PrivacyPolicyViews in the views.

    Args:
        serializers (ModelSerializer): DRF model serializer class for serialization.
    """
    class Meta:
        """Required meta class for serialization."""
        model = PrivacyPolicy
        fields = ['id', 'title', 'description']
