"""
WSGI config for taskmate project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taskmate.settings')
# check if we need to use proxy config or not
# you can also define PROXY_URI in settings.py module
if settings.PROXY_ENABLE:
    proxy_uri = f"socks5h://{settings.PROXY_HOST}:{settings.PROXY_PORT}"
    os.environ['http_proxy'] = proxy_uri
    os.environ['https_proxy'] = proxy_uri
    
application = get_wsgi_application()
