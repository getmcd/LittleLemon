from django.contrib import admin
from .models import Menu, Booking

# 1. Define the Admin Class
class MenuAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "price", "inventory")
    list_filter = ['title']

class BookingAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "number_of_guests", "booking_date")
    list_filter = ['name']

# 2. Register them at the bottom
admin.site.register(Menu, MenuAdmin)
admin.site.register(Booking, BookingAdmin)

# Important
# For the HTML Form (Meta course assignment): If you are building 
# an HTML form manually, make sure your <input> tag is set to datetime-local:
# <input type="datetime-local" id="booking_date" name="booking_date">
    
    

    
        