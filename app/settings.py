"""
Django settings for icomplex project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
globals().update(os.environ)

import dotenv
from getenv import env

# Place path to .env file here
dotenv.read_dotenv('.env')

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']

CACHES = {
    'default': {
        'BACKEND': env('CACHE_BACKEND'),
        'LOCATION': env('CACHE_LOCATION'),
    }
}

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'app',
    'compressor',
    'ckeditor',
    'django.contrib.sitemaps',
    'robots'
)

SITE_ID = 1

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'app.middleware.ForceDefaultLanguageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'app.urls'

WSGI_APPLICATION = 'app.webapp_uwsgi.application'
TEMPLATE_DIRS = env('TEMPLATE_DIRS')
LOCALE_PATHS = (os.path.join(BASE_DIR, 'locale'), )

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': env('DATABASE_ENGINE'),
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST': env('DATABASE_HOST'),
        'PORT': env('DATABASE_PORT')
    },
}

# EMAIL settings
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_USE_TLS = env('EMAIL_USE_TLS')
EMAIL_PORT = env('EMAIL_PORT')

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'ru'

LANGUAGES = (
    ('ru', 'Russian'),
    ('en', 'English'),
)

TIME_ZONE = 'Asia/Krasnoyarsk'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = env('STATIC_URL')
STATIC_ROOT = env('STATIC_ROOT')

UPLOADED_FILE_PATH = env('UPLOADED_FILE_PATH')

MEDIA_ROOT = UPLOADED_FILE_PATH
MEDIA_URL = '/files/'

UPLOAD_FILE_EXTENSIONS = ['jpg', 'png', 'jpeg', 'txt', 'doc', 'docx', 'odt', 'pdf']

CKEDITOR_UPLOAD_PATH = "uploads/"  # don't forget collectstatic
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_CONFIGS = {
    "default": {
        "removePlugins": "stylesheetparser",
        'allowedContent': True,
        'toolbar': 'full',
    }
}

COMPRESS_OFFLINE = False
COMPRESS_ENABLED = True
COMPRESS_URL = env('COMPRESS_URL')
COMPRESS_ROOT = env('COMPRESS_ROOT')
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]
COMPRESS_JS_FILTERS = [
    'compressor.filters.jsmin.SlimItFilter',
]
