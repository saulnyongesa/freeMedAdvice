from django.urls import path

from backend import views

# User logic url
urlpatterns = [
    path('user/<int:pk>/', views.get_user, name="get_user-url"),
    path('user/create/', views.create_user, name="create_user-url"),
]

# Topic logic url
urlpatterns += [
    path('topics/', views.get_topics, name="get_topics-url"),
    path('topic/<int:pk>/', views.get_topic, name="get_topic-url"),
    path('topic/create/', views.create_topic, name="create_topic-url"),
]

# Post logic url
urlpatterns += [
    path('posts/', views.get_posts, name="get_posts-url"),
    path('post/<int:pk>/', views.get_post, name="get_post-url"),
    path('post/create/', views.create_post, name="create_post-url"),
]

# Room logic url
urlpatterns += [
    path('rooms/', views.get_rooms, name="get_rooms-url"),
    path('room/<int:pk>/', views.get_room, name="get_room-url"),
    path('room/create/', views.create_room, name="create_room-url"),
]

# Room Chat logic url
urlpatterns += [
    path('room/chat/<int:pk>/', views.room_chat, name="get_room_chat-url"),
]