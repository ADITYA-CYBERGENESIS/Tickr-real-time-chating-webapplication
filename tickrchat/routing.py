from django.urls import path
from . import consumers
websocket_urlpatterns=[
    path('ws/<int:id>/',consumers.PersonalChatConsumer.as_asgi()),
    path('ws/<str:uniquegroupid>',consumers.GroupChatConsumer.as_asgi()),
    path('ws/onlinestatus/',consumers.Userloginstatus.as_asgi()),
]