"""
WSGI config for pract3 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
from decouple import config

ENV_ID = config("PRACT3_ENV_ID", default="local")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'settings.env.{ENV_ID}')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
