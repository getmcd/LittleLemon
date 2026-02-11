"""
URL configuration for littlelemon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from restaurant import views

# routers.DefaultRouter() is part of Django REST Framework’s automatic URL 
# routing system.  It creates an object that automatically generates RESTful 
# API URL patterns from registered ViewSets, eliminating the need to manually 
# define paths for standard CRUD operations.
router = routers.DefaultRouter()

# It builds URL patterns for your API for you, based on ViewSets, so you don’t have to
# manually write path() entries for each CRUD operation.
# users endpoint to support full CRUD
# http://127.0.0.1:8000/auth/users/
# http://127.0.0.1:8000/auth/users/3
router.register(r'users', views.UserViewSet)

# http://127.0.0.1:8000/api/booking/
# http://127.0.0.1:8000/api/booking/3
router.register(r'booking', views.BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/', include('restaurant.urls')),
    path('api/', include(router.urls)), 
    
    # The api-auth route is defined to let you use the browsable API feature of DRF.   
    # This path statement only adds the Browsable API login/logout views; don't use
    # it for any other purpose:
    #   /api-auth/login/
    #   /api-auth/logout/
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    #path('api/', include('rest_framework.urls', namespace='rest_framework')),   
    # path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.authtoken'))
    # This endpoint displays Djoser's Extra Action button with a list of 9
    # actions you can do to a user account like change their password or activate them
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken'))
]

# Test URLs for Insomnia and DRF.
# Never use endpoing # http://127.0.0.1:8000/api/users/3/ because you will not be able
# to use the extra actions button found in djoser urls, 
# Auth endpoint puts email first.  Api puts username first.
# Important: using the api instead of auth will prevent you from using djoser
# auto-created urls.
# 0.  Register a new user:
#       POST http://127.0.0.1:8000/auth/users/
# 1.  Add or display users: 
#       GET, POST http://127.0.0.1:8000/auth/users/
# 2.  Get single user id=3
#       GET, PUT, PATCH, DELETE, http://127.0.0.1:8000/auth/users/3/
# 3.  For Insomnia, get an access token by POST, plus username and password.                                 
#       POST http://127.0.0.1:8000/api/api-token-auth/
# 4.  Add, display or update Menu Items:
#       GET, POST  http://127.0.0.1:8000/api/menu-items/
#       GET, PUT, PATCH, DELETE, http://127.0.0.1:8000/api/menu-items/3
# 5.  Render to client an HTML 5 Template to display Welcome to Little 
#     Lemon Restaurant.
#       http://127.0.0.1:8000/api/
# 6.  Add, display or update bookings:
#       GET POST http://127.0.0.1:8000/api/booking/
#       GET, PUT, PATCH, DELETE  http://127.0.0.1:8000/api/booking/16/
