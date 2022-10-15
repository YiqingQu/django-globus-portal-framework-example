"""
Django settings for myportal project.

Generated by 'django-admin startproject' using Django 3.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import logging
from pathlib import Path
from myportal import fields

log = logging.getLogger(__name__)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep all secret keys used in production secret!
# You can generate a secure secret key with `openssl rand -hex 32`
SECRET_KEY = 'django-insecure-47f(ub2qs-n!b@&&)tis&l$&qf1%^@&jy-95jx!bahqrm^19m2'
# Your portal credentials for enabling user login via Globus Auth
SOCIAL_AUTH_GLOBUS_KEY = ''
SOCIAL_AUTH_GLOBUS_SECRET = ''

# This is a general Django setting if views need to redirect to login
# https://docs.djangoproject.com/en/3.2/ref/settings/#login-url
LOGIN_URL = '/login/globus'

# This dictates which scopes will be requested on each user login
SOCIAL_AUTH_GLOBUS_SCOPE = [
    'urn:globus:auth:scope:search.api.globus.org:all',
]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


SEARCH_INDEXES = {
    'my-search-index': {
        'uuid': '4dcf50b9-14e7-4994-be36-6c6b11a73cd2',
        'name': 'My Search Index',
        'fields': [
            ('dc', fields.dc),
            ('title', fields.title),
            ('formatted_search_results', fields.formatted_search_results),
            ('formatted_files', fields.formatted_files),
        ],
        'facets': [
            {
                'name': 'Publisher',
                'field_name': 'dc.publisher',
                'size': 10,
                'type': 'terms'
            },
            {
                'name': 'Type',
                'field_name': 'dc.subjects.subject',
                'size': 10,
                'type': 'terms'
            },
            {
                'name': 'Type',
                'field_name': 'dc.formats',
                'size': 10,
                'type': 'terms'
            },
            {
                'name': 'File Size (Bytes)',
                'type': 'numeric_histogram',
                'field_name': 'files.length',
                'size': 10,
                'histogram_range': {'low': 5000, 'high': 10000},
            },
            {
                "name": "Dates",
                "field_name": "dc.dates.date",
                "type": "date_histogram",
                "date_interval": "hour",
            },
        ],
    },
    'demo-index': {
        'uuid': '43e540e1-dbd9-4723-a67a-b44b60621338',
        'name': 'My Search Index Demo',
        'fields': [
            ('extension', fields.extension),
            ('date', fields.date),
            # ('title', fields.title),
            # ('formatted_search_results', fields.formatted_search_results),
            # ('formatted_files', fields.formatted_files),
        ],
        'facets': [
            {
                'name': 'Subject',
                'field_name': 'subject',
                'size': 10,
                'type': 'terms'
            },
            {
                "name": "Dates",
                "field_name": "date",
                "type": "date_histogram",
                "date_interval": "hour",
            },
        ],
    }
}


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'globus_portal_framework',
    'social_django',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'globus_portal_framework.middleware.ExpiredTokenMiddleware',
    'globus_portal_framework.middleware.GlobusAuthExceptionMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

# Authentication backends setup OAuth2 handling and where user data should be
# stored
AUTHENTICATION_BACKENDS = [
    'globus_portal_framework.auth.GlobusOpenIdConnect',
    'django.contrib.auth.backends.ModelBackend',
]

ROOT_URLCONF = 'myportal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'myportal' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'globus_portal_framework.context_processors.globals',
            ],
        },
    },
]

WSGI_APPLICATION = 'myportal.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


LOGGING = {
    'version': 1,
    'handlers': {
        'stream': {'level': 'DEBUG', 'class': 'logging.StreamHandler'},
    },
    'loggers': {
        'django': {'handlers': ['stream'], 'level': 'INFO'},
        'globus_portal_framework': {'handlers': ['stream'], 'level': 'INFO'},
        'myportal': {'handlers': ['stream'], 'level': 'INFO'},
    },
}

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

try:
    from .local_settings import *
except ImportError:
    expected_path = Path(__file__).resolve().parent / 'local_settings.py'
    log.warning(f'You should create a file for your secrets at {expected_path}')
