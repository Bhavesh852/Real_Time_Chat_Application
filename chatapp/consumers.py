import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from .models import ChatMsg, ChatRoom

class ChatConsumer(WebsocketConsumer):


    def save_message(self, room_code, msg, sender):
        obj = ChatRoom.objects.get(room_code=room_code)
        ChatMsg.objects.create(room=obj, message=msg, sender=sender)

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_code']
        self.group_name = f'room_{self.room_name}'

        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )

        self.accept()

        self.send(text_data = json.dumps({
            'status' : 'connected'
        }))
    
    def receive(self, text_data):
        data = json.loads(text_data)

        payload = {'message' : data.get('message'), 'sender' : data.get('sender')}

        self.save_message(self.room_name, data.get('message'), data.get('sender'))
        async_to_sync(self.channel_layer.group_send)(
            f'room_{self.room_name}', {
                'type' : 'send_message', 
                'value' : json.dumps(payload)
            }
        )
    
    def disconnect(self, close_code):
        print(close_code)

    def send_message(self, text_data):
        msg = text_data.get('value')
        self.send(text_data = json.dumps({
            'payload' : json.loads(msg)
        }))
