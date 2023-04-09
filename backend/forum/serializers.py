from rest_framework import serializers
from .models import Post, Comment
from user.serializers import UserViewSerializer
        
class CommentSerializer(serializers.ModelSerializer):
    owner = UserViewSerializer(source='user', read_only=True)
    
    class Meta:
        model = Comment
        fields = [
            'id',
            'text',
            'post',
            'owner', # read_only
        ]
        read_only_fields = ['id']
        
class UpdateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'text'        
        ]
        
class PostCommentsSerializer(serializers.ModelSerializer):
    owner = UserViewSerializer(source='user', read_only=True)
    
    class Meta:
        model = Comment
        fields = [
            'id',
            'text',
            'owner', # read_only
        ]
        read_only_fields = ['id']
        
class PostSerializer(serializers.ModelSerializer):
    owner = UserViewSerializer(source='user', read_only=True)
    comment_set = PostCommentsSerializer(many=True, read_only=True)
      
    class Meta:
        model = Post
        fields = [
            'id',
            'text',
            'owner', # read_only
            'comment_set', # read_only
        ]
        read_only_fields = ['id']
        