from django.contrib.auth.models import User
from django.shortcuts import render

from rest_framework import viewsets, permissions, generics 
from rest_framework.decorators import api_view, permission_classes, authentication_classes, action

# Was not able to login to DRF Browsable API without using SessionAuthentication
# http://127.0.0.1:8000/api-auth/login/
# Fix:  That login sets a session cookie (sessionid) for SessionAuthentication.
# That forces the the view to allow SessionAuthentication
# Insomnia end point testing requires TokenAuthenication

from .permissions import IsOwnerOrAdmin

from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import (
    BasePermission, 
    SAFE_METHODS, 
    IsAuthenticated, 
    IsAdminUser, 
    AllowAny 
    )
from rest_framework.response import Response

from .models import Booking, MenuItem
from .serializers import UserSerializer, BookingSerializer, MenuItemSerializer
from .permissions import IsAdminOrReadOnly, IsOwnerOrAdmin
from .models import MenuItem

# {} means render page with no dynamic data, meaning: empty dictionary.
def index(request):
    return render( request, 'index.html', {})
  
class UserViewSet(viewsets.ModelViewSet):
    # No access allowed to unathenticated users
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = User.objects.all().order_by("username")
    serializer_class = UserSerializer
    
    # Function renders in DRF Browsable API under a button called Extra Actions
    # located between the Filters and Options buttons.    
    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated])
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

class RegistrationView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrReadOnly]
    queryset = MenuItem.objects.all().order_by("title")
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):    
    permission_classes = [IsAdminOrReadOnly] 
    queryset = MenuItem.objects.all().order_by("title") 
    serializer_class = MenuItemSerializer

# This enforces:
# GET list: user sees only their bookings
# GET detail: user can only retrieve their own booking
# PATCH/PUT/DELETE: user can only modify/delete their own booking
# Admin: full access
class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
    serializer_class = BookingSerializer

    def get_queryset(self):
        qs = Booking.objects.all().order_by("-booking_date", "-id")
        # Admin sees all; users see only theirs
        if self.request.user.is_staff:
            return qs
        return qs.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Force the booking owner to be the logged-in user
        serializer.save(user=self.request.user)

    
# This is a Django REST Framework function-based DRF API view that:
# - Only allows authenticated users
# - Accepts only GET requests
# - Returns a JSON response
#
# @authentication_classes tells DRF how to identify the user.
# Two authentication mechanisms are allowed:
# - SessionAuthentication
# Uses Django login sessions (browser cookies)
# Works with DRF Browsable API login
# - TokenAuthentication
# Uses header:
# Authorization: Token <token>
@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def msg(request):
    return Response({"message": "View Function msg called successfully. This msg view is protected by IsAthenticated"})