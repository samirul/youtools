from django.urls import path
from .views import TopBannerView
urlpatterns = [
    path("top-banner/", TopBannerView.as_view()),
 
]


