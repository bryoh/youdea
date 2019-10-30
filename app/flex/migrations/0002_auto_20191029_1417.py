# Generated by Django 2.2.4 on 2019-10-29 14:17

from django.db import migrations
import streams.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import wagtailmedia.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='content',
            field=wagtail.core.fields.StreamField([('title_and_text', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your title', required=True)), ('text', wagtail.core.blocks.TextBlock(help_text='Add additional text', required=True))])), ('full_richtext', streams.blocks.RichTextBlock()), ('card', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your title', required=True)), ('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('trackno', wagtail.core.blocks.CharBlock(help_text='Track Number', required=True)), ('track', wagtailmedia.blocks.AbstractMediaChooserBlock(help_text='Upload/Choose audio file', required=True)), ('title', wagtail.core.blocks.CharBlock(help_text='Episode Title', max_length=40, required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Upload/Choose Image', required=False))])))]))], blank=True, null=True),
        ),
    ]
