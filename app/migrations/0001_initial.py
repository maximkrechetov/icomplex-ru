# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import bitfield.models
import app.models
import django.core.validators
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailContact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=64, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('pages', bitfield.models.BitField(((b'contacts', '\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430 \u043a\u043e\u043d\u0442\u0430\u043a\u0442\u043e\u0432'), (b'vacancy', '\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430 \u0432\u0430\u043a\u0430\u043d\u0441\u0438\u0439'), (b'service', '\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430 \u0443\u0441\u043b\u0443\u0433')), default=None, verbose_name='\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u044b \u043f\u043e\u043a\u0430\u0437\u0430')),
                ('email', models.EmailField(max_length=64, verbose_name='Email')),
                ('icq', models.CharField(max_length=32, verbose_name='ICQ')),
                ('skype', models.CharField(max_length=32, verbose_name='Skype')),
            ],
            options={
                'verbose_name': '\u041a\u0443\u0434\u0430 \u043f\u0438\u0441\u0430\u0442\u044c',
                'verbose_name_plural': '\u0411\u043b\u043e\u043a\u0438 "\u041a\u0443\u0434\u0430 \u043f\u0438\u0441\u0430\u0442\u044c"',
            },
        ),
        migrations.CreateModel(
            name='FeedbackMessage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, null=True, verbose_name='\u0418\u043c\u044f', blank=True)),
                ('phone', app.models.PhoneField(max_length=64, null=True, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d', validators=[django.core.validators.RegexValidator(regex=b'(8|\\+7)[\\s-]?\\(?\\d{3}\\)?[\\s-]?\\d{1}[\\s-]?\\d{1}[\\s-]?\\d{1}[\\s-]?\\d{1}[\\s-]?\\d{1}[\\s-]?\\d{1}[\\s-]?\\d$', message='\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043e\u0440\u0440\u0435\u043a\u0442\u043d\u044b\u0439 \u0442\u0435\u043b\u0435\u0444\u043e\u043d')])),
                ('email', models.EmailField(max_length=128, verbose_name='Email')),
                ('reason', models.IntegerField(default=1)),
                ('message', models.TextField(verbose_name='\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435 \u043e\u0442 \u0433\u043e\u0441\u0442\u044f')),
            ],
            options={
                'abstract': False,
                'verbose_name': '\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435 \u043e\u0431\u0440\u0430\u0442\u043d\u043e\u0439 \u0441\u0432\u044f\u0437\u0438',
                'verbose_name_plural': '\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f \u043e\u0431\u0440\u0430\u0442\u043d\u043e\u0439 \u0441\u0432\u044f\u0437\u0438',
            },
        ),
        migrations.CreateModel(
            name='FeedbackMessageFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('filename', models.CharField(max_length=64)),
                ('feedback_message', models.ForeignKey(to='app.FeedbackMessage')),
            ],
            options={
                'verbose_name': '\u041f\u0440\u0438\u043a\u0440\u0435\u043f\u043b\u0435\u043d\u043d\u044b\u0439 \u0444\u0430\u0439\u043b',
                'verbose_name_plural': '\u041f\u0440\u0438\u043a\u0440\u0435\u043f\u043b\u0435\u043d\u043d\u044b\u0435 \u0444\u0430\u0439\u043b\u044b',
            },
        ),
        migrations.CreateModel(
            name='PageBlock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=16, verbose_name='\u041a\u043b\u044e\u0447')),
                ('name', models.CharField(max_length=64, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('show', models.BooleanField(default=True, verbose_name='\u041f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c')),
            ],
            options={
                'verbose_name': '\u0411\u043b\u043e\u043a \u043d\u0430 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0435',
                'verbose_name_plural': '\u0411\u043b\u043e\u043a\u0438 \u043d\u0430 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0435',
            },
        ),
        migrations.CreateModel(
            name='PhoneContact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=64, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('pages', bitfield.models.BitField(((b'contacts', '\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430 \u043a\u043e\u043d\u0442\u0430\u043a\u0442\u043e\u0432'), (b'vacancy', '\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430 \u0432\u0430\u043a\u0430\u043d\u0441\u0438\u0439'), (b'service', '\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430 \u0443\u0441\u043b\u0443\u0433')), default=None, verbose_name='\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u044b \u043f\u043e\u043a\u0430\u0437\u0430')),
                ('phone', app.models.PhoneField(max_length=32, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d', validators=[django.core.validators.RegexValidator(regex=b'(8|\\+7)[\\s-]?\\(?\\d{3}\\)?[\\s-]?\\d{1}[\\s-]?\\d{1}[\\s-]?\\d{1}[\\s-]?\\d{1}[\\s-]?\\d{1}[\\s-]?\\d{1}[\\s-]?\\d$', message='\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043e\u0440\u0440\u0435\u043a\u0442\u043d\u044b\u0439 \u0442\u0435\u043b\u0435\u0444\u043e\u043d')])),
                ('name', models.CharField(max_length=64, verbose_name='\u0424\u0418\u041e')),
            ],
            options={
                'verbose_name': '\u041a\u0443\u0434\u0430 \u0437\u0432\u043e\u043d\u0438\u0442\u044c',
                'verbose_name_plural': '\u0411\u043b\u043e\u043a\u0438 "\u041a\u0443\u0434\u0430 \u0437\u0432\u043e\u043d\u0438\u0442\u044c"',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.IntegerField(null=True, verbose_name='\u041f\u043e\u0437\u0438\u0446\u0438\u044f', blank=True)),
                ('page_title', models.CharField(max_length=256, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b', blank=True)),
                ('addition_page_title', models.CharField(max_length=256, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u043a\u043d\u043e\u043f\u043a\u0438', blank=True)),
                ('url', app.models.UrlField(db_index=True, unique=True, max_length=64, verbose_name='url', validators=[django.core.validators.RegexValidator(regex=b'^[-_0-9a-z]+$', message='\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043e\u0440\u0440\u0435\u043a\u0442\u043d\u044b\u0439 \u0430\u0434\u0440\u0435\u0441 \u0441\u0441\u044b\u043b\u043a\u0438')])),
                ('display_name', models.CharField(max_length=256, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('cost', models.PositiveIntegerField(default=0, verbose_name='\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c', blank=True)),
                ('description', ckeditor.fields.RichTextField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0443\u0441\u043b\u0443\u0433\u0438')),
                ('show', models.NullBooleanField(verbose_name='\u041f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c \u0443\u0441\u043b\u0443\u0433\u0443')),
                ('parent', models.ForeignKey(verbose_name='\u041f\u043e\u0434\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f', blank=True, to='app.Service', null=True)),
            ],
            options={
                'ordering': ['position'],
                'abstract': False,
                'verbose_name': '\u0423\u0441\u043b\u0443\u0433\u0430',
                'verbose_name_plural': '\u0423\u0441\u043b\u0443\u0433\u0438',
            },
        ),
        migrations.CreateModel(
            name='ServiceFeedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, null=True, verbose_name='\u0418\u043c\u044f', blank=True)),
                ('phone', app.models.PhoneField(max_length=64, null=True, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d', validators=[django.core.validators.RegexValidator(regex=b'(8|\\+7)[\\s-]?\\(?\\d{3}\\)?[\\s-]?\\d{1}[\\s-]?\\d{1}[\\s-]?\\d{1}[\\s-]?\\d{1}[\\s-]?\\d{1}[\\s-]?\\d{1}[\\s-]?\\d$', message='\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043e\u0440\u0440\u0435\u043a\u0442\u043d\u044b\u0439 \u0442\u0435\u043b\u0435\u0444\u043e\u043d')])),
                ('email', models.EmailField(max_length=128, verbose_name='Email')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
                ('service_url', models.CharField(max_length=64, null=True, verbose_name='\u0423\u0441\u043b\u0443\u0433\u0430-\u043e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u0435\u043b\u044c', blank=True)),
            ],
            options={
                'ordering': ['-create_date'],
                'abstract': False,
                'verbose_name': '\u0417\u0430\u044f\u0432\u043a\u0430 \u043d\u0430 \u0443\u0441\u043b\u0443\u0433\u0443',
                'verbose_name_plural': '\u0417\u0430\u044f\u0432\u043a\u0438 \u043d\u0430 \u0443\u0441\u043b\u0443\u0433\u0443',
            },
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('out_url', models.CharField(max_length=128, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430')),
                ('banner_url', models.CharField(max_length=128, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0431\u0430\u043d\u043d\u0435\u0440')),
                ('show', models.BooleanField(default=True, verbose_name='\u041f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c')),
            ],
            options={
                'verbose_name': '\u0421\u043b\u0430\u0439\u0434 \u043d\u0430 \u0433\u043b\u0430\u0432\u043d\u043e\u0439',
                'verbose_name_plural': '\u0421\u043b\u0430\u0439\u0434\u044b \u043d\u0430 \u0433\u043b\u0430\u0432\u043d\u043e\u0439',
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.IntegerField(null=True, verbose_name='\u041f\u043e\u0437\u0438\u0446\u0438\u044f', blank=True)),
                ('job_title', models.CharField(max_length=128, verbose_name='\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c')),
                ('short_description', models.CharField(max_length=512, verbose_name='\u041a\u0440\u0430\u0442\u043a\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('requirements', ckeditor.fields.RichTextField(verbose_name='\u0422\u0440\u0435\u0431\u043e\u0432\u0430\u043d\u0438\u044f')),
                ('job_functions', ckeditor.fields.RichTextField(verbose_name='\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u043d\u044b\u0435 \u043e\u0431\u044f\u0437\u0430\u043d\u043d\u043e\u0441\u0442\u0438')),
                ('job_conditions', ckeditor.fields.RichTextField(verbose_name='\u0423\u0441\u043b\u043e\u0432\u0438\u044f \u0440\u0430\u0431\u043e\u0442\u044b')),
                ('pay', models.CharField(max_length=512, verbose_name='\u0417\u0430\u0440\u0430\u0431\u043e\u0442\u043d\u0430\u044f \u043f\u043b\u0430\u0442\u0430')),
                ('actual', models.BooleanField(default=True, verbose_name='\u0410\u043a\u0442\u0443\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u044c')),
                ('url', app.models.UrlField(blank=True, max_length=200, null=True, verbose_name='URL', validators=[django.core.validators.RegexValidator(regex=b'^[-_0-9a-z]+$', message='\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043e\u0440\u0440\u0435\u043a\u0442\u043d\u044b\u0439 \u0430\u0434\u0440\u0435\u0441 \u0441\u0441\u044b\u043b\u043a\u0438')])),
            ],
            options={
                'ordering': ['position'],
                'abstract': False,
                'verbose_name': '\u0412\u0430\u043a\u0430\u043d\u0441\u0438\u044f',
                'verbose_name_plural': '\u0412\u0430\u043a\u0430\u043d\u0441\u0438\u0438',
            },
        ),
    ]
