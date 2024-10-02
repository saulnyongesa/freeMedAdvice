from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name', 'last_name', 'username', 'phone', 'email', 'is_active', 'is_authenticated']

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'user', 'topic']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'user', 'topic', 'text', 'video']


class PostPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostPhoto
        fields = ['id','post', 'photo']

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'moderator','topic']

class RoomChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomChat
        fields = ['id','room', 'participant', 'chat']