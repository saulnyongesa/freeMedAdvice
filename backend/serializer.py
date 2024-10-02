from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name', 'last_name', 'username', 'phone', 'email', 'is_active', 'is_authenticated']

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
<<<<<<< HEAD
        fields = ['id', 'user', 'topic']
=======
        fields = ['id','topic']
>>>>>>> 1500c71627aee91dfad6bb07462a2105c050169d


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
<<<<<<< HEAD
        fields = ['id', 'user', 'topic', 'text', 'video']

=======
        fields = ['id','topic']

class PostTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostText
        fields = ['id','text']
>>>>>>> 1500c71627aee91dfad6bb07462a2105c050169d

class PostPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostPhoto
<<<<<<< HEAD
        fields = ['id','post', 'photo']
=======
        fields = ['id','photo']

class PostVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostVideo
        fields = ['id','video']
>>>>>>> 1500c71627aee91dfad6bb07462a2105c050169d

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
<<<<<<< HEAD
        fields = ['id', 'moderator','topic']
=======
        fields = ['id','topic', 'moderator']
>>>>>>> 1500c71627aee91dfad6bb07462a2105c050169d

class RoomChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomChat
        fields = ['id','room', 'participant', 'chat']