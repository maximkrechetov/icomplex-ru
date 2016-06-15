# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20150910_1144'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mainpageservice',
            options={'verbose_name': '\u0423\u0441\u043b\u0443\u0433\u0430 \u043d\u0430 \u0433\u043b\u0430\u0432\u043d\u043e\u0439 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0435', 'verbose_name_plural': '\u0423\u0441\u043b\u0443\u0433\u0438 \u043d\u0430 \u0433\u043b\u0430\u0432\u043d\u043e\u0439 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0435'},
        ),
        migrations.AddField(
            model_name='slide',
            name='caption',
            field=models.CharField(default=b'', max_length=1024, verbose_name='\u041f\u043e\u0434\u043f\u0438\u0441\u044c'),
        ),
        migrations.AddField(
            model_name='slide',
            name='caption_bg_color',
            field=models.CharField(default=b'ffffff', max_length=8, verbose_name='\u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u043e\u0434\u043f\u0438\u0441\u0438'),
        ),
        migrations.AlterField(
            model_name='mainpageservice',
            name='image_url',
            field=models.CharField(max_length=256, verbose_name='URL \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0438'),
        ),
        migrations.AlterField(
            model_name='mainpageservice',
            name='service_url',
            field=models.CharField(max_length=128, verbose_name='URL \u0443\u0441\u043b\u0443\u0433\u0438'),
        ),
    ]
