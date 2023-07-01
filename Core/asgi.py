"""
ASGI config for Core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from chatapp.consumers import ChatConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Core.settings')

application = get_asgi_application()

ws_patterns = [
    path('chat/send/<room_code>', ChatConsumer)
]

application = ProtocolTypeRouter({
    'websocket' : URLRouter(ws_patterns)
})
