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
    
    
        