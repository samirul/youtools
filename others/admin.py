from django.contrib import admin
from .models import (TopBanner, QuickLinksFooter, NavigationLinksFooter, SocialLinksFooter,
                     TitleFooter, CopyRightFooter)

# Register your models here.
@admin.register(TopBanner)
class OthersModelAdmin(admin.ModelAdmin):
    list_display = [
      'id','banner_text'
    ]

@admin.register(QuickLinksFooter)
class QuickLinksFooterModelAdmin(admin.ModelAdmin):
    list_display = [
      'id','quicklinks_title','quicklinks_url'
    ]

@admin.register(NavigationLinksFooter)
class NavigationLinksFooterModelAdmin(admin.ModelAdmin):
    list_display = [
      'id','navigation_title','navigation_url'
    ]

@admin.register(SocialLinksFooter)
class SocialLinksFooterModelAdmin(admin.ModelAdmin):
    list_display = [
      'id','social_icon','social_url','social_label'
    ]

@admin.register(TitleFooter)
class TitleFooterModelAdmin(admin.ModelAdmin):
    list_display = [
      'id','footer_title','footer_description'
    ]

@admin.register(CopyRightFooter)
class CopyRightFooterModelAdmin(admin.ModelAdmin):
    list_display = [
      'id','copyright_footer'
    ]