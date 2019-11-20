from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ['*']
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
AWS_LOCATION = 'youdeastatic'
AWS_S3_FILE_OVERWRITE = False
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_DEFAULT_ACL = None
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
if AWS_ACCESS_KEY_ID:
    STATIC_URL = 'https://%s/%s/youdeastatic/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
    MEDIA_URL = 'https://%s/%s/youdeamedia/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
    STATIC_ROOT = 'static'  # os.path.join(BASE_DIR, 'static')
    MEDIA_ROOT = 'media'  # os.path.join(BASE_DIR, 'media')


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
INSTALLED_APPS += ['django_sass', 'debug_toolbar']

MIDDLEWARE = MIDDLEWARE + ['debug_toolbar.middleware.DebugToolbarMiddleware']
INTERNAL_IPS = ("127.0.0.1", "172.17.0.1", "staging.herokuapp.com")

WAGTAIL_CACHE = False

try:
    from .local_settings import *
except ImportError:
    pass
