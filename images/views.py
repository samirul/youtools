import requests as rq
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import GenerateImagesSerializers

class Generate_Image(APIView):
    def post(self, request):
        try:
            serializer = GenerateImagesSerializers(data=request.data)
            if serializer.is_valid():
                text = serializer.validated_data.get("text")
                api_link = "http://127.0.0.1:5000/generate-image"
                req = rq.post(api_link, json={"text": text})
                return Response({"msg": req.json()}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
