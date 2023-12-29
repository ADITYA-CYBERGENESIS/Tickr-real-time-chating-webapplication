import json
from channels.consumer import AsyncConsumer
from customuserml.models import User
from channels.db import database_sync_to_async

@database_sync_to_async
def is_username_taken(username):
    return User.objects.filter(username=username).exists()

@database_sync_to_async
def is_email_taken(email):
    return User.objects.filter(email=email).exists() 

class MyConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print('connected', event)
        await self.send({
            'type': 'websocket.accept'
        })

    async def websocket_receive(self, event):
        try:
            print('receive', event) 
            received_data = json.loads(event['text'])
            if received_data.get('is') == 'username':
                username = received_data.get('username')
                print(username)
                result = await is_username_taken(username)
                if not result:
                    data_to_be_sent = 1  # available
                else:
                    data_to_be_sent = 2  # not available

                response = {
                    'type': 'websocket.send',
                    'text': json.dumps({'is': 'username', 'availability': data_to_be_sent})
                }

                await self.send(response)
            elif received_data.get('is') == 'email':
                email = received_data.get('email')
                result = await is_email_taken(email)
                if not result:
                    data_to_be_sent = 1  # available
                else:
                    data_to_be_sent = 2  # not available
                response = {
                    'type': 'websocket.send',
                    'text': json.dumps({'is': 'email', 'availability': data_to_be_sent})
                }
                await self.send(response)

        except Exception as e:
            # Handle the exception, you can log it or send an error response to the client
            print(f"An error occurred: {e}")
            error_response = {'error': 'An error occurred while processing the request.'}
            await self.send(error_response) 

    async def websocket_disconnect(self, event):
        print('disconnect', event)
