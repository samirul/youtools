from django.contrib import admin
from .models import (TopBanner, LinksFooterCategory, LinksFooter, SocialLinksFooter,
                     TitleFooter, CopyRightFooter)

# Register your models here.
@admin.register(TopBanner)
class OthersModelAdmin(admin.ModelAdmin):
    list_display = [
      'id','banner_text'
    ]

@admin.register(LinksFooterCategory)
class LinksFooterCategoryModelAdmin(admin.ModelAdmin):
    list_display = [
      'id','category_name'
    ]

@admin.register(LinksFooter)
class LinksFooterModelAdmin(admin.ModelAdmin):
    list_display = [
      'id','links_title','category'
    ]

@admin.register(SocialLinksFooter)
class SocialLinksFooterModelAdmin(admin.ModelAdmin):
    list_display = [
      'id','social_label'
    ]

@admin.register(TitleFooter)
class TitleFooterModelAdmin(admin.ModelAdmin):
    list_display = [
      'id','footer_title'
    ]

@admin.register(CopyRightFooter)
class CopyRightFooterModelAdmin(admin.ModelAdmin):
    list_display = [
      'id','copyright_footer'
    ]