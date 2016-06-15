# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20150910_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainpageservice',
            name='url',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
    ]
