from django.db import models
from django.utils import timezone
from datetime import datetime # Use standard Python datetime
from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime

# Allows developers to make logic to read and act on:
# - settings.TIME_ZONE
# - settings.USE_TZ
# - settings.DEBUG
# - settings.DATABASES
# - settings.REST_FRAMEWORK
# - settings.INSTALLED_APPS
from django.conf import settings

# Create your models here.
# class Menu(models.Model):
#     # id is automatically created by Django
#     title = models.CharField(max_length=255, db_index=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     inventory = models.IntegerField()
    
#     def __str__(self):
#         return self.title   # 👈 this controls how it appears in admin dropdowns & FK fields

class MenuItem(models.Model):
    title = models.CharField(max_length=255)   
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[
            MinValueValidator(Decimal("2.00")),
            MaxValueValidator(Decimal("50.00")),
        ],
    )
    inventory = models.IntegerField(
        validators=[
            MinValueValidator(1), 
            MaxValueValidator(200)],
    )
    
    # The f means this is an f-string (formatted string literal).
    # It allows you to embed Python expressions inside a string using {}.
    def get_item(self):
        # return f'{self.title : {{self.price:.2f})}}'
        return f"{self.title} : {self.price:.2f}"
    
    def __str__(self):
        # return f'{self.title : {{self.price:.2f}}}'
        return f"{self.title} : {self.price:.2f}"
        # return f"{self.title} (${self.price:.2f})"

# Previous record in Migration History file contains a 
# past update referencing function get_local_now().
# Update: booking_date = models.DateTimeField(default=datetime.now)
#   Caused makemigrations command to fail because of that 
#   previous function get_local_now().   Threw error.  
#     AttributeError: module 'restaurant.models' has no 
#     attribute 'get_local_now' 
#
# Here is why timezone.now is better than datetime.now.
# datetime.now() # is "naive," meaning it doesn't know about UTC or Daylight Savings.
# timezone.now() is "aware." It uses the TIME_ZONE setting in your settings.py (e.g.,
# 'UTC' or 'America/New_York').
#
# If you use naive times, your bookings might appear to be several 
# hours off once you deploy the app to a server.

# def get_local_now():
#     # return timezone.localtime(timezone.now())
#     return timezone.localtime(datetime.now())   

def get_local_now():
    if settings.USE_TZ:
        return timezone.localtime(timezone.now())  # aware
    return datetime.now()  # naive

class Booking(models.Model):
    # id is automatically created by Django
    name = models.CharField(max_length=255, db_index=True)
    number_of_guests = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(31)],
    )
    booking_date = models.DateTimeField(default=get_local_now)
    # datetime.now() grabs the system clock time without tSimezone info
    #booking_date = models.DateTimeField(default=datetime.now) 
    def __str__(self):
        return self.name   # 👈 this controls how it appears in admin dropdowns & FK fields    
    
