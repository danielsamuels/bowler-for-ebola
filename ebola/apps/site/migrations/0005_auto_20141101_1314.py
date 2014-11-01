# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('site', '0004_auto_20141101_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='ip_address',
            field=models.GenericIPAddressField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='image',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now, auto_now_add=True),
            preserve_default=True,
        ),
    ]
