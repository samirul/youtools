from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TopBannerViewSerializer
from .models import TopBanner

# Create your views here.
class TopBannerView(APIView):
    def get(self, request):
        try:
            top_banner = TopBanner.objects.defer('created_at','updated_at')
            serializer = TopBannerViewSerializer(instance=top_banner, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)
