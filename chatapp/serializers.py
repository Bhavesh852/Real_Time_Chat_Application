from rest_framework import serializers
from .models import *

class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserDetail
        fields = '__all__'
        depth = 1


class ChatRoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChatRoom
        fields = '__all__'
        depth = 1


class ChatMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChatMsg
        fields = '__all__'
        depth = 1