from .base import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

INSTALLED_APPS += (
    'raven.contrib.django.raven_compat',
)

# Sentry config.
RAVEN_CONFIG = {
    'dsn': 'https://bbe540f965174d2da70ffacd097c59db:6345ee5cc988477489f817f54eed054e@app.getsentry.com/32482',
}

SERVER_IP = '178.62.96.52'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
)

COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter'
]


THUMBNAIL_DEBUG = False
