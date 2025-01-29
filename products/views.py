"""
    Product Views is for showing cards in the frontend.
"""

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import ProductList
from .serializers import ProductViewsSerializer

# Create your views here.

class ProductViews(APIView):
    """View this product on the product page(Auth required).

    Args:
        APIView (Class): Django Rest Framework(DRF) API View.

    """
    permission_classes = [IsAuthenticated]
    def get(self, request):
        """Get request for viewing data on products frontend.

        Args:
            request (Parameters): Django request.

        Returns:
            Response: Return status code (200 OK) if no error or exception is happening.
            Return status code (204) if no content is found.
        """
        try:
            products = ProductList.objects.defer('created_at','updated_at')
            serializer = ProductViewsSerializer(instance=products, many=True)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception:
            return Response({'errors': 'No product is found.'}, status=status.HTTP_204_NO_CONTENT)
        
class ProductFrontViews(APIView):
    """View this product on the home page(No Auth required).

    Args:
        APIView (Class): Django Rest Framework(DRF) API View.
    """
    def get(self, request):
        """Get request for viewing data on the frontpage(Home) frontend.

        Args:
            request (Parameters): Django request.

        Returns:
            Response: Return status code (200 OK) if no error or exception is happening.
            Return status code (204) if no content is found.
        """
        try:
            products = ProductList.objects.defer('created_at','updated_at')
            serializer = ProductViewsSerializer(instance=products, many=True)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception:
            return Response({'errors': 'No product is found.'}, status=status.HTTP_204_NO_CONTENT)