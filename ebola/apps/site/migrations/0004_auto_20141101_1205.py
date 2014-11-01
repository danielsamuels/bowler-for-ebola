# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import ebola.apps.site.models


class Migration(migrations.Migration):

    dependencies = [
        ('site', '0003_auto_20141101_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=sorl.thumbnail.fields.ImageField(upload_to=ebola.apps.site.models.upload_path),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='image',
            name='processed',
            field=sorl.thumbnail.fields.ImageField(null=True, upload_to=ebola.apps.site.models.processed_upload_path, blank=True),
            preserve_default=True,
        ),
    ]
