from django.shortcuts import render
from requests import Response
from rest_framework.response import *
from rest_framework.decorators import api_view
from rest_framework import status

from .models import *
from .serializer import *

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
