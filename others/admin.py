"""
  Added models from others app inside admin so can register inside control panel(can view data from
  django admin panel).
"""
from django.contrib import admin
from django.apps import apps
from .models import (TopBanner, BottomBanner, LinksFooterCategory, SocialLinksFooterCategory,
                    LinksFooter, SocialLinksFooter,
                    TitleFooter, CopyRightFooter, AboutUs, PrivacyPolicy)

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
    
    def has_add_permission(self, request):
      """Allow to post if there is no data inside specific table
      can only add rows once.

      Args:
          request (object): Django request.
      Returns:
          Boolean: If rows on table more than once then will return false else will return true.
      """
      if TopBanner.objects.count() >= 1:
          return False
      return True
    
@admin.register(BottomBanner)
class BottomBannerModelAdmin(admin.ModelAdmin):
    """ Register BottomBanner model.

    Args:
        admin (class ModelAdmin): For registering in the admin panel.
    """
    list_display = [
        'id','banner_text'
      ]
    
    def has_add_permission(self, request):
      """Allow to post if there is no data inside specific table
      can only add rows once.

      Args:
          request (object): Django request.
      Returns:
          Boolean: If rows on table more than once then will return false else will return true.
      """
      if BottomBanner.objects.count() >= 1:
          return False
      return True


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

    def has_add_permission(self, request):
      """Allow to post if there is no data inside specific table
      can only add rows once.

      Args:
          request (object): Django request.
      Returns:
          Boolean: If rows on table more than once then will return false else will return true.
      """
      if TitleFooter.objects.count() >= 1:
          return False
      return True


@admin.register(CopyRightFooter)
class CopyRightFooterModelAdmin(admin.ModelAdmin):
    """ Register CopyRightFooter model.

    Args:
        admin (class ModelAdmin): For registering in the admin panel.
    """
    list_display = [
      'id','copyright_footer'
    ]

    def has_add_permission(self, request):
      """Allow to post if there is no data inside specific table
      can only add rows once.

      Args:
          request (object): Django request.
      Returns:
          Boolean: If rows on table more than once then will return false else will return true.
      """
      if CopyRightFooter.objects.count() >= 1:
          return False
      return True
    

@admin.register(AboutUs)
class AboutUsModelAdmin(admin.ModelAdmin):
    """ Register AboutUs model.

    Args:
        admin (class ModelAdmin): For registering in the admin panel.
    """
    list_display = [
      'id','title','description'
    ]

    def has_add_permission(self, request):
      """Allow to post if there is no data inside specific table
      can only add rows once.

      Args:
          request (object): Django request.
      Returns:
          Boolean: If rows on table more than once then will return false else will return true.
      """
      if AboutUs.objects.count() >= 1:
          return False
      return True

@admin.register(PrivacyPolicy)
class PrivacyPolicyModelAdmin(admin.ModelAdmin):
    """ Register PrivacyPolicy model.

    Args:
        admin (class ModelAdmin): For registering in the admin panel.
    """
    list_display = [
      'id','title','description'
    ]

    def has_add_permission(self, request):
      """Allow to post if there is no data inside specific table
      can only add rows once.

      Args:
          request (object): Django request.
      Returns:
          Boolean: If rows on table more than once then will return false else will return true.
      """
      if PrivacyPolicy.objects.count() >= 1:
          return False
      return True
  
apps.get_app_config('others').verbose_name = "Others Management"
