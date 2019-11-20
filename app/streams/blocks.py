from wagtail.core import blocks
from wagtailmedia.edit_handlers import MediaChooserPanel

from wagtail.images.blocks import ImageChooserBlock
from wagtailmedia.blocks import AbstractMediaChooserBlock


class EpisodeBlock(blocks.StructBlock):
    """Episode Block with title media"""

    episodes = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("showno", blocks.FloatBlock(required=True, help_text="Track Number")),
                ("showmedia", AbstractMediaChooserBlock(required=True, help_text="Upload/Choose audio file")),
                ("showdate", blocks.DateBlock(required=False, help_text="Upload date")),
                ("shownotes", blocks.PageChooserBlock(required=False, help_text='Choose Shownotespage')),
            ]
        )
    )

    class Meta:  # noqa
        template = "streams/episodes_block.html"
        icon = "placeholder"
        label = "Pocast Episode"
