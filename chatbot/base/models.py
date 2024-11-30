from django.db import models
from django.contrib.auth.models import User


class MessagesModel(models.Model):
    sender = models.ForeignKey(User,on_delete=models.CASCADE)
    msg = models.TextField('message')

class TabModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title = models.CharField('tab title',max_length=100,null=True)
    chats = models.ManyToManyField(MessagesModel)
    