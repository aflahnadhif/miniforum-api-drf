from rest_framework import permissions

class ForumUserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ['list', 'retrieve']:
            return True
        
        if view.action in ['create', 'update', 'partial-update', 'destroy']:
            return request.user.is_authenticated
        
        return False
    
    def has_object_permission(self, request, view, obj):
        if view.action in ['list', 'retrieve']:
            return True
        
        if view.action == 'create':
            return request.user.is_authenticated
        
        if request.user.is_superuser:
            return True
        
        if view.action in ['update', 'partial-update', 'destroy']:
            return request.user == obj.user
        
        return False
