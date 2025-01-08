from django.urls import path
from .views import (text2image_generate_Image, text2Image_get_all_images,
text2Image_get_single_image, text2Image_delete_single_image, text2Image_task_status_progress,
sentiment_analysis_fetch_comments_and_analysis,
sentiment_analysis_fetch_all_results_by_single_category, sentiment_analysis_get_single_result_by_id,
sentiment_analysis_delete_single_result_by_id, sentiment_analysis_all_categories,
sentiment_analysis_delete_single_category_by_id, sentiment_analysis_task_status_progress)

urlpatterns = [
    # text2image-microservice
    path("generate_image/", text2image_generate_Image.as_view()),
    path("images/", text2Image_get_all_images.as_view()),
    path("image/<str:ids>/", text2Image_get_single_image.as_view()),
    path("delete_image/<str:ids>/", text2Image_delete_single_image.as_view()),
    path("task-status-image/<str:task_ids>/", text2Image_task_status_progress.as_view()),

    # sentiment-analysis-microservice
    path("fetch_and_analysis/", sentiment_analysis_fetch_comments_and_analysis.as_view()),
    path("results/<str:ids>/", sentiment_analysis_fetch_all_results_by_single_category.as_view()),
    path("result/<str:ids>/", sentiment_analysis_get_single_result_by_id.as_view()),
    path("delete_result/<str:ids>/", sentiment_analysis_delete_single_result_by_id.as_view()),
    path("categories/", sentiment_analysis_all_categories.as_view()),
    path("delete_category/<str:ids>/", sentiment_analysis_delete_single_category_by_id.as_view()),
    path("task-status/<str:task_ids>/", sentiment_analysis_task_status_progress.as_view()),
   
]
