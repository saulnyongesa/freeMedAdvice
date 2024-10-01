from django.urls import path

from backend import views

urlpatterns = [
    path('user/<int:pk>', views.get_user, name="get_user-url"),
    path('create-user/', views.create_user, name="create_user-url"),
]