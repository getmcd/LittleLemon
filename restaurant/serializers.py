from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Menu, Booking

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        # The 'id' is included because it's the primary key created by Django
        fields = ['id', 'title', 'price', 'inventory']
        
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        # The 'id' is included because it's the primary key created by Django
        fields = '__all__'
        

# class BookingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Booking
#         fields = '__all__'
#         extra_kwargs = {
#             'booking_date': {'format': '%Y-%m-%dT%H:%M:%S'} # ISO format with time
#         }