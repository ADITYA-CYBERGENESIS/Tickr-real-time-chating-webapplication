import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from datetime import datetime
from tickrchat.models import ChatThread, ChatMessage
from datetime import datetime
import pytz
User = get_user_model()
def get_time():
    ist = pytz.timezone('Asia/Kolkata')
    current_time = datetime.now(ist).strftime("%H:%M")
    return current_time
def get_date():
    current_date = datetime.now().strftime("%Y/%m/%d")
    return current_date
@database_sync_to_async
def get_chat_thread(thread_name):
    try:
        chat_thread = ChatThread.objects.get(thread_name=thread_name)
        return chat_thread
    except ChatThread.DoesNotExist:
        return None
@database_sync_to_async
def create_thread(thread_name, user_one, user_two):
        return ChatThread.objects.create(thread_name=thread_name, user_one=user_one, user_two=user_two)
@database_sync_to_async
def get_user_by_id(user_id):
    try:
        user = User.objects.get(id=user_id)
        return user
    except User.DoesNotExist:
        print('nouser')
        return None
@database_sync_to_async
def get_user_by_username(username):
    try:
        user = User.objects.get(username=username)
        return user
    except User.DoesNotExist:
        return None
@database_sync_to_async
def save_chat(thread_name, sender, message,sent_time_12,sent_time_24,sent_date):
        return ChatMessage.objects.create(thread=thread_name, sender=sender, message=message,sent_time_12=sent_time_12,sent_time_24=sent_time_24,sent_date=sent_date)

class PersonalChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        my_id = self.scope['user'].id
        other_user_id = self.scope['url_route']['kwargs']['id']
        user1 =await get_user_by_id(my_id)
        user2 =await get_user_by_id(other_user_id) 
        if int(my_id) > int(other_user_id):
            self.room_name = f'{my_id}-{other_user_id}'
        else:
            self.room_name = f'{other_user_id}-{my_id}'

        self.room_group_name = 'chat_%s' % self.room_name
        chat_thread = await get_chat_thread(self.room_group_name)
        print(chat_thread)
        if chat_thread is None:
            if user1 is not None and user2 is not None and user2 != user1:
              chat_thread =await create_thread(self.room_group_name, user1, user2)
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        
        

    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        print(data)
        message = data['message']
        username = data['username']
        receiver = data['receiver']
        thread =await get_chat_thread(self.room_group_name)
        current_date =get_date()
        current_time =get_time()
        formatted_time_12 = (datetime.now().strftime("%I:%M %p")).lstrip('0')
        sender = await get_user_by_username(username)
        sfname = sender.first_name
        slname = sender.last_name
        await save_chat(thread,sender,message,formatted_time_12,current_time,current_date)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
                'sfname':sfname,
                'slname':slname
            }
        )
    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        sfname = event['sfname']
        slname = event['slname']
        formatted_time_12 = (datetime.now().strftime("%I:%M %p")).lstrip('0')
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'time':formatted_time_12,
            'sfname':sfname,
            'slname':slname
        }))

    async def disconnect(self, code):
        self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        

class GroupChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        my_id = self.scope['user']
        other_user_id = self.scope['url_route']['kwargs']['uniquegroupid']
        user1 =await get_user_by_id(my_id)
        if int(my_id) > int(other_user_id):
            self.room_name = f'{my_id}-{other_user_id}'
        else:
            self.room_name = f'{other_user_id}-{my_id}'

        self.room_group_name = 'chat_%s' % self.room_name
        chat_thread = await get_chat_thread(self.room_group_name)
        print(chat_thread)
        if chat_thread is None:
            if user1 is not None and user2 is not None and user2 != user1:
              chat_thread =await create_thread(self.room_group_name, user1, user2)
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        
        

    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        print(data)
        message = data['message']
        username = data['username']
        receiver = data['receiver']
        thread =await get_chat_thread(self.room_group_name)
        current_date =get_date()
        current_time =get_time()
        formatted_time_12 = (datetime.now().strftime("%I:%M %p")).lstrip('0')
        sender = await get_user_by_username(username)
        sfname = sender.first_name
        slname = sender.last_name
        await save_chat(thread,sender,message,formatted_time_12,current_time,current_date)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
                'sfname':sfname,
                'slname':slname
            }
        )
    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        sfname = event['sfname']
        slname = event['slname']
        formatted_time_12 = (datetime.now().strftime("%I:%M %p")).lstrip('0')
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'time':formatted_time_12,
            'sfname':sfname,
            'slname':slname
        }))

    async def disconnect(self, code):
        self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )        
        
@database_sync_to_async
def print_user_details(user):
    print(f"User Details - "
          f"Username: {user.username}, "
          f"Email: {user.email}, "
          f"Email Token: {user.email_token}, "
          f"Last Logout Time: {user.last_logout_time}, "
          f"Is Online: {user.is_online}, "
          f"Email Activated: {user.email_activated}, "
          f"Account Type: {user.account_type}, "
          f"Avatar: {user.avatar}, "
          f"Bio: {user.bio}, "
          f"Blocked List: {user.blocklist.all() if user.blocklist.exists() else None}")

class Userloginstatus(AsyncWebsocketConsumer):
    @database_sync_to_async
    def user_online(self,status):
        user = self.scope['user']
        user.is_online = status
        user.save()
        print(f'changed status of user to {status}')  
    async def connect(self):
        await self.accept()
        await self.user_online(True)
    async def receive(self):
        pass  
    async def disconnect(self,close_code):
        await self.user_online(False)
        

        
        

        