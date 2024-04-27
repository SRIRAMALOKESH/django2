from django.urls import path
from . import views

app_name = 'customer'

urlpatterns = [
    path('login/', views.customer_login, name='login'),
    path('logout/', views.customer_logout, name='logout'),
    path('signup/', views.customer_signup, name='signup'),
    path('services/', views.service, name='services'),
    path('service_reg/', views.service_reg, name='service_reg'),
    
    
]
