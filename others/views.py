from django.shortcuts import render
from rest_framework.views import APIView

# Create your views here.
class TopBanner(APIView):
    def get(self, request):
        pass