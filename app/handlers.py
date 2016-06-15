# -*- coding: utf-8 -*-
from __future__ import absolute_import

from datetime import datetime
import random

from django.conf import settings
from django.core.mail import send_mail
from django.template import Context
from django.template.loader import get_template


def handle_uploaded_file(f):
    """
    Управляет загрузкой файлов
    :param f: file
    :return: dict
    """
    try:
        extension = f.name.split('.')[-1]
        if extension in settings.UPLOAD_FILE_EXTENSIONS:
            file_name = datetime.now().strftime('%Y%m%d_%H%M%S') + "_" + ("%08x" % random.getrandbits(32)) + "." + extension
            destination = open(settings.UPLOADED_FILE_PATH + file_name, 'w')
            for chunk in f.chunks():
                destination.write(chunk)
            destination.close()
            return {'created': True, 'file_name': file_name}
        else:
            return {'error': 'File has wrong extension!'}
    except Exception as e:
        return {'error': e}


def send_email(title, template, email, context):
    msg_body = get_template(template).render(Context(context))
    try:
        send_mail(subject=title, message=msg_body, from_email=settings.EMAIL_HOST_USER, recipient_list=[email])
    except:
        pass