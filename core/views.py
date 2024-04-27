from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def services(request):
    return render(request, 'service.html')

def about(request):
    return render(request, 'about.html')


def feedback(request):
    return render(request, 'feedback.html')


def location(request):
    # Fetch user's location using Geolocation API
    # For demonstration purposes, you can pass sample latitude and longitude values
    latitude = 40.7128
    longitude = -74.0060
    return render(request, 'location.html', {'latitude': latitude, 'longitude': longitude})