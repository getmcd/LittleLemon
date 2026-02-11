from django.contrib import admin
from django.db import models
from django.contrib.admin.widgets import AdminSplitDateTime
from .models import MenuItem, Booking

from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Unregister the default admin
admin.site.unregister(User)

# Re-register with ordering
@admin.register(User)
class CustomUserAdmin(UserAdmin):
        # List page columns
    list_display = ("id", "username", "email", "password",)

    # Right-side filters (DateTime gets a nice drill-down)
    list_filter = ("username", )

    # Search box (top)
    search_fields = ("username",)

    # Default ordering
    ordering = ("-booking_date",)

    # Optional: pagination size
    list_per_page = 5
    
    ordering = ("username",)  # force ordering in admin list view

# MenuItem Admin
@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "price", "inventory")
    list_filter = ("title",)
    search_fields = ("title",)
    ordering = ("title",)

# Booking Admin
# Django Admin widgets do not affect the DRF Browsable API.
#
# The DRF “viewer” (Browsable API) renders HTML inputs based on your 
# serializer fields, and it mostly relies on HTML5 input types. If the 
# browser doesn’t provide a picker UI for that input type, you’ll still 
# see a plain textbox.
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    # List page columns
    list_display = ("id", "name", "number_of_guests", "booking_date")

    # Right-side filters (DateTime gets a nice drill-down)
    list_filter = ("booking_date", "name")

    # Search box (top)
    search_fields = ("name",)

    # Default ordering
    ordering = ("-booking_date",)

    # Optional: pagination size
    list_per_page = 5

    # Optional: quickly edit fields from list view
    # (comment out if you don’t like inline editing)
    list_editable = ("number_of_guests", "booking_date")

    # Adds a date hierarchy navigation at the top (Year / Month / Day)
    date_hierarchy = "booking_date"

    # Use the split date/time widget (calendar + time)
    formfield_overrides = {
        models.DateTimeField: {"widget": AdminSplitDateTime()},
    }



# from django.contrib import admin
# from django.db import models

# from .models import MenuItem, Booking

# # import ability to select both date and time in DRF API Viewer
# from django.contrib.admin.widgets import AdminSplitDateTime

# # 1. Define the Admin Class
# class MenuItemAdmin(admin.ModelAdmin):
#     list_display = ("id", "title", "price", "inventory")
#     list_filter = ['title']

# # class BookingAdmin(admin.ModelAdmin):
# #     list_display = ("id", "name", "number_of_guests", "booking_date")
# #     list_filter = ['name']


# @admin.register(Booking)
# class BookingAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         models.DateTimeField: {"widget": AdminSplitDateTime()},
#     }

# # Register them at the bottom
# admin.site.register(MenuItem, MenuItemAdmin)
# # admin.site.register(Booking, BookingAdmin)

# # Important
# # For the HTML Form (Meta course assignment): If you are building 
# # an HTML form manually, make sure your <input> tag is set to datetime-local:
# # <input type="datetime-local" id="booking_date" name="booking_date">
    
    

    
        