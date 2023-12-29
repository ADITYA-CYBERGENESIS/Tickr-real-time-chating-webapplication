from django.contrib import admin
from .models import ChatThread, ChatMessage,GroupChatMessage,GroupChatThread

admin.site.register(ChatMessage)
admin.site.register(ChatThread)
admin.site.register(GroupChatMessage)
admin.site.register(GroupChatThread)