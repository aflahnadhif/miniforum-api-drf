from rest_framework import permissions

class UserManagementPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == 'create':
            return True
        
        if request.user.is_superuser:
            return True
        
        if view.action in ['retrieve', 'update', 'partial-update', 'destroy']:
            return request.user.is_authenticated
        
        return False
    
    def has_object_permission(self, request, view, obj):
        if view.action == 'create':
            return True
        
        if request.user.is_superuser:
            return True
        
        if view.action in ['retrieve', 'update', 'partial-update', 'destroy']:
            return request.user == obj
        
        return False