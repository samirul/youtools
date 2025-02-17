"""
    DRF Other views for send data to api from backend to frontend for banners and footers.
"""
import os
from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import (TopBannerViewSerializer, LinksFooterViewSerializer,
                          SocialLinksFooterViewSerializer, TitleFooterViewSerializer,
                          CopyRightFooterViewSerializer, AboutUsViewsSerializer,
                          PrivacyPolicyViewsSerializer)
from .models import (TopBanner, LinksFooterCategory,
                     TitleFooter, CopyRightFooter, SocialLinksFooterCategory,
                     AboutUs, PrivacyPolicy)


CACHE_TIMEOUT = 60*int(os.environ.get('CACHE_TIME_LIMIT'))

# Create your views here.
class TopBannerView(APIView):
    """Responsible for sending data to the top banner in the frontend.

    Args:
        APIView (Class): Django Rest Framework(DRF) API View.
    """
    def get(self, request):
        """fetch top banner description and images for frontend from the backend (GET method).

        Args:
            request (request): Django request argument.

        Returns:
            Response: Send Response as json if response ok then send (200 OK) else
            send Exception (404 not found).
        """
        try:
            # check if cached item is stored or not.
            cached_item = cache.get('django_drf_top_banner_cache')
            if cached_item:
                return Response(cached_item, status=status.HTTP_200_OK)

            top_banner = TopBanner.objects.defer('created_at','updated_at')
            serializer = TopBannerViewSerializer(instance=top_banner, many=True)
            cache.set('django_drf_top_banner_cache', serializer.data, timeout=CACHE_TIMEOUT)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)

               
class LinksFooterView(APIView):
    """Responsible for sending data to footer links in the frontend from the backend.

    Args:
        APIView (Class): Django Rest Framework(DRF) API View.
    """
    def get(self, request):
        """fetch links from the backend to the frontend (GET method).

        Args:
            request (request): Django request argument.

        Returns:
            Response: Send Response as json if response ok then send (200 OK) else
            send Exception (404 not found).
        """
        try:
            # check if cached item is stored or not.
            cached_item = cache.get('django_drf_link_footer_cache')
            if cached_item:
                return Response(cached_item, status=status.HTTP_200_OK)
            
            link = LinksFooterCategory.objects.prefetch_related('links_footer').defer('created_at','updated_at')
            serializer = LinksFooterViewSerializer(instance=link, many=True)
            cache.set('django_drf_link_footer_cache', serializer.data, timeout=CACHE_TIMEOUT)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class SocialLinksFooterView(APIView):
    """Responsible for sending data to footer social links in the frontend from the backend.

    Args:
         APIView (Class): Django Rest Framework(DRF) API View.
    """
    def get(self, request):
        """fetch social links from the backend to the frontend (GET method).

        Args:
            request (request): Django request argument.

        Returns:
            Response: Send Response as json if response ok then send (200 OK) else
            send Exception (404 not found).
        """
        try:
            # check if cached item is stored or not.
            cached_item = cache.get('django_drf_social_link_footer_cache')
            if cached_item:
                return Response(cached_item, status=status.HTTP_200_OK)
            
            link = SocialLinksFooterCategory.objects.prefetch_related('sociallinks_footer').defer('created_at','updated_at')
            serializer = SocialLinksFooterViewSerializer(instance=link, many=True)
            cache.set('django_drf_social_link_footer_cache', serializer.data, timeout=CACHE_TIMEOUT)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)

class TitleFooterView(APIView):
    """Responsible for sending data to footer title in the frontend from the backend.

    Args:
        APIView (Class): Django Rest Framework(DRF) API View.
    """
    def get(self, request):
        """fetch footer title from the backend to the frontend (GET method).

        Args:
            request (request): Django request argument.

        Returns:
            Response: Send Response as json if response ok then send (200 OK) else
            send Exception (404 not found).
        """
        try:
            # check if cached item is stored or not.
            cached_item = cache.get('django_drf_title_footer_cache')
            if cached_item:
                return Response(cached_item, status=status.HTTP_200_OK)
            
            link = TitleFooter.objects.defer('created_at','updated_at')
            serializer = TitleFooterViewSerializer(instance=link, many=True)
            cache.set('django_drf_title_footer_cache', serializer.data, timeout=CACHE_TIMEOUT)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class CopyRightFooterView(APIView):
    """Responsible for sending data to footer copyright in the frontend from the backend.

    Args:
        APIView (Class): Django Rest Framework(DRF) API View.
    """
    def get(self, request):
        """fetch footer copyright from the backend to the frontend (GET method).

        Args:
            request (request): Django request argument.

        Returns:
            Response: Send Response as json if response ok then send (200 OK) else
            send Exception (404 not found).
        """
        try:
            # check if cached item is stored or not.
            cached_item = cache.get('django_drf_copyright_footer_cache')
            if cached_item:
                return Response(cached_item, status=status.HTTP_200_OK)
            
            link = CopyRightFooter.objects.defer('created_at','updated_at')
            serializer = CopyRightFooterViewSerializer(instance=link, many=True)
            cache.set('django_drf_copyright_footer_cache', serializer.data, timeout=CACHE_TIMEOUT)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)


class AboutUsView(APIView):
    """Responsible for sending data to About us in the frontend from the backend.

    Args:
        APIView (Class): Django Rest Framework(DRF) API View.
    """
    def get(self, request):
        """fetch about us from the backend to the frontend (GET method).

        Args:
            request (request): Django request argument.

        Returns:
            Response: Send Response as json if response ok then send (200 OK) else
            send Exception (404 not found).
        """
        try:
            # check if cached item is stored or not.
            cached_item = cache.get('django_drf_about-us_page_cache')
            if cached_item:
                return Response(cached_item, status=status.HTTP_200_OK)
            
            about_us = AboutUs.objects.defer('created_at', 'updated_at')
            serializer = AboutUsViewsSerializer(instance=about_us, many=True)
            cache.set('django_drf_about-us_page_cache', serializer.data, timeout=CACHE_TIMEOUT)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)


class PrivacyPolicyView(APIView):
    """Responsible for sending data to privacy policy in the frontend from the backend.

    Args:
        APIView (Class): Django Rest Framework(DRF) API View.
    """
    def get(self, request):
        """fetch privacy policy from the backend to the frontend (GET method).

        Args:
            request (request): Django request argument.

        Returns:
            Response: Send Response as json if response ok then send (200 OK) else
            send Exception (404 not found).
        """
        try:
            # check if cached item is stored or not.
            cached_item = cache.get('django_drf_privacy-policy_page_cache')
            if cached_item:
                return Response(cached_item, status=status.HTTP_200_OK)
            
            privacy_policy = PrivacyPolicy.objects.defer('created_at', 'updated_at')
            serializer = PrivacyPolicyViewsSerializer(instance=privacy_policy, many=True)
            cache.set('django_drf_privacy-policy_page_cache', serializer.data, timeout=CACHE_TIMEOUT)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)
