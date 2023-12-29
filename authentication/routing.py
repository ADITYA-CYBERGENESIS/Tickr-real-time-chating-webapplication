from django.urls import path
from . import consumers


websocket_urlpatterns = [
    path('registration/ws',consumers.MyConsumer.as_asgi()),
]