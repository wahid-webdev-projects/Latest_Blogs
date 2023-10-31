# from django.contrib import admin
# from .models import Post
# # Register your models here.
# admin.site.register(Post)

from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'body')  # Add additional fields here

admin.site.register(Post, PostAdmin)
