import uuid

from django.db import models


class Chat(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255)


class Message(models.Model):
    id = models.BigAutoField(primary_key=True)
    chat = models.ForeignKey(
        to='chats.Chat',
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        to='users.User',
        on_delete=models.CASCADE
    )
    text = models.CharField(max_length=2048)
    sent_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(null=True)
