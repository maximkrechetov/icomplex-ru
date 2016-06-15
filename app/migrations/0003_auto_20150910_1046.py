# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_mainpageservice'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainpageservice',
            name='active',
            field=models.BooleanField(default='', verbose_name='\u0410\u043a\u0442\u0438\u0432\u043d\u044b\u0439'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mainpageservice',
            name='title',
            field=models.CharField(max_length=256, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a'),
        ),
    ]
