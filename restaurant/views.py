from django.shortcuts import render

from django.contrib.auth.models import User

from rest_framework import viewsets, permissions, generics 
from rest_framework.decorators import api_view

from .models import Menu, Booking
from .serializers import UserSerializer, MenuSerializer, BookingSerializer

# Create your views here.
def index(request):
    return render( request, 'index.html', {})

# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    
    # Added permission class here
    # No access allowed to unathenticated users
    permission_classes = [permissions.IsAuthenticated]
    
# Create your views here. 
class MenuItemsView(generics.ListCreateAPIView): 
    queryset = Menu.objects.all() 
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):     
    queryset = Menu.objects.all() 
    serializer_class = MenuSerializer
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer