from rest_framework.viewsets import ModelViewSet

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer, UpdateCommentSerializer
from .permissions import ForumUserPermission

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [ForumUserPermission]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
            
class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes = [ForumUserPermission]
    
    def get_serializer_class(self):
        if self.action in ['update', 'partial-update']:
            return UpdateCommentSerializer
        
        return CommentSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
    def perform_update(self, serializer):
        instance = self.get_object()
        serializer.save(user=self.request.user, post=instance.post)
    
