from django.contrib import admin
from webapp.models import User, Post, Comment, Rating


# Register your models here.
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Rating)