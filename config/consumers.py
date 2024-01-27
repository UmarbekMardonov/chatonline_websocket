from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from rest_framework.authtoken.models import Token
# from rest_framework_simplejwt.tokens import Token
import json

from django.db import models

from chat.models import ChatPrivate, ChatPrivateMessage


class ChatPrivateConsumer(WebsocketConsumer):
    user = None
    chat = None

    def connect(self):
        # Join room group
        self.room_name = self.scope['url_route']['kwargs']['user_id']
        async_to_sync(self.channel_layer.group_add)(
            f"private_{self.room_name}", self.channel_name
        )

        headers = dict(self.scope["headers"])

        self.token = None
        if b"token" in headers:
            self.token = headers[b"token"].decode('utf-8')

        token = Token.objects.filter(key=self.token)

        if token.exists():
            user = token.first().user
            self.user = user
        else:
            self.close()

        chat = ChatPrivate.objects.filter(
            models.Q(user1=self.user) | models.Q(user2=self.user)
        )

        if chat.exists():
            self.chat = chat.first()
            self.user.is_online = True
            self.user.save()
            self.accept()
        else:
            self.close()

    def disconnect(self, close_code):
        if self.user:
            self.user.is_online = False
            self.user.save()
        async_to_sync(self.channel_layer.group_discard)(
            f"private_{self.room_name}", self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            f"private_{self.room_name}",
            {
                "type": "chat_message",
                "message": message,
            },
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event["message"]

        ChatPrivateMessage.objects.create(
            user=self.user, chat=self.chat, message=message
        )

        self.send(text_data=message)
