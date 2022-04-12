from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrAdmin(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user or request.user.is_staff)
