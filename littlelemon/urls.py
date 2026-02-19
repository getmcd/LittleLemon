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
from restaurant import views
from rest_framework.routers import DefaultRouter

# routers.DefaultRouter() is part of Django REST Framework’s automatic URL 
# routing system.  It creates an object that automatically generates RESTful 
# API URL patterns from registered ViewSets, eliminating the need to manually 
# define paths for standard CRUD operations.

# It builds URL patterns for your API for you, based on ViewSets, so you don’t have to
# manually write path() entries for each CRUD operation.
# users, booking and menu endpoints to support full CRUD

router = DefaultRouter()

# URL examples follow.

# http://127.0.0.1:8000/auth/users/
# http://127.0.0.1:8000/auth/users/3
router.register(r'users', views.UserViewSet)

# http://127.0.0.1:8000/api/booking/
# http://127.0.0.1:8000/api/booking/3

router.register(r"booking", views.BookingViewSet, basename="booking")

# http://127.0.0.1:8000/api/menu/
# http://127.0.0.1:8000/api/menu/13
router.register(r"menu", views.MenuViewSet, basename="menu")

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/', include('restaurant.urls')),
    path('api/', include(router.urls)), 
    
    # Browsable API only
    # The api-auth route is defined to let you use the browsable API feature of DRF.   
    #
    # After submitting on /qpi-auth/ , it will auto-redirect to /api-auth/login/

    #   /api-auth/login/ ,   Displays login screen to enter username and password
    #   /api-auth/logout/ ,  Is a browser-session logout endpoint; it logs you out, 
    #                           then redirects, so you won’t necessarily remain on that URL.
    #
    # Endpoint api-auth/ will render a web page welcome message.
    # Append menu to that endpoint and it will launch DRF Browsable API menu
    # After submitting on /qpi-auth/ , it will auto-redirect to /api-auth/login/
    # Submitting endpoint http://127.0.0.1:8000/api-auth/ will return a 404 Not Found.
    # To clear the 404, append login/ to the end of the URL
    #
    # Example of redirect after login:
    # http://127.0.0.1:8000/api-auth/login/?next=/api/menu/
    # After successful login, redirects to:
    # http://127.0.0.1:8000/api/menu/
    # To logout, append logout/ to URL.
    
    # http://127.0.0.1:8000/api-auth/logout/ sent back an error.
    # Error code: 405 Method Not Allowed
    #     Check to make sure you’ve typed the website address correctly.
    # Validated correct.  So, the logout endpoint is not allowed.
    # In DRF Browsable API, click on logout.  It does the same thing.
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')), 
    # path('api-auth/logout/', include('rest_framework.urls', namespace='rest_framework')),     
    #path('api/registration/', include('dj_rest_auth.registration.urls')),
    
    #path('api/', include('rest_framework.urls', namespace='rest_framework')),   
    # This endpoint displays Djoser's Extra Action button with a list of 9
    # actions you can do to a user account like change their password or activate them
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken'))
]


