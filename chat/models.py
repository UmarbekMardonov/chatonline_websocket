from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class ChatType(models.TextChoices):
    PRIVATE = "private"
    GROUP = "group"


class Chat(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    chat_type = models.CharField(
        max_length=10,
        choices=ChatType.choices,
        default=ChatType.PRIVATE,
    )

    owner = models.ForeignKey(
        'UserAbr', on_delete=models.CASCADE, related_name="chat_owner")

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class UserAbr(AbstractUser):
    is_online = models.BooleanField(default=False)
    user_permissions = None
    groups = None
    # chat = models.ForeignKey(
    #     Chat, on_delete=models.CASCADE, related_name='chats', blank=True, null=True
    # )


class ChatPrivate(models.Model):
    user1 = models.OneToOneField(
        UserAbr, on_delete=models.CASCADE, related_name="user1")
    user2 = models.ForeignKey(
        UserAbr, on_delete=models.CASCADE, related_name="user2")
    # description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     if self.chat_type == ChatType.PRIVATE:
    #         return f"{self.id} (private)"
    #     return self.title


class ChatPrivateMessage(models.Model):
    user = models.ForeignKey(UserAbr, on_delete=models.CASCADE)
    chat = models.ForeignKey(
        ChatPrivate, on_delete=models.CASCADE, related_name='private_messages')

    message = models.TextField()

    is_read = models.BooleanField(default=False)
    is_edited = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)


# class CharGroup(models.Model):
#     owner = models.ForeignKey(User, on_delete=models.CASCADE)
