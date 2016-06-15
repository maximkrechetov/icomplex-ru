# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.contrib import admin
from django.forms.widgets import TextInput

from bitfield.forms import BitFieldCheckboxSelectMultiple
from bitfield.admin import BitFieldListFilter

from .models import *


class PhoneWidget(TextInput):
    input_type = 'tel'


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'parent', 'url', 'cost', 'position']
    ordering = ['parent']
    list_filter = ['parent']


class PhoneContactAdmin(admin.ModelAdmin):
    formfield_overrides = {
        BitField: {'widget': BitFieldCheckboxSelectMultiple},
        PhoneField: {'widget': PhoneWidget(attrs={
            'placeholder': "+7 (___) ___-__-__",
            'pattern': PhoneField.r
        })}
    }
    fields = ('title', 'phone', 'name', 'pages')
    list_filter = [
        ('pages', BitFieldListFilter),
    ]
    list_display = ['title', 'phone', 'name']


class EmailContactAdmin(admin.ModelAdmin):
    formfield_overrides = {
        BitField: {'widget': BitFieldCheckboxSelectMultiple},
    }
    fields = ('title', 'email', 'icq', 'skype', 'pages')
    list_filter = [
        ('pages', BitFieldListFilter),
    ]
    list_display = ['title', 'email', 'icq']


class ServiceFeedbackAdmin(admin.ModelAdmin):
    date_hierarchy = 'create_date'
    readonly_fields = ['create_date']
    list_display = ['name', 'phone', 'email', 'create_date']


class MainPageServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'service_url', 'description', 'image_url', 'active']


admin.site.register(Vacancy)
admin.site.register(FeedbackMessage)
admin.site.register(FeedbackMessageFile)
admin.site.register(Service, ServiceAdmin)
admin.site.register(PageBlock)
admin.site.register(EmailContact, EmailContactAdmin)
admin.site.register(PhoneContact, PhoneContactAdmin)
admin.site.register(Slide)
admin.site.register(ServiceFeedback, ServiceFeedbackAdmin)
admin.site.register(MainPageService, MainPageServiceAdmin)
