# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-15 13:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20170315_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='video_embed',
            field=models.TextField(blank=True, null=True),
        ),
    ]
