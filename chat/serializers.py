from rest_framework import serializers

from chat import models


class ChatPrivateMessageSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.ChatPrivateMessage
        fields = (
            'id',
            'user',
            'chat',
            'message',
            'is_read',
            'is_edited',
            'created_at',
        )


class ChatPrivateSerializer(serializers.ModelSerializer):
    # private_messages = ChatPrivateMessageSerializer(many=True)

    class Meta:
        models = models.ChatPrivate
        fields = (
            'id',
            'user1',
            'user2',
            # 'private_messages',
            'created_at',
            'updated_at',
        )
