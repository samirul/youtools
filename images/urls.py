from django.urls import path
from .views import Generate_Image

urlpatterns = [
    path("generate_image/", Generate_Image.as_view(), name='generate_image'),
]
