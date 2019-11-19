from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ['*']


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
INSTALLED_APPS += ['django_sass', 'debug_toolbar']

MIDDLEWARE = MIDDLEWARE + ['debug_toolbar.middleware.DebugToolbarMiddleware']
INTERNAL_IPS = ("127.0.0.1", "172.17.0.1", "staging.herokuapp.com")

WAGTAIL_CACHE = False

try:
    from .local_settings import *
except ImportError:
    pass
