from django.urls import path
from .views import (TopBannerView, LinksFooterCategoryView,
                    LinksFooterView, SocialLinksFooterView, TitleFooterView,
                    CopyRightFooterView)
urlpatterns = [
    path("top-banner/", TopBannerView.as_view()),
    path("link-category/", LinksFooterCategoryView.as_view()),
    path("links/", LinksFooterView.as_view()),
    path("social-links/", SocialLinksFooterView.as_view()),
    path("footer-title/", TitleFooterView.as_view()),
    path("copyright-text/", CopyRightFooterView.as_view()),
]


