"""
Settings for local development.

These settings are not fast or efficient, but allow local servers to be run
using the django-admin.py utility.

This file should be excluded from version control to keep the settings local.
"""

import os
import os.path

from .base import *


# Run in debug mode.

DEBUG = True

TEMPLATE_DEBUG = DEBUG

THUMBNAIL_DEBUG = DEBUG


# Save media files to the user's Sites folder.

MEDIA_ROOT = os.path.expanduser(os.path.join("~/Sites", SITE_DOMAIN, "media"))
STATIC_ROOT = os.path.expanduser(os.path.join("~/Sites", SITE_DOMAIN, "static"))


# Use local server.

SITE_DOMAIN = "localhost:8000"

PREPEND_WWW = False


# Disable the template cache for development.

TEMPLATE_LOADERS = (
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
)


# Optional separate database settings
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "HOST": "localhost",
        "NAME": "ebola",
        "USER": "",
        "PASSWORD": "",
    },
}

# Mailtrip SMTP
EMAIL_HOST = 'mailtrap.io'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = '2525'
EMAIL_USE_TLS = True

# INSTALLED_APPS = INSTALLED_APPS + (
#     'debug_toolbar',
# )

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
