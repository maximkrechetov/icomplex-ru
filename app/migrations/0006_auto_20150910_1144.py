# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_mainpageservice_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mainpageservice',
            old_name='url',
            new_name='service_url',
        ),
        migrations.RemoveField(
            model_name='mainpageservice',
            name='image',
        ),
        migrations.AddField(
            model_name='mainpageservice',
            name='image_url',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
    ]
