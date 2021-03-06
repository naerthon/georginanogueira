# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 13:42
from __future__ import unicode_literals

import apps.core.models
from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20171123_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image_thumbnail',
            field=imagekit.models.fields.ProcessedImageField(upload_to=apps.core.models.Images.image_thumb_path),
        ),
    ]
