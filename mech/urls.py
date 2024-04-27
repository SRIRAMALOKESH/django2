from django.urls import path
from . import views

app_name = 'mech'

urlpatterns = [
    path('login/', views.mech_login, name='mech_login'),  # Define the URL pattern with the correct name
    path('home/', views.mech_home, name='mech_home'),
    path('signup/', views.mech_signup, name='mech_signup'),
]
