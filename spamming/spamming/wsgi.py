"""
WSGI config for spamming project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os, sys, site

SITE_DIR = '/home/ubuntu/Spamming/spamming/'
site.addsitedir(SITE_DIR)
sys.path.append(SITE_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'spamming.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
