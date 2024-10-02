from django.contrib import admin

from backend.models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Topic)
admin.site.register(Post)
admin.site.register(PostPhoto)
admin.site.register(Room)
admin.site.register(RoomChat)