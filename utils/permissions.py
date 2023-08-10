from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """ Разрешения владельца
    """
    
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return bool(request.user == obj)
