from django.db import models

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page

# Create your models here.
class FlexPage(Page):
    """ Flexible page class """

    temlate = "flex/flex_page.html"
    # content = StreamField()
    subtitle = models.CharField(max_length=250, null=True, blank=True)
    content_panels = Page.content_panels + [FieldPanel("subtitle")]

    class Meta:  # noqa
        verbose_name = "Flex Page"
