from django.contrib import admin

from chat.models import UserAbr, ChatPrivateMessage, ChatPrivate
# Register your models here.


admin.site.register(UserAbr)
admin.site.register(ChatPrivate)
admin.site.register(ChatPrivateMessage)
