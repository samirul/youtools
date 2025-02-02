"""
  Added models from others app inside admin so can register inside control panel(can view data from
  django admin panel).
"""
from django.contrib import admin
from .models import (TopBanner, LinksFooterCategory, SocialLinksFooterCategory,
                    LinksFooter, SocialLinksFooter,
                    TitleFooter, CopyRightFooter)

# Register your models here.
@admin.register(TopBanner)
class TopBannerModelAdmin(admin.ModelAdmin):
    """ Register TopBanner model.

    Args:
        admin (class ModelAdmin): For registering in the admin panel.
    """
    list_display = [
        'id','banner_text'
      ]

@admin.register(LinksFooterCategory)
class LinksFooterCategoryModelAdmin(admin.ModelAdmin):
    """ Register LinksFooterCategory model.

    Args:
        admin (class ModelAdmin): For registering in the admin panel.
    """
    list_display = [
      'id','category_name'
    ]

@admin.register(SocialLinksFooterCategory)
class SocialLinksFooterCategoryModelAdmin(admin.ModelAdmin):
    """ Register SocialLinksFooterCategory model.

    Args:
        admin (class ModelAdmin): For registering in the admin panel.
    """
    list_display = [
      'id','social_category_name'
    ]

@admin.register(LinksFooter)
class LinksFooterModelAdmin(admin.ModelAdmin):
    """ Register LinksFooter model.

    Args:
        admin (class ModelAdmin): For registering in the admin panel.
    """
    list_display = [
      'id','links_title','category'
    ]

@admin.register(SocialLinksFooter)
class SocialLinksFooterModelAdmin(admin.ModelAdmin):
    """ Register SocialLinksFooter model.

    Args:
        admin (class ModelAdmin): For registering in the admin panel.
    """
    list_display = [
      'id','social_label'
    ]

@admin.register(TitleFooter)
class TitleFooterModelAdmin(admin.ModelAdmin):
    """ Register TitleFooter model.

    Args:
        admin (class ModelAdmin): For registering in the admin panel.
    """
    list_display = [
      'id','footer_title'
    ]

@admin.register(CopyRightFooter)
class CopyRightFooterModelAdmin(admin.ModelAdmin):
    """ Register CopyRightFooter model.

    Args:
        admin (class ModelAdmin): For registering in the admin panel.
    """
    list_display = [
      'id','copyright_footer'
    ]