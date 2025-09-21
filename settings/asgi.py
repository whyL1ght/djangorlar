"""
ASGI config for pract3 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
from decouple import config
from django.core.asgi import get_asgi_application

ENV_ID = config("PRACT3_ENV_ID", default="local")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'settings.env.{ENV_ID}')

application = get_asgi_application()
