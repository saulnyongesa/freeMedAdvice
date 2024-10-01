from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name', 'last_name', 'username', 'phone', 'email', 'is_active', 'is_authenticated']

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id','topic']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','topic']

class PostTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostText
        fields = ['id','text']

class PostPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostPhoto
        fields = ['id','photo']

class PostVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostVideo
        fields = ['id','video']

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id','topic', 'moderator']

class RoomChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomChat
        fields = ['id','room', 'participant', 'chat']