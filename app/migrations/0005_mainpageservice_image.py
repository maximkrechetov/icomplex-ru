# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_mainpageservice_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainpageservice',
            name='image',
            field=models.ImageField(default='', upload_to=b''),
            preserve_default=False,
        ),
    ]
