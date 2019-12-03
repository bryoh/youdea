from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
# DEBUG = True

# Add your site's domain name(s) here.
ALLOWED_HOSTS = ['*', '0.0.0.0', '127.0.0.1', 'localhost', 'www.youdea.co.uk', 'youdea-staging.herokuapp.com', 'youdea.herokuapp.com']

# To send email from the server, we recommend django_sendmail_backend
# Or specify your own email backend such as an SMTP server.
# https://docs.djangoproject.com/en/2.2/ref/settings/#email-backend
EMAIL_BACKEND = 'django_sendmail_backend.backends.EmailBackend'

# Default email address used to send messages from the website.
DEFAULT_FROM_EMAIL = 'Live Life <info@youdea.co.uk>'

# A list of people who get error notifications.
ADMINS = [('Administrator', 'admin@youdea.co.uk')]

# A list in the same format as ADMINS that specifies who should get broken link
# (404) notifications when BrokenLinkEmailsMiddleware is enabled.
MANAGERS = ADMINS

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
AWS_LOCATION = 'youdeastatic' + os.environ.get("DBNAME", "")
AWS_DEFAULT_ACL = None
AWS_S3_FILE_OVERWRITE = False
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATIC_URL = 'https://%s/%s/youdeastatic/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
MEDIA_URL = 'https://%s/%s/youdeamedia/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
GA_KEY_CONTENT = os.environ['GA_KEY_CONTENT']
GA_VIEW_ID = os.environ['GA_VIEW_ID']

if GA_VIEW_ID is not None:
    INSTALLED_APPS = INSTALLED_APPS + ['wagalytics']
# Email address used to send error messages to ADMINS.
SERVER_EMAIL = DEFAULT_FROM_EMAIL

# DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'HOST': 'localhost',
#        'NAME': 'app',
#        'USER': 'app',
#        'PASSWORD': '',
#        # If using SSL to connect to a cloud mysql database, spedify the CA as so.
#        'OPTIONS': { 'ssl': { 'ca': '/path/to/certificate-authority.pem' } },
#    }
# }

# Use template caching to speed up wagtail admin and front-end.
# Requires reloading web server to pick up template changes.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'wagtail.contrib.settings.context_processors.settings',
            ],
            'loaders': [
                (
                    'django.template.loaders.cached.Loader',
                    ['django.template.loaders.filesystem.Loader', 'django.template.loaders.app_directories.Loader'],
                )
            ],
        },
    }
]

try:
    from .local_settings import *
except ImportError:
    pass
