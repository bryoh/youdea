"""
<<<<<<< HEAD:app/app/wsgi.py
WSGI config for app project.
=======
WSGI config for youdea project.
>>>>>>> c20cf9485f154246ae416bf0af206e6497224593:youdea/wsgi.py

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD:app/app/wsgi.py
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
=======
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
>>>>>>> c20cf9485f154246ae416bf0af206e6497224593:youdea/wsgi.py
"""

import os

from django.core.wsgi import get_wsgi_application

<<<<<<< HEAD:app/app/wsgi.py
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings.dev")
=======
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "youdea.settings")
>>>>>>> c20cf9485f154246ae416bf0af206e6497224593:youdea/wsgi.py

application = get_wsgi_application()
