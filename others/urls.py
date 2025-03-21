"""
    Url for others app(frontend top banner and footer).
"""

from django.urls import path
from .views import (TopBannerView, BottomBannerView, LinksFooterView, SocialLinksFooterView, TitleFooterView,
                    CopyRightFooterView, AboutUsView, PrivacyPolicyView)
urlpatterns = [
    path("top-banner/", TopBannerView.as_view()),
    path("bottom-banner/", BottomBannerView.as_view()),
    path("links/", LinksFooterView.as_view()),
    path("social-links/", SocialLinksFooterView.as_view()),
    path("footer-title/", TitleFooterView.as_view()),
    path("copyright-text/", CopyRightFooterView.as_view()),
    path("about-us/", AboutUsView.as_view()),
    path("privacy-policy/", PrivacyPolicyView.as_view()),
]


