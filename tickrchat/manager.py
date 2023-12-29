
from .models import ChatThread , ChatMessage
def create_thread(thread_name, user_one, user_two):
        return ChatThread.objects.create(thread_name=thread_name, user_one=user_one, user_two=user_two)

def save_chat(thread_name, sender, message,sent_time,sent_date):
        return ChatMessage.objects.create(thread=thread_name, sender=sender, message=message,sent_time=sent_time,sent_date=sent_date)
        