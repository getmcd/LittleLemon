from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers
from restaurant import views

urlpatterns = [
    # Remember to use the endpoint /api/ after http://127.0.0.1:8000
    path('', views.index, name='index'),      
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token),
    path("registration/", views.RegistrationView.as_view(), name="registration"),
]

