from django.urls import path
from .views import ProductViews, ProductFrontViews
urlpatterns = [
    path("product-items/", ProductViews.as_view()),
    path("product-items/front/", ProductFrontViews.as_view()),
    
   
]
























