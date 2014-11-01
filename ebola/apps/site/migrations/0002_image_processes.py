# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('site', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='processes',
            field=sorl.thumbnail.fields.ImageField(null=True, upload_to=b'uploads/files', blank=True),
            preserve_default=True,
        ),
    ]
