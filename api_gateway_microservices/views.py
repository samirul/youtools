import requests 
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import GenerateImagesSerializers, GetCommentsAndAnalysisCommentsSerializers

# text2image microservice

class text2image_generate_Image(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            access_token = request.COOKIES.get('access_token')
            serializer = GenerateImagesSerializers(data=request.data)
            if serializer.is_valid():
                text = serializer.validated_data.get("text")
                api_link = "http://localhost:81/generate-image/"
                req = requests.post(api_link, json={"text": text}, headers={'Authorization': f"Bearer {access_token}"}, timeout=60)
                if req.status_code == 401:
                    return Response({"msg": req.json()}, status=status.HTTP_401_UNAUTHORIZED)
                return Response({"msg": req.json()}, status=status.HTTP_200_OK)
            return Response({"error": "Something is wrong."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({"error": "Something is wrong."}, status=status.HTTP_400_BAD_REQUEST)
        

class text2Image_get_all_images(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            access_token = request.COOKIES.get('access_token')
            api_link = "http://localhost:81/all-images/"
            req = requests.get(api_link, headers={'Authorization': f"Bearer {access_token}"}, timeout=60)
            if req.status_code == 401:
                return Response({"msg": req.json()}, status=status.HTTP_401_UNAUTHORIZED)
            return Response({"msg": req.json()}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"error": "Something is wrong."}, status=status.HTTP_400_BAD_REQUEST)
        
    
class text2Image_get_single_image(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, ids):
        try:
            access_token = request.COOKIES.get('access_token')
            api_link = f"http://localhost:81/image/{ids}/"
            req = requests.get(api_link, headers={'Authorization': f"Bearer {access_token}"}, timeout=60)
            if req.status_code == 401:
                return Response({"msg": req.json()}, status=status.HTTP_401_UNAUTHORIZED)
            return Response({"msg": req.json()}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"error": "Something is wrong."}, status=status.HTTP_400_BAD_REQUEST)
        

class text2Image_delete_single_image(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request, ids):
        try:
            access_token = request.COOKIES.get('access_token')
            api_link = f"http://localhost:81/image/delete/{ids}/"
            req = requests.delete(api_link, headers={'Authorization': f"Bearer {access_token}"}, timeout=60)
            if req.status_code == 401:
                return Response({"msg": req.json()}, status=status.HTTP_401_UNAUTHORIZED)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            print(e)
            return Response({"error": "Something is wrong."}, status=status.HTTP_400_BAD_REQUEST)
        

class text2Image_task_status_progress(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, task_ids):
        try:
            access_token = request.COOKIES.get('access_token')
            api_link = f"http://localhost:81/task_status/{task_ids}/"
            req = requests.get(api_link, headers={'Authorization': f"Bearer {access_token}"}, timeout=60)
            if req.status_code == 401:
                return Response({"msg": req.json()}, status=status.HTTP_200_OK)
            return Response({"msg": req.json()}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"error": "Something is wrong."}, status=status.HTTP_400_BAD_REQUEST)


# sentiment-analysis microservice

class sentiment_analysis_fetch_comments_and_analysis(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            access_token = request.COOKIES.get('access_token')
            serializer = GetCommentsAndAnalysisCommentsSerializers(data=request.data)
            if serializer.is_valid():
                url = serializer.validated_data.get("url")
                max_len = serializer.validated_data.get("max_len")
                if not url:
                    raise ValueError("No url is found.")
                if not max_len:
                    raise ValueError("No Max length is found.")
                api_link = "http://localhost:82/analysis-youtube-comments/"
                req = requests.post(api_link, json={"url": url, "max_len": max_len}, headers={'Authorization': f"Bearer {access_token}"}, timeout=60)
                if req.status_code == 401:
                    return Response({"msg": req.json()}, status=status.HTTP_401_UNAUTHORIZED)
                return Response({"msg": req.json()}, status=status.HTTP_200_OK)
            return Response({"error": "Something is wrong."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({"error": "Something is wrong."}, status=status.HTTP_400_BAD_REQUEST)
        

class sentiment_analysis_fetch_all_results_by_single_category(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, ids):
        try:
            access_token = request.COOKIES.get('access_token')
            api_link = f"http://localhost:82/all-youtube-comments-results/{ids}/"
            req = requests.get(api_link, headers={'Authorization': f"Bearer {access_token}"}, timeout=60)
            if req.status_code == 401:
                return Response({"msg": req.json()}, status=status.HTTP_401_UNAUTHORIZED)
            return Response({"msg": req.json()}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"error": "Something is wrong."}, status=status.HTTP_400_BAD_REQUEST)
        

class sentiment_analysis_get_single_result_by_id(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, ids):
        try:
            access_token = request.COOKIES.get('access_token')
            api_link = f"http://localhost:82/get-youtube-comment-result/{ids}/"
            req = requests.get(api_link, headers={'Authorization': f"Bearer {access_token}"}, timeout=60)
            if req.status_code == 401:
                return Response({"msg": req.json()}, status=status.HTTP_401_UNAUTHORIZED)
            return Response({"msg": req.json()}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"error": "Something is wrong."}, status=status.HTTP_400_BAD_REQUEST)
        

class sentiment_analysis_delete_single_result_by_id(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request, ids):
        try:
            access_token = request.COOKIES.get('access_token')
            api_link = f"http://localhost:82/delete-comment/{ids}/"
            req = requests.delete(api_link, headers={'Authorization': f"Bearer {access_token}"}, timeout=60)
            if req.status_code == 401:
                return Response({"msg": req.json()}, status=status.HTTP_401_UNAUTHORIZED)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            print(e)
            return Response({"error": "Something is wrong."}, status=status.HTTP_400_BAD_REQUEST)
        
        
class sentiment_analysis_all_categories(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            access_token = request.COOKIES.get('access_token')
            api_link = f"http://localhost:82/all-categories/"
            req = requests.get(api_link, headers={'Authorization': f"Bearer {access_token}"}, timeout=60)
            if req.status_code == 401:
                return Response({"msg": req.json()}, status=status.HTTP_401_UNAUTHORIZED)
            return Response({"msg": req.json()}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"error": "Something is wrong."}, status=status.HTTP_400_BAD_REQUEST)
        
        
class sentiment_analysis_delete_single_category_by_id(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request, ids):
        try:
            access_token = request.COOKIES.get('access_token')
            api_link = f"http://localhost:82/delete-category/{ids}/"
            req = requests.delete(api_link, headers={'Authorization': f"Bearer {access_token}"}, timeout=60)
            if req.status_code == 401:
                return Response({"msg": req.json()}, status=status.HTTP_401_UNAUTHORIZED)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            print(e)
            return Response({"error": "Something is wrong."}, status=status.HTTP_400_BAD_REQUEST)
        

class sentiment_analysis_task_status_progress(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, task_ids):
        try:
            access_token = request.COOKIES.get('access_token')
            api_link = f"http://localhost:82/task_status/{task_ids}/"
            req = requests.get(api_link, headers={'Authorization': f"Bearer {access_token}"}, timeout=60)
            if req.status_code == 401:
                return Response({"msg": req.json()}, status=status.HTTP_200_OK)
            return Response({"msg": req.json()}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"error": "Something is wrong."}, status=status.HTTP_400_BAD_REQUEST)