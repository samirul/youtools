"""
    URL is for Views of microservices.
"""

from django.urls import path
from .views import (Text2ImageGenerateImage, Text2ImageGetAllImages,
Text2ImageGetSingleImageById, Text2ImageDeleteSingleImageById, Text2ImageTaskStatusProgressByTaskId,
SentimentAnalysisFetchCommentsAndAnalysis,
SentimentAnalysisFetchAllResultsBySingleCategory, SentimentAnalysisGetSingleResultById,
SentimentAnalysisDeleteSingleResultById, SentimentAnalysisAllCategories,
SentimentAnalysisDeleteSingleCategoryById, SentimentAnalysisTaskStatusProgress)

urlpatterns = [
    # text2image-microservice
    path("generate_image/", Text2ImageGenerateImage.as_view()),
    path("images/", Text2ImageGetAllImages.as_view()),
    path("image/<str:ids>/", Text2ImageGetSingleImageById.as_view()),
    path("delete_image/<str:ids>/", Text2ImageDeleteSingleImageById.as_view()),
    path("task-status-image/<str:task_ids>/", Text2ImageTaskStatusProgressByTaskId.as_view()),

    # sentiment-analysis-microservice
    path("fetch_and_analysis/", SentimentAnalysisFetchCommentsAndAnalysis.as_view()),
    path("results/<str:ids>/", SentimentAnalysisFetchAllResultsBySingleCategory.as_view()),
    path("result/<str:ids>/", SentimentAnalysisGetSingleResultById.as_view()),
    path("delete_result/<str:ids>/", SentimentAnalysisDeleteSingleResultById.as_view()),
    path("categories/", SentimentAnalysisAllCategories.as_view()),
    path("delete_category/<str:ids>/", SentimentAnalysisDeleteSingleCategoryById.as_view()),
    path("task-status/<str:task_ids>/", SentimentAnalysisTaskStatusProgress.as_view()),
   
]
