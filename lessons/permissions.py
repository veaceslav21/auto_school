from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrAdminOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS and request.auth:
            return True
        return bool(obj.student == request.user or request.user.is_staff is True)
