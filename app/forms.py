# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.forms import (CharField, FileField, Form, Textarea, FileInput, TextInput, ChoiceField, Select, EmailField,
                          EmailInput, ModelForm, HiddenInput)
from .models import ServiceFeedback


class FeedbackForm(Form):
    CHOICES = (
        (1, u'Хочу заказать услугу'),
        (2, u'Ищу работу'),
        (3, u'Нашел ошибку на сайте'),
        (4, u'Другое'),
    )

    name = CharField(max_length=120,
                     widget=TextInput({'class': "input",
                                       'placeholder': u"Имя"}))

    message = CharField(widget=Textarea({'class': "textarea feedback__textarea",
                                         'placeholder': u"О чем поговорим?"}))

    reason = ChoiceField(choices=CHOICES,
                         widget=Select({'class': 'select'}))

    email = EmailField(max_length=40,
                       widget=EmailInput({'class': "input",
                                          'placeholder': u"Например, example@mail.ru"}))

    phone = CharField(max_length=120,
                      widget=TextInput({'class': "input",
                                        'placeholder': u"Например, +79999999999"}),
                      required=False)

    file = FileField(label=u"Прикрепленные файлы",
                     widget=FileInput({'multiple': True}),
                     required=False)


class ServiceFeedbackForm(ModelForm):
    class Meta:
        model = ServiceFeedback
        fields = ['name', 'phone', 'email', 'service_url']

    service_url = CharField(max_length=64, widget=HiddenInput())


class LandingForm(Form):
    name = CharField(max_length=120,
                     widget=TextInput({'class': "lp-input input--black",
                                       'placeholder': u"Имя"}))

    phone = CharField(max_length=120,
                      widget=TextInput({'class': "lp-input input--black lp-input_data_phone",
                                        'placeholder': u"Телефон"}))
