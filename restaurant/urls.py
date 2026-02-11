from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # Remember to use the endpoint /api/ after http://127.0.0.1:8000
    path('', views.index, name='index'),
    # path('welcome/', views.index, name='welcome'),   
    
     # http://127.0.0.1:8000/api/menu-items/
    path('menu-items/', views.MenuItemsView.as_view()),   
 
    # http://127.0.0.1:8000/api/menu-items/2 or
    # http://127.0.0.1:8000/api/menu-items/2/ will both work
    path('menu-items/<int:pk>/', views.SingleMenuItemView.as_view()),
    
    path('message/', views.msg),
    
    path('api-token-auth/', obtain_auth_token),
]

