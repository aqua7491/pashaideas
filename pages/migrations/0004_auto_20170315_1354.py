# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-15 13:54
from __future__ import unicode_literals

from django.db import migrations, models
import pages.models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_page_video_embed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='nav_color',
            field=models.CharField(default='#000000', max_length=7, validators=[pages.models.layout_validator]),
        ),
    ]
