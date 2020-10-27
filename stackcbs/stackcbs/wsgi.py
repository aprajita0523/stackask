"""
WSGI config for stackcbs project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stackcbs.settings')
if os.environ.get('DJANGO_ENV') == 'production':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stackcbs.production')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stackcbs.settings')  

application = get_wsgi_application()
