from django.db import models
from BaseID.models import BaseIdModel

# Create your models here.
class TopBanner(BaseIdModel):
    banner_image = models.ImageField(upload_to='media/homepage')
    banner_text = models.TextField(max_length=500)
    objects = models.Manager()

    def __str__(self):
        return str(self.banner_text)
    
class LinksFooterCategory(BaseIdModel):
    category_name = models.CharField(max_length=100)
    objects = models.Manager()
    
    def __str__(self):
        return str(self.category_name)
    
class LinksFooter(BaseIdModel):
    links_title = models.CharField(max_length=60)
    links_url = models.CharField(max_length=200)
    category = models.ForeignKey(LinksFooterCategory, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return str(self.links_title)

    
class SocialLinksFooter(BaseIdModel):
    social_icon = models.CharField(max_length=40)
    social_url = models.CharField(max_length=200)
    social_label = models.CharField(max_length=60)
    category = models.ForeignKey(LinksFooterCategory, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return str(self.social_label)
    
class TitleFooter(BaseIdModel):
    footer_title = models.CharField(max_length=200)
    footer_description = models.TextField(max_length=500)
    category = models.ForeignKey(LinksFooterCategory, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return str(self.footer_title)
    
class CopyRightFooter(BaseIdModel):
    copyright_footer = models.CharField(max_length=200)
    objects = models.Manager()

    def __str__(self):
        return str(self.copyright_footer)