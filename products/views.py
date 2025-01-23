from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import ProductList
from .serializers import ProductViewsSerializer

# Create your views here.

class ProductViews(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            products = ProductList.objects.defer('created_at','updated_at')
            serializer = ProductViewsSerializer(instance=products, many=True)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception:
            return Response({'errors': 'No product is found.'}, status=status.HTTP_204_NO_CONTENT)
        
class ProductFrontViews(APIView):
    def get(self, request):
        try:
            products = ProductList.objects.defer('created_at','updated_at')
            serializer = ProductViewsSerializer(instance=products, many=True)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception:
            return Response({'errors': 'No product is found.'}, status=status.HTTP_204_NO_CONTENT)