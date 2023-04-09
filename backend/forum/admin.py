from django.contrib import admin
from .models import Post, Comment

@admin.register(Comment)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'post', 'text']

@admin.register(Post)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'text']