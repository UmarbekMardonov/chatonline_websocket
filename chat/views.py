from django.shortcuts import render
from rest_framework import generics

from chat import models
from chat import serializers


class ChatPrivateMessagesListView(generics.ListAPIView):
    queryset = models.ChatPrivateMessage.objects.all()
    serializer_class = serializers.ChatPrivateMessageSerializer

    # def filter_queryset(self, queryset):
    #     queryset = super(ChatPrivateMessagesListView,
    #                      self).filter_queryset(queryset)
    #     print(self.kwargs['chat_pk'])
    #     return queryset.filter(chat=self.kwargs['chat_pk'])

class ChatPrivateRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.ChatPrivate.objects.all()
    serializer_class = serializers.ChatPrivateSerializer
