"""
Django settings for cliCodec project.

Generated by 'django-admin startproject' using Django 3.2.25.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path
import datetime
import logging
from logging.handlers import TimedRotatingFileHandler 

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Get the parent directory of the base directory of your Django project
LOGS_DIR = os.path.join(BASE_DIR, 'pixie_logger')  # Define the log directory
os.makedirs(LOGS_DIR, exist_ok=True)  # Ensure the log directory exists

# Generate a timestamp for the log file name
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
LOG_FILENAME = os.path.join(LOGS_DIR, f'cliCodec_{timestamp}.log')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-g4*a9^mdc&9bl*+$xvdvn-brvq*wnnvlgh7g#7_7+*(2oiub$)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'cliCodec',
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

ROOT_URLCONF = 'cliCodec.urls'

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

WSGI_APPLICATION = 'cliCodec.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


two_days_ago = datetime.datetime.now() - datetime.timedelta(days=2)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'timed': {
            'level': 'INFO',  # Set level to INFO
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': LOG_FILENAME,  # Store logs in a file with timestamp in the name
            'formatter': 'verbose',
            'when': 'midnight',  # Rotate logs daily
            'backupCount': (datetime.datetime.now() - two_days_ago).days + 1,  # Keep logs for at least 2 days
        },
    },
    'formatters': {
        'verbose': {
            'format': '%(asctime)s - %(levelname)s - %(message)s'
        },
    },
    'loggers': {
        '': {
            'handlers': ['timed'],
            'level': 'INFO',  # Set level to INFO
            'propagate': False,
        },
        'django': {
            'handlers': ['timed'],
            'level': 'INFO',  # Set level to INFO
            'propagate': False,
        },
        'cliCodec.connectNE_cli': {  # Log messages only from the connectNE module
            'handlers': ['timed'],
            'level': 'INFO',  # Set level to INFO
            'propagate': False,
        },
        'cliCodec.sendRCV_cli': {  # Log messages only from the connectNE module
            'handlers': ['timed'],
            'level': 'INFO',  # Set level to INFO
            'propagate': False,
        },
        'cliCodec.disconnectNe_cli': {  # Log messages only from the connectNE module
            'handlers': ['timed'],
            'level': 'INFO',  # Set level to INFO
            'propagate': False,
        },
    },
}