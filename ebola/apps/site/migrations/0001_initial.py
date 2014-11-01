# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('uuid', models.CharField(default=uuid.uuid4, max_length=36, serialize=False, primary_key=True)),
                ('image', sorl.thumbnail.fields.ImageField(upload_to=b'uploads/files')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
