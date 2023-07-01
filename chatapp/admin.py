from django.contrib import admin
from .models import *

# Register your models here.
class UserDetailAdmin(admin.ModelAdmin):
    list_display =  ('user', 'status')

admin.site.register(UserDetail, UserDetailAdmin)

admin.site.register(ChatRoom)

class ChatMessageAdmin(admin.ModelAdmin):
    list_display =  ('room', 'message', 'sender')

admin.site.register(ChatMsg, ChatMessageAdmin)