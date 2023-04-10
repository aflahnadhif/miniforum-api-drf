from rest_framework import generics
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserSerializer, UserUpdateSerializer, AdminUserSerializer, UserRoleUpdateSerializer
from .permissions import UserManagementPermission
from .paginations import UserPagination

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    # TODO: Try Session Auth
    # To enable trying requests in Swagger API Doc
    permission_classes = [UserManagementPermission]
    pagination_class = UserPagination
    
    def get_serializer_class(self):
        if self.action == 'list':
            return AdminUserSerializer
        
        if self.action in ['update', 'partial-update']:
            return UserUpdateSerializer
        
        return UserSerializer
    
    # TODO: Soft Delete
    # Should be implemented in model
    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        user.is_active = False
        user.save()
        
        return Response(UserSerializer(user).data)
    
class UserRoleUpdate(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRoleUpdateSerializer
    permission_classes = [permissions.IsAdminUser]