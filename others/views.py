"""
    DRF Other views for send data to api from backend to frontend for banners and footers.
"""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import (TopBannerViewSerializer, LinksFooterViewSerializer,
                          SocialLinksFooterViewSerializer, TitleFooterViewSerializer, CopyRightFooterViewSerializer)
from .models import (TopBanner, LinksFooterCategory,
                     TitleFooter, CopyRightFooter, SocialLinksFooterCategory)

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
            top_banner = TopBanner.objects.defer('created_at','updated_at')
            serializer = TopBannerViewSerializer(instance=top_banner, many=True)
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
            link = LinksFooterCategory.objects.prefetch_related('links_footer').defer('created_at','updated_at')
            serializer = LinksFooterViewSerializer(instance=link, many=True)
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
            link = SocialLinksFooterCategory.objects.prefetch_related('sociallinks_footer').defer('created_at','updated_at')
            serializer = SocialLinksFooterViewSerializer(instance=link, many=True)
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
            link = TitleFooter.objects.defer('created_at','updated_at')
            serializer = TitleFooterViewSerializer(instance=link, many=True)
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
            link = CopyRightFooter.objects.defer('created_at','updated_at')
            serializer = CopyRightFooterViewSerializer(instance=link, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)



