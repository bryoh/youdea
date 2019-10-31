from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtailmedia.edit_handlers import MediaChooserPanel
from streams import blocks


class HomePage(Page):
    """Home page model."""

    template = "home/home_page.html"
    max_count = 1

    banner_text = RichTextField()
    banner_author = RichTextField(features=["italic"])
    banner_image = models.ForeignKey("wagtailimages.Image", null=True, blank=True, on_delete=models.SET_NULL, related_name="+")
    content = StreamField([('card', blocks.CardBlock())], null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("banner_text"),
        FieldPanel("banner_author"),
        ImageChooserPanel("banner_image"),
        StreamFieldPanel('content'),
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
