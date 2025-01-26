"""
    Added Microservice Architecture api links(API Gateway).
"""
import requests 
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import GenerateImagesSerializers, GetCommentsAndAnalysisCommentsSerializers

# text2image microservice

class Text2ImageGenerateImage(APIView):
    """Generate Image from the text.

    Args:
        APIView (Class): Django Rest Framework(DRF) API View.

    """
    permission_classes = [IsAuthenticated]
    def post(self, request):
        """ Will send POST request to the api server for generating image.

        Args:
            request (Parameters): Django request.

        Returns:
            Response: If user is not logged in and then will return Not authorized (401).
            If user is logged in and no error is occurred and then will return OK (200) and json data.
            If user is logged in or even not logged in and some error occurred then will
            return Bad Request (400).
        """
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
        

class Text2ImageGetAllImages(APIView):
    """Retrieve all the images.

    Args:
        APIView (Class): Django Rest Framework(DRF) API View.

    """
    permission_classes = [IsAuthenticated]
    def get(self, request):
        """Will send GET request to the api server for getting all the images.

        Args:
            request (Parameters): Django request.

        Returns:
            Response: If user is not logged in and then will return Not authorized (401).
            If user is logged in and no error is occurred and then will return OK (200) and json data.
            If user is logged in or even not logged in and some error occurred then will
            return Bad Request (400).
        """
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
        
    
class Text2ImageGetSingleImageById(APIView):
    """Retrieve single image.

    Args:
        APIView (Class): Django Rest Framework(DRF) API View.

    """
    permission_classes = [IsAuthenticated]
    def get(self, request, ids):
        """Will send GET request to the api server for getting single image by id.

        Args:
            request (Parameters): Django request.
            ids (Parameters): Image id.

        Returns:
            Response: If user is not logged in and then will return Not authorized (401).
            If user is logged in and no error is occurred and then will return OK (200) and json data.
            If user is logged in or even not logged in and some error occurred then will
            return Bad Request (400).
        """
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
        

class Text2ImageDeleteSingleImageById(APIView):
    """Delete single image.

    Args:
        APIView (Class): Django Rest Framework(DRF) API View.

    """
    permission_classes = [IsAuthenticated]
    def delete(self, request, ids):
        """Will send DELETE request to the api server for delete single image by id.

        Args:
            request (Parameters): Django request.
            ids (Parameters): Image id.

        Returns:
            Response: If user is not logged in and then will return Not authorized (401).
            If user is logged in and no error is occurred and then will return no content (204) and no json data.
            If user is logged in or even not logged in and some error occurred then will
            return Bad Request (400).
        """
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
        

class Text2ImageTaskStatusProgressByTaskId(APIView):
    """Image generation celery task progress.

    Args:
        APIView (Class): Django Rest Framework(DRF) API View.

    """
    permission_classes = [IsAuthenticated]
    def get(self, request, task_ids):
        """Will send GET request to the api server for getting celery task progress.


        Args:
            request (Parameters): Django request.
            task_ids (Parameters): Celery Task Id.

        Returns:
            Response: If user is not logged in and then will return Not authorized (401).
            If user is logged in and no error is occurred and then will return OK (200) and json data.
            If user is logged in or even not logged in and some error occurred then will
            return Bad Request (400).
        """
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

class SentimentAnalysisFetchCommentsAndAnalysis(APIView):
    """Sentiment-Analysis from youtube comments.

    Args:
        APIView (Class): Django Rest Framework(DRF) API View.

    """
    permission_classes = [IsAuthenticated]
    def post(self, request):
        """Will send POST request to analysis comments from youtube.

        Args:
            request (Parameters): Django request.

        Raises:
            ValueError (URL): Throw if no url is found.
            ValueError (MAX_LEN): Throw if no Max length is found.

        Returns:
            Response: If user is not logged in and then will return Not authorized (401).
            If user is logged in and no error is occurred and then will return OK (200) and json data.
            If user is logged in or even not logged in and some error occurred then will
            return Bad Request (400).
        """
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
        

class SentimentAnalysisFetchAllResultsBySingleCategory(APIView):
    """Retrieve analyzed results by categories.

    Args:
        APIView (Class): Django Rest Framework(DRF) API View.

    """
    permission_classes = [IsAuthenticated]
    def get(self, request, ids):
        """Will send GET request to the api server for getting all the results.

        Args:
            request (Parameters): Django request.
            ids (Parameters): Category id.

        Returns:
            Response: If user is not logged in and then will return Not authorized (401).
            If user is logged in and no error is occurred and then will return OK (200) and json data.
            If user is logged in or even not logged in and some error occurred then will
            return Bad Request (400).
        """
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
        

class SentimentAnalysisGetSingleResultById(APIView):
    """Retrieve analyzed single result by id.

    Args:
        APIView (Class): Django Rest Framework(DRF) API View.

    """
    permission_classes = [IsAuthenticated]
    def get(self, request, ids):
        """Will send GET request to the api server for getting single result.

        Args:
            request (Parameters): Django request.
            ids (Parameters): Analyzed id.

        Returns:
            Response: If user is not logged in and then will return Not authorized (401).
            If user is logged in and no error is occurred and then will return OK (200) and json data.
            If user is logged in or even not logged in and some error occurred then will
            return Bad Request (400).
        """
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
        

class SentimentAnalysisDeleteSingleResultById(APIView):
    """Delete analyzed result by id.

    Args:
        APIView (Class): Django Rest Framework(DRF) API View.

    """
    permission_classes = [IsAuthenticated]
    def delete(self, request, ids):
        """Will send DELETE request to the api server for deleting a single result.

        Args:
            request (Parameters): Django request.
            ids (Parameters): Analyzed id.

        Returns:
            Returns:
            Response: If user is not logged in and then will return Not authorized (401).
            If user is logged in and no error is occurred and then will return no content (204) and no json data.
            If user is logged in or even not logged in and some error occurred then will
            return Bad Request (400).
        """
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
        
        
class SentimentAnalysisAllCategories(APIView):
    """Get all the categories.

    Args:
        APIView (Class): Django Rest Framework(DRF) API View.

    """
    permission_classes = [IsAuthenticated]
    def get(self, request):
        """Will send GET request to the api server for getting all the categories.

        Args:
            request (Parameters): Django request.

        Returns:
            Response: If user is not logged in and then will return Not authorized (401).
            If user is logged in and no error is occurred and then will return OK (200) and json data.
            If user is logged in or even not logged in and some error occurred then will
            return Bad Request (400).
        """
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
        
        
class SentimentAnalysisDeleteSingleCategoryById(APIView):
    """Delete category.

    Args:
        APIView (_type_): _description_

    """
    permission_classes = [IsAuthenticated]
    def delete(self, request, ids):
        """Will send DELETE request to the api server for deleting a single category.

        Args:
            request (Parameters): Django request.
            ids (Parameters): category id.

        Returns:
            Returns:
            Response: If user is not logged in and then will return Not authorized (401).
            If user is logged in and no error is occurred and then will return no content (204) and no json data.
            If user is logged in or even not logged in and some error occurred then will
            return Bad Request (400).
        """
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
        

class SentimentAnalysisTaskStatusProgress(APIView):
    """Sentiment analysis celery task progress.

    Args:
        APIView (Class): Django Rest Framework(DRF) API View.

    """
    permission_classes = [IsAuthenticated]
    def get(self, request, task_ids):
        """Will send GET request to the api server for getting celery task progress.

        Args:
            request (Parameters): Django request.
            task_ids (Parameters): Celery Task Id.

        Returns:
            Response: If user is not logged in and then will return Not authorized (401).
            If user is logged in and no error is occurred and then will return OK (200) and json data.
            If user is logged in or even not logged in and some error occurred then will
            return Bad Request (400).
        """
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