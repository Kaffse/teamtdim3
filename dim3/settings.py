"""
Django settings for dim3 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SETTINGS_DIR = os.path.dirname(__file__)
PROJECT_PATH = os.path.join(SETTINGS_DIR, os.pardir)
PROJECT_PATH = os.path.abspath(PROJECT_PATH)
TEMPLATE_PATH = os.path.join(PROJECT_PATH, 'template')
STATIC_PATH = os.path.join(PROJECT_PATH, 'static')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

AUTH_PROFILE_MODULE = 'dim3app.UserAcc'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8$$y&xf6s1pmy0#yc$2&m0$0@1@@@j1w12089i+(e3!_ee6wm!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'aggressiveBackpack',
    'south',
    'django_markdown',
    'keyboard_shortcuts',
    'taggit',
    'taggit_templatetags',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'dim3.urls'

WSGI_APPLICATION = 'dim3.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

ADMINS = (
    ('P. Yordanov', 'ppyordanov@yahoo.com'),
    ('Keir Smith', 'kaffse@gmail.com'),
    ('Ally Weir', 'ally.pcgf@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': PROJECT_PATH + '/dim3db',  # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        # 'USER': 'dim3',
        # 'PASSWORD': 't34mt34mt',
        # 'HOST': '127.0.0.1',                   # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        # 'PORT': '',                      # Set to empty string for default.
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-GB'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    STATIC_PATH,
)

TEMPLATE_DIRS = (
TEMPLATE_PATH,
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

LOGIN_URL = '/aggressiveBackpack/login.html/'

# START keyboard_shortcuts settings #
HOTKEYS = [
            {'keys': 'g + d',  # go to dashboard
            'link': '/aggressiveBackpack/dashboard/'},
            {'keys': 'n + p',  #make a new project
            'link': '/aggressiveBackpack/new_project/'},
            {'keys': 'g + s',  #go to settings
            'link': '/aggressiveBackpack/settings/'},
            {'keys': 'n + l',  #make a new list
            'js': 'alert(\'This keyboard shortcut will let you make a new list\');'},
        ]
SPECIAL_DISABLED = True
# END keyboard_shortcuts settings #
