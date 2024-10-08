from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    phone = models.CharField(max_length=15, null=True, blank=True)  # Use CharField for phone numbers

class Topic(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    topic = models.CharField(max_length=100, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.topic

class Post(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, null=True, on_delete=models.CASCADE)
    text = models.TextField(max_length=1500, null=True, blank=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}'s Post"


class PostPhoto(models.Model):
    post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='images/')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Photo for {self.post.user.username}"

# ROOMS
class Room(models.Model):
    topic = models.ForeignKey(Topic, null=True, on_delete=models.CASCADE)
    moderator = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.moderator.username}'s Room, Topic: {self.topic.topic}"

class RoomChat(models.Model):
    room = models.ForeignKey(Room, null=True, on_delete=models.CASCADE)
    participant = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    chat = models.CharField(max_length=500, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"'{self.chat[:30]}'--{self.room.moderator.username}'s Room, Topic: {self.room.topic.topic}"

