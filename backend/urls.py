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