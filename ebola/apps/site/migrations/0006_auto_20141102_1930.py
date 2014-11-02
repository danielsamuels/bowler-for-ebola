# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('site', '0005_auto_20141101_1314'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ('-timestamp',)},
        ),
        migrations.AlterField(
            model_name='image',
            name='ip_address',
            field=models.GenericIPAddressField(null=True, verbose_name=b'IP address', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='image',
            name='uuid',
            field=models.CharField(default=uuid.uuid4, max_length=36, serialize=False, verbose_name=b'UUID', primary_key=True),
            preserve_default=True,
        ),
    ]
