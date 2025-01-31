from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission: Only admins can create, update, or delete.
    Other users can only read (GET).
    """
    def has_permission(self, request, view):
        # Allow read-only (GET, HEAD, OPTIONS) for all authenticated users
        if request.method in permissions.SAFE_METHODS:
            return True

        # Allow create, update, delete only for admins
        return request.user and request.user.is_staff
