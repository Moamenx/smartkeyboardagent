"""
WSGI config for ska project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

path = '/home/khaled/Downloads/Smartkeyboardagent-master'

import sys
sys.path.append(path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ska.settings")

application = get_wsgi_application()