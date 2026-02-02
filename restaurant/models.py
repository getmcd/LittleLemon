from django.db import models
from django.utils import timezone
from datetime import datetime # Use standard Python datetime

# Create your models here.
class Menu(models.Model):
    # id is automatically created by Django
    title = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
    
    def __str__(self):
        return self.title   # 👈 this controls how it appears in admin dropdowns & FK fields

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

def get_local_now():
    return timezone.localtime(timezone.now())
    
class Booking(models.Model):
    # id is automatically created by Django
    name = models.CharField(max_length=255, db_index=True)
    number_of_guests = models.IntegerField()
    booking_date = models.DateTimeField(default=get_local_now)
    # datetime.now() grabs the system clock time without tSimezone info
    #booking_date = models.DateTimeField(default=datetime.now) 
    def __str__(self):
        return self.name   # 👈 this controls how it appears in admin dropdowns & FK fields    
    
