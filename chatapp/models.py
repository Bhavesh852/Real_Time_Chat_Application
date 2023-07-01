from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.BooleanField()


class ChatRoom(models.Model):
    room_code = models.CharField(max_length=10)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.room_code

class ChatMsg(models.Model):

    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    sender = models.CharField(max_length=20)
    message = models.CharField(max_length=100)

