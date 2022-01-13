"""
WSGI config for longnosebros project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# try:
#     os.environ['DJANGO_SETTINGS_MODULE']
# except KeyError:
print('MADE IT TO THE WSGI SETTINGS @@@@@@@@@@@@@@@@')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'longnosebros.settings.production')

application = get_wsgi_application()
