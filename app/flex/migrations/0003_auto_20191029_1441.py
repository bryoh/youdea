# Generated by Django 2.2.4 on 2019-10-29 14:41

from django.db import migrations
import streams.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0002_auto_20191029_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='content',
            field=wagtail.core.fields.StreamField([('title_and_text', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your title', required=True)), ('text', wagtail.core.blocks.TextBlock(help_text='Add additional text', required=True))])), ('full_richtext', streams.blocks.RichTextBlock()), ('card', wagtail.core.blocks.StructBlock([('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('trackno', wagtail.core.blocks.CharBlock(help_text='Track Number', required=True)), ('title', wagtail.core.blocks.CharBlock(help_text='Episode Title', max_length=40, required=True)), ('track', wagtail.core.blocks.ChooserBlock(help_text='Upload/Choose audio file', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Upload/Choose Image', required=False))])))]))], blank=True, null=True),
        ),
    ]
