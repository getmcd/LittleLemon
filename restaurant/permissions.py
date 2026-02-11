from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework import generics

class IsAdminOrReadOnly(BasePermission):
    """
    Allow anyone authenticated to read (GET, HEAD, OPTIONS).
    Only admins can create/update/delete.
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user and request.user.is_authenticated

        return request.user and request.user.is_staff