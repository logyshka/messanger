from rest_framework import serializers

from .models import Chat, Message


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['id', 'name']


class MessageSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Message
        fields = ['id', 'chat', 'user', 'text', 'sent_at', 'edited_at']
        read_only_fields = ['user', 'sent_at', 'edited_at']
