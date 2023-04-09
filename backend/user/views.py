from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserSerializer, UserUpdateSerializer, AdminUserSerializer
from .permissions import UserManagementPermission

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [UserManagementPermission]
    
    def get_serializer_class(self):
        if self.action == 'list':
            return AdminUserSerializer
        
        if self.action in ['update', 'partial-update']:
            return UserUpdateSerializer
        
        return UserSerializer
    
    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        user.is_active = False
        user.save()
        
        return Response(UserSerializer(user).data)