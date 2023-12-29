from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
import uuid

User = get_user_model()

class ChatThread(models.Model):
    thread_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Thread Name')
    user_one = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='user_one_threads', verbose_name='User One')
    user_two = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='user_two_threads', verbose_name='User Two')

    class Meta:
        unique_together = ['user_one', 'user_two']
        verbose_name = 'Chat Thread'
        verbose_name_plural = 'Chat Threads'

class ChatMessage(models.Model):
    thread = models.ForeignKey(ChatThread, null=True, blank=True, on_delete=models.CASCADE, related_name='messages', verbose_name='Thread')
    sender = models.ForeignKey(User, on_delete=models.CASCADE,null=True, verbose_name='Sender')
    message = models.TextField(verbose_name='Message',null=True, blank=True,)
    file = models.FileField(verbose_name='File',null=True,blank=True,default=None , max_length=1000)
    image = models.ImageField(verbose_name='Image',null=True,blank=True,default=None,max_length=1000)
    sent_time_12 = models.CharField(max_length=100,verbose_name='Time-12',null=True, blank=True)
    sent_time_24 = models.CharField(max_length=100,verbose_name='Time-24',null=True, blank=True)
    sent_date = models.CharField(max_length=100,verbose_name='Date',null=True, blank=True)
    class Meta:
        verbose_name = 'Chat Message'
        verbose_name_plural = 'Chat Messages'


class GroupChatThread(models.Model):
    group_owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='Group_owner_user', verbose_name='GroupOwner')
    thread_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Thread Name')
    Groupbio = models.CharField(max_length=255, null=True, blank=True, verbose_name='Group Bio')
    users = models.ManyToManyField(User, related_name='chat_threads', verbose_name='Users')
    thread_avatar = models.ImageField(upload_to='images/',verbose_name='Avatar Image',null=True,blank=True,default=None,max_length=1000)
    groupuniqueid = models.CharField(default=None,null=True,blank=True, editable=True, unique=True,max_length=500)
    class Meta:
        verbose_name = 'Group Chat Thread'
        verbose_name_plural = 'Group Chat Threads'


class GroupChatMessage(models.Model):
    thread = models.ForeignKey(GroupChatThread, null=True, blank=True, on_delete=models.CASCADE, related_name='messages', verbose_name='Group Thread')
    sender = models.ForeignKey(User, on_delete=models.CASCADE,null=True, verbose_name='Sender')
    message = models.TextField(verbose_name='Message',null=True, blank=True,)
    file = models.FileField(verbose_name='File',null=True,blank=True,default=None , max_length=1000)
    image = models.ImageField(verbose_name='Image',null=True,blank=True,default=None,max_length=1000)
    sent_time_12 = models.CharField(max_length=100,verbose_name='Time-12',null=True, blank=True)
    sent_time_24 = models.CharField(max_length=100,verbose_name='Time-24',null=True, blank=True)
    sent_date = models.CharField(max_length=100,verbose_name='Date',null=True, blank=True)
    class Meta:
        verbose_name = 'Group Chat Message'
        verbose_name_plural = 'Group Chat Messages'
