"""
WSGI config for mic project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os, sys
from os.path import dirname

from django.core.wsgi import get_wsgi_application

# To include the application's path in the Python search path
sys.path.append(dirname(dirname(__file__)))

# Tell WSGI application what default setting files to use
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mic.settings')

# Tell WSGI application what settings file to use
os.environ['DJANGO_SETTINGS_MODULE'] = 'mic.settings'

application = get_wsgi_application()


