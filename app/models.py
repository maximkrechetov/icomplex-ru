# -*- coding: utf-8 -*-
from __future__ import absolute_import
from pytils import translit

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.cache import cache
from django.core.validators import RegexValidator
from django.core.mail import send_mail
from django.conf import settings
from django.db.models.signals import post_save, post_delete
from django.core.exceptions import ValidationError

from bitfield import BitField
from ckeditor.fields import RichTextField


class PhoneField(models.CharField):
    r = r'(8|\+7)[\s-]?\(?\d{3}\)?[\s-]?\d{1}[\s-]?\d{1}[\s-]?\d{1}[\s-]?\d{1}[\s-]?\d{1}[\s-]?\d{1}[\s-]?\d$'

    def __init__(self, *args, **kwargs):
        phone_valid = RegexValidator(regex=self.r, message=u'Введите корректный телефон')
        kwargs['validators'] = [phone_valid]
        models.CharField.__init__(self, *args, **kwargs)


class UrlField(models.CharField):
    r = r'^[-_0-9a-z]+$'

    def __init__(self, *args, **kwargs):
        url_valid = RegexValidator(regex=self.r, message=u'Введите корректный адрес ссылки')
        kwargs['validators'] = [url_valid]
        models.CharField.__init__(self, *args, **kwargs)


class CustomPosition(models.Model):
    position = models.IntegerField(verbose_name=u'Позиция', null=True, blank=True)

    class Meta:
        abstract = True
        ordering = ['position']


class Contacts(models.Model):
    name = models.CharField(verbose_name=u'Имя', max_length=128, null=True, blank=True)
    phone = PhoneField(verbose_name=u'Телефон', max_length=64, null=True)
    email = models.EmailField(verbose_name=u'Email', max_length=128)

    def send_message(self):
        data = {
            'name': self.name,
            'phone': self.phone,
            'email': self.email
        }
        msg = u"""name: {name}\nphone: {phone}\nemail: {email}\n""".format(**data)
        if hasattr(self, 'message') and getattr(self, 'message', None):
            msg += u"message: %s" % self.message

        send_mail('feedback', msg, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])

    class Meta:
        abstract = True


class Vacancy(CustomPosition):
    job_title = models.CharField(max_length=128, verbose_name=u"Должность")
    short_description = models.CharField(max_length=512, verbose_name=u"Краткое описание")
    requirements = RichTextField(verbose_name=u"Требования")
    job_functions = RichTextField(verbose_name=u"Должностные обязанности")
    job_conditions = RichTextField(verbose_name=u"Условия работы")
    pay = models.CharField(max_length=512, verbose_name=u"Заработная плата")
    actual = models.BooleanField(default=True, verbose_name=u"Актуальность")
    url = UrlField(max_length=200, null=True, verbose_name=u"URL", blank=True)

    def __unicode__(self):
        return self.job_title

    class Meta(CustomPosition.Meta):
        verbose_name = u'Вакансия'
        verbose_name_plural = u'Вакансии'


@receiver(pre_save, sender=Vacancy)
def set_url_and_title_for_vacancy(instance, **kwargs):
    instance.url = translit.translify(instance.job_title.lower().replace(' ', '_'))


class FeedbackMessage(Contacts):
    reason = models.IntegerField(default=1)
    message = models.TextField(verbose_name=u"Сообщение от гостя")

    def __unicode__(self):
        return u"%s - %s" % (self.name, self.reason)

    @classmethod
    def create_feedback(cls, data):
        new_message = cls(
            name=data.get('name', ''),
            reason=data.get('reason', 1),
            message=data.get('message', ''),
            phone=data.get('phone', ''),
            email=data.get('email', '')
        )
        try:
            new_message.save()
            return new_message
        except Exception as e:
            raise ValidationError({"new_message": "Can't save new message"})

    class Meta(Contacts.Meta):
        verbose_name = u'Сообщение обратной связи'
        verbose_name_plural = u'Сообщения обратной связи'


class FeedbackMessageFile(models.Model):
    feedback_message = models.ForeignKey(FeedbackMessage)
    filename = models.CharField(max_length=64)

    def __unicode__(self):
        return u"%s - %s" % (self.filename, self.feedback_message.name)

    @classmethod
    def create_feedback_message_file(cls, feedback_message, file_name):
        new_file = cls(
            feedback_message=feedback_message,
            filename=file_name
        )
        try:
            new_file.save()
            return new_file
        except Exception:
            raise ValidationError({"new_message": "Can't save new file"})

    class Meta:
        verbose_name = u'Прикрепленный файл'
        verbose_name_plural = u'Прикрепленные файлы'


class Service(CustomPosition):
    parent = models.ForeignKey('self', null=True, blank=True, verbose_name=u'Подкатегория')
    page_title = models.CharField(max_length=256, verbose_name=u'Заголовок страницы', null=True, blank=True)
    addition_page_title = models.CharField(max_length=256, verbose_name=u'Заголовок кнопки', null=True, blank=True)
    url = UrlField(max_length=64, unique=True, verbose_name=u'url', db_index=True)
    display_name = models.CharField(max_length=256, verbose_name=u'Название')
    cost = models.PositiveIntegerField(verbose_name=u'Стоимость', default=0, blank=True)
    description = RichTextField(verbose_name=u'Описание услуги')
    show = models.NullBooleanField(verbose_name=u'Показывать услугу')

    @property
    def root(self):
        return not bool(self.parent)

    class Meta(CustomPosition.Meta):
        verbose_name = u'Услуга'
        verbose_name_plural = u'Услуги'

    def __unicode__(self):
        return self.display_name

    @property
    def children(self):
        return self.service_set.all()

    @property
    def neighbours(self):
        if self.parent:
            return self.parent.children.exclude(id=self.id)


class PageBlock(models.Model):
    code = models.CharField(max_length=16, verbose_name=u'Ключ')
    name = models.CharField(max_length=64, verbose_name=u'Название')
    show = models.BooleanField(default=True, verbose_name=u'Показывать')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Блок на странице'
        verbose_name_plural = u'Блоки на странице'


class BaseContact(models.Model):
    flags = (
        ('contacts', u'Страница контактов'),
        ('vacancy', u'Страница вакансий'),
        ('service', u'Страница услуг')
    )

    title = models.CharField(max_length=64, verbose_name=u'Заголовок')
    pages = BitField(flags=flags, verbose_name=u'Страницы показа')

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.title


class PhoneContact(BaseContact):
    phone = PhoneField(max_length=32, verbose_name=u'Телефон')
    name = models.CharField(max_length=64, verbose_name=u'ФИО')

    class Meta:
        verbose_name = u"Куда звонить"
        verbose_name_plural = u'Блоки "Куда звонить"'


class EmailContact(BaseContact):
    email = models.EmailField(max_length=64, verbose_name=u'Email')
    icq = models.CharField(max_length=32, verbose_name=u'ICQ')
    skype = models.CharField(max_length=32, verbose_name=u'Skype')

    class Meta:
        verbose_name = u'Куда писать'
        verbose_name_plural = u'Блоки "Куда писать"'


class Slide(models.Model):
    out_url = models.CharField(max_length=128, verbose_name=u"Ссылка")
    banner_url = models.CharField(max_length=128, verbose_name=u"Ссылка на баннер")
    show = models.BooleanField(default=True, verbose_name=u"Показывать")
    caption = models.CharField(max_length=1024, verbose_name=u'Подпись', default='')
    caption_bg_color = models.CharField(max_length=8, verbose_name=u'Цвет фона подписи', default='ffffff')

    class Meta:
        verbose_name = u'Слайд на главной'
        verbose_name_plural = u'Слайды на главной'

    def __unicode__(self):
        return self.out_url


class ServiceFeedback(Contacts):
    create_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name=u'Время создания')
    service_url = models.CharField(max_length=64, verbose_name=u'Услуга-отправитель', null=True, blank=True)

    class Meta(Contacts.Meta):
        ordering = ['-create_date']
        verbose_name = u'Заявка на услугу'
        verbose_name_plural = u'Заявки на услугу'

    get_absolute_url = lambda x: ''

    def __unicode__(self):
        return self.name


class MainPageService(models.Model):
    title = models.CharField(max_length=256, verbose_name=u'Заголовок')
    description = models.TextField(verbose_name=u'Описание услуги')
    active = models.BooleanField(verbose_name=u'Активный')
    service_url = models.CharField(max_length=128, verbose_name=u'URL услуги')
    image_url = models.CharField(max_length=256, verbose_name=u'URL картинки')

    class Meta:
        verbose_name = u'Услуга на главной странице'
        verbose_name_plural = u'Услуги на главной странице'

    def __unicode__(self):
        return self.title


@receiver([post_save, post_delete])
def recache(**kwargs):
    instance = kwargs.get('instance', None)
    if instance:
        if kwargs.get('created') and (isinstance(instance, ServiceFeedback) or isinstance(instance, FeedbackMessage)):
            try:
                instance.send_message()
            except Exception as e:
                print e
        cache.clear()
