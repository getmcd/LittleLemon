from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework import generics


class IsAdminOrReadOnly(BasePermission):
    """
    Allow anyone authenticated to read (GET, HEAD, OPTIONS).
    Only admins can create/update/delete.
    How DRF Uses This

    When a request arrives:
    1.  DRF calls has_permission()
    2.  If it returns True, continue
    3.  If False, return 403 Forbidden
    
    DRF automatically calls this method before executing the view.
    """

    def has_permission(self, request, view):
        # SAFE_METHODS = ("GET", "HEAD", "OPTIONS")
        # If request.user exists and is logged in and authenticated,
        # then RETURN True. 
        if request.method in SAFE_METHODS:
            return request.user and request.user.is_authenticated

        # request.user exists, is staff, is logged in and authenticated,
        # then RETURN True.  
        # If non-staff or non-admin, RETURN False
        return request.user and request.user.is_staff

class IsOwnerOrAdmin(BasePermission):
    """
    IsOwnerOrAdmin will throw a 404 Not Found if non-admin user
    tries to change a booking that does not belong to them
    """
    # DRF automatically calls this method before executing the view.
    def has_object_permission(self, request, view, obj):
        # Admin/staff can do anything
        if request.user and request.user.is_staff:
            return True
        
        # Otherwise, only the owner can access/modify
        # True or False: Does this object belong to the currently authenticated user?
        # obj is the object being accessed
        # Example: a Booking instance
        # request.user.id is the ID of the logged-in user making the request.
        # If booking not owned by request.user, then RETURN False
        return getattr(obj, "user_id", None) == request.user.id