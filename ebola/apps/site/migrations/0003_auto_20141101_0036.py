# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site', '0002_image_processes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='processes',
            new_name='processed',
        ),
    ]
