from .base import *
import os


ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1', 'localhost', 'www.youdea.co.uk', 'youdea.herokuapp.com']

DEBUG = False
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
AWS_LOCATION = 'static'
AWS_S3_FILE_OVERWRITE = False
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATIC_URL = 'https://%s/%s/static/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
MEDIA_URL = 'https://%s/%s/media/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
GA_KEY_CONTENT = os.environ['GA_KEY_CONTENT']
GA_VIEW_ID = os.environ['GA_VIEW_ID']

INSTALLED_APPS = INSTALLED_APPS + ['wagalytics']

try:
    from .local import *
except ImportError:
    pass
