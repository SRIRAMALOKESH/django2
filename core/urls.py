from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('location/', views.location, name='location'),
    path('feedback/', views.feedback, name='feedback'),

]
