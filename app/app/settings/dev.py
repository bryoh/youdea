from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = 'static'  # os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = 'media'  # os.path.join(BASE_DIR, 'media')

INSTALLED_APPS = INSTALLED_APPS + ['debug_toolbar']

MIDDLEWARE = MIDDLEWARE + ['debug_toolbar.middleware.DebugToolbarMiddleware']
INTERNAL_IPS = ("127.0.0.1", "172.17.0.1", "staging.herokuapp.com")

try:
    from .local import *
except ImportError:
    pass
