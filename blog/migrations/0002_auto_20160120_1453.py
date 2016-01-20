# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='summary',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=b'', blank=True),
            preserve_default=True,
        ),
    ]
