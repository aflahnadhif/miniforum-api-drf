from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.models import (
    TimeStampedModel,
    ActivatorModel
)

class Post(
    TimeStampedModel,
    ActivatorModel
    ):
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['pk']
        
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    text = models.TextField(null=False, blank=False)

class Comment(
    TimeStampedModel,
    ActivatorModel,
    ):
    
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['pk']
        
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False, blank=False)
    text = models.TextField(null=False, blank=False)