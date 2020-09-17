"""
Django settings for mic project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from pathlib import Path
import logging.config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('MIC_API_SECRET_KEY', '0(w&un#*n$)3_6ld=@cwhawb(ia72w8zl63$l%jn0j*wh0t%&b')

# HTTPS Setting
# Requests over HTTP are redirected to HTTPS
# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_api_key',
    'django_filters',
    'mic_api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mic.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mic.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'oracle_sid',
        'USER': 'oracle_user_name',
        'PASSWORD': 'oracle_pwd',
        'HOST': 'oracle_host',
        'PORT': 'oracle_port',
        'OPTIONS': {
            'threaded': True,
        },
    }
}

# Application Logging Setting

LOGGING_CONFIG = None
logging.config.dictConfig({
    "version": 1,
    "disable_existing_loggers": False,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s %(module)s %(process)d %(thread)d -- %(message)s'
        },
        'log_server_formatter': {
            '()': 'django.utils.log.ServerFormatter',
            'format': '[{server_time}] {message}',
            'datefmt' : '%Y-%m-%d %H:%M:%S',
            'style': '{',
        }
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        # 'mic_api_file': {
        #     'level': os.getenv('MIC_API_LOG_LEVEL', 'INFO'),
        #     'class': 'logging.FileHandler',
        #     'filename': os.getenv('MIC_API_LOG_FILE'),
        #     'formatter': 'verbose',
        # },
        'mic_api_console': {
            'level': os.getenv('MIC_API_LOG_LEVEL', 'INFO'),
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'django_console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'filters': ['require_debug_true'],
        },
        'django_server_console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'log_server_formatter',
        },
        'django_request_console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'log_server_formatter',
        },
    },
    'loggers': {
        'mic_api': {
            'handlers': [os.getenv('MIC_API_LOG_HANDLER', 'mic_api_console'),],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django': {
            'handlers': ['django_console'],
            'level': 'DEBUG',
        },
        'django.server': {
            'handlers': ['django_server_console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['django_request_console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
})

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework_api_key.permissions.HasAPIKey',
    'rest_framework.permissions.IsAuthenticated',),
    'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework_simplejwt.authentication.JWTAuthentication',)
}

API_KEY_CUSTOM_HEADER = "HTTP_X_API_KEY"

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_URL = '/assets/'
STATIC_ROOT = os.path.join(BASE_DIR, "static/")