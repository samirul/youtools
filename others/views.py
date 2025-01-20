from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import (TopBannerViewSerializer, LinksFooterCategoryViewSerializer, LinksFooterViewSerializer,
                          SocialLinksFooterViewSerializer, TitleFooterViewSerializer, CopyRightFooterViewSerializer)
from .models import (TopBanner, LinksFooterCategory, LinksFooter, SocialLinksFooter,
                     TitleFooter, CopyRightFooter)

# Create your views here.
class TopBannerView(APIView):
    def get(self, request):
        try:
            top_banner = TopBanner.objects.defer('created_at','updated_at')
            serializer = TopBannerViewSerializer(instance=top_banner, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)
        

class LinksFooterCategoryView(APIView):
    def get(self, request):
        try:
            link_category = LinksFooterCategory.objects.defer('created_at','updated_at')
            serializer = LinksFooterCategoryViewSerializer(instance=link_category, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class LinksFooterView(APIView):
    def get(self, request):
        try:
            link = LinksFooter.objects.defer('created_at','updated_at')
            serializer = LinksFooterViewSerializer(instance=link, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class SocialLinksFooterView(APIView):
    def get(self, request):
        try:
            link = SocialLinksFooter.objects.defer('created_at','updated_at')
            serializer = SocialLinksFooterViewSerializer(instance=link, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)

class TitleFooterView(APIView):
    def get(self, request):
        try:
            link = TitleFooter.objects.defer('created_at','updated_at')
            serializer = TitleFooterViewSerializer(instance=link, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class CopyRightFooterView(APIView):
    def get(self, request):
        try:
            link = CopyRightFooter.objects.defer('created_at','updated_at')
            serializer = CopyRightFooterViewSerializer(instance=link, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)
