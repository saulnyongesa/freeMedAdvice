<<<<<<< HEAD
=======
from django.shortcuts import render
>>>>>>> 1500c71627aee91dfad6bb07462a2105c050169d
from requests import Response
from rest_framework.response import *
from rest_framework.decorators import api_view
from rest_framework import status
<<<<<<< HEAD
=======

from .models import *
>>>>>>> 1500c71627aee91dfad6bb07462a2105c050169d
from .serializer import *

# User logic
@api_view(['GET', 'PUT', 'DELETE'])
def get_user(request, pk):
    try:
        user = User.objects.get(id=pk)  # Adjust the query as needed
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=404)

    if request.method=='GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Topic logics
@api_view(['GET'])
def get_topics(request):
    topics = Topic.objects.all()  # Adjust the query as needed
<<<<<<< HEAD
    serializer = TopicSerializer(topics, many=True)
=======
    serializer = TopicSerializer(topics)
>>>>>>> 1500c71627aee91dfad6bb07462a2105c050169d
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def get_topic(request, pk):
    try:
        topic = Topic.objects.get(id=pk)  # Adjust the query as needed
    except Topic.DoesNotExist:
        return Response({"error": "Topic not found"}, status=404)

    if request.method=='GET':
        serializer = TopicSerializer(topic)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TopicSerializer(topic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        topic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def create_topic(request):
<<<<<<< HEAD
    data = request.data
    serializer = TopicSerializer(data=data)
=======
    serializer = TopicSerializer(data=request.data)
>>>>>>> 1500c71627aee91dfad6bb07462a2105c050169d
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

<<<<<<< HEAD
# Post logics
@api_view(['GET'])
def get_posts(request):
    posts = Post.objects.all()  # Adjust the query as needed
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def get_post(request, pk):
    try:
        post = Post.objects.get(id=pk)  # Adjust the query as needed
    except Post.DoesNotExist:
        return Response({"error": "Post not found"}, status=404)

    if request.method=='GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def create_post(request):
    data = request.data
    serializer = PostSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Room logics
@api_view(['GET'])
def get_rooms(request):
    rooms = Room.objects.all()  # Adjust the query as needed
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def get_room(request, pk):
    try:
        room = Room.objects.get(id=pk)  # Adjust the query as needed
    except Room.DoesNotExist:
        return Response({"error": "Room not found"}, status=404)

    if request.method=='GET':
        serializer = RoomSerializer(room)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = RoomSerializer(room, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        room.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def create_room(request):
    data = request.data
    serializer = RoomSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Room Chat Logic
@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def room_chat(request, pk):
    try:
        room = Room.objects.get(id=pk)  # Adjust the query as needed
    except Room.DoesNotExist:
        return Response({"error": "Room not found"}, status=404)
    room_chats = RoomChat.objects.filter(room=room)
    if request.method=='GET':
        serializer = RoomChatSerializer(room_chats, many=True)
        return Response(serializer.data)


=======
>>>>>>> 1500c71627aee91dfad6bb07462a2105c050169d
