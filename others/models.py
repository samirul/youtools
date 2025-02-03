"""
    Required models for others app (ORM) so can make databases in PostgresDB (migrate)
    without writing raw SQL commands.
"""

from django.db import models
from BaseID.models import BaseIdModel

# Create your models here.
class TopBanner(BaseIdModel):
    """ORM model for topbanner database.

    Args:
        BaseIdModel (Custom abstract Django model): Custom BaseID django abstract model
        for needing some attributes to inheritate(BaseIdModel will not migrate in the database,
        will be just abstract class).

    Returns:
        String: Will return string text banner so can view in the admin control pannel.
    """
    banner_image = models.ImageField(upload_to='media/homepage')
    banner_text = models.TextField(max_length=500)
    objects = models.Manager()

    class Meta:
        """Added custom model name."""
        verbose_name_plural = "Top banner"

    def __str__(self):
        return str(self.banner_text)
    
class LinksFooterCategory(BaseIdModel):
    """ORM model for Links category on the footer database.

    Args:
        BaseIdModel (Custom abstract Django model): Custom BaseID django abstract model
        for needing some attributes to inheritate(BaseIdModel will not migrate in the database,
        will be just abstract class).

    Returns:
        String: Will return string category names so can view in the admin control pannel.
    """
    category_name = models.CharField(max_length=100)
    objects = models.Manager()

    class Meta:
        """Added custom model name."""
        verbose_name_plural = "Links footer categories"
    
    def __str__(self):
        return str(self.category_name)
    
class SocialLinksFooterCategory(BaseIdModel):
    """ORM model for Social Links category on the footer database.

    Args:
        BaseIdModel (Custom abstract Django model): Custom BaseID django abstract model
        for needing some attributes to inheritate(BaseIdModel will not migrate in the database,
        will be just abstract class).

    Returns:
        String: Will return string social category names so can view in the admin control pannel.
    """
    social_category_name = models.CharField(max_length=100)
    objects = models.Manager()

    class Meta:
        """Added custom model name."""
        verbose_name_plural = "Social Links footer categories"
    
    def __str__(self):
        return str(self.social_category_name)
    
class LinksFooter(BaseIdModel):
    """ORM model for Links on the footer database.

    Args:
        BaseIdModel (Custom abstract Django model): Custom BaseID django abstract model
        for needing some attributes to inheritate(BaseIdModel will not migrate in the database,
        will be just abstract class).

    Returns:
        String: Will return string links titles so can view in the admin control pannel.
    """
    links_title = models.CharField(max_length=60)
    links_url = models.CharField(max_length=200)
    category = models.ForeignKey(LinksFooterCategory, on_delete=models.CASCADE, related_name='links_footer')
    objects = models.Manager()

    class Meta:
        """Added custom model name."""
        verbose_name_plural = "Links footer"

    def __str__(self):
        return str(self.links_title)

    
class SocialLinksFooter(BaseIdModel):
    """ORM model for social Links on the footer database.

    Args:
        BaseIdModel (Custom abstract Django model): Custom BaseID django abstract model
        for needing some attributes to inheritate(BaseIdModel will not migrate in the database,
        will be just abstract class).

    Returns:
        String: Will return string social labels so can view in the admin control pannel.
    """
    social_icon = models.CharField(max_length=40)
    social_url = models.CharField(max_length=200)
    social_label = models.CharField(max_length=60)
    category = models.ForeignKey(SocialLinksFooterCategory, on_delete=models.CASCADE, related_name='sociallinks_footer')
    objects = models.Manager()

    class Meta:
        """Added custom model name."""
        verbose_name_plural = "Social links footer"

    def __str__(self):
        return str(self.social_label)
    
class TitleFooter(BaseIdModel):
    """ORM model for footer title name on the footer database.

    Args:
        BaseIdModel (Custom abstract Django model): Custom BaseID django abstract model
        for needing some attributes to inheritate(BaseIdModel will not migrate in the database,
        will be just abstract class).

    Returns:
        String: Will return string footer titles so can view in the admin control pannel.
    """
    footer_title = models.CharField(max_length=200)
    footer_description = models.TextField(max_length=500)
    objects = models.Manager()

    class Meta:
        """Added custom model name."""
        verbose_name_plural = "Title footer"

    def __str__(self):
        return str(self.footer_title)
    
class CopyRightFooter(BaseIdModel):
    """ORM model for footer copytight name on the footer database.

    Args:
        BaseIdModel (Custom abstract Django model): Custom BaseID django abstract model
        for needing some attributes to inheritate(BaseIdModel will not migrate in the database,
        will be just abstract class).

    Returns:
        String: Will return string copyright footer so can view in the admin control pannel.
    """
    copyright_footer = models.CharField(max_length=200)
    objects = models.Manager()

    class Meta:
        """Added custom model name."""
        verbose_name_plural = "Copyright footer"

    def __str__(self):
        return str(self.copyright_footer)
