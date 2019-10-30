from wagtail.core import blocks
from wagtailmedia.edit_handlers import MediaChooserPanel

from wagtail.images.blocks import ImageChooserBlock
from wagtailmedia.blocks import AbstractMediaChooserBlock


class TitleAndTextBlock(blocks.StructBlock):
    """Title and text and nothing else."""

    title = blocks.CharBlock(required=True, help_text="Add your title")
    text = blocks.TextBlock(required=True, help_text="Add additional text")

    class Meta:  # noqa
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"


class RichTextBlock(blocks.RichTextBlock):
    """ Richtext with all the features """

    class Meta:  # noqa
        template = "streams/richtext_block.html"
        icon = "edit"
        label = "Full Richtext"


class CardBlock(blocks.StructBlock):
    """Card with title text and media"""

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("trackno", blocks.CharBlock(required=True, help_text="Track Number")),
                ('title', blocks.CharBlock(required=True, max_length=40, help_text='Episode Title')),
                ("track", AbstractMediaChooserBlock(required=True, help_text="Upload/Choose audio file")),
                ("image", ImageChooserBlock(required=False, help_text='Upload/Choose Image')),
            ]
        )
    )

    class Meta:  # noqa
        template = "streams/card_block.html"
        js = "cardblock.js"
        icon = "placeholder"
        label = "Podcasts"
