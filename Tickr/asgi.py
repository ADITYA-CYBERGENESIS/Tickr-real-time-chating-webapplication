"""
ASGI config for Tickr project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
import authentication.routing
import tickrchat.routing
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import include,path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Tickr.settings')
websocket_urlpatterns =(
    authentication.routing.websocket_urlpatterns+
    tickrchat.routing.websocket_urlpatterns+[
])
application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    )
})
