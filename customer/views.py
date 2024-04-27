from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.templatetags.static import static

def customer_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['user_id'] = user.id  # Store user ID in session
            messages.success(request, 'You have successfully logged in!')
            return redirect('services')  # Redirect to home page
        else:
            messages.error(request, 'Invalid username or password. If you do not have an account, please sign up.')
    return render(request, 'login.html')

def customer_logout(request):
    request.session.flush()  # Clear session data
    logout(request)
    return redirect('home')

def customer_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken.')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                messages.success(request, 'You have successfully signed up! Please login.')
                # Use reverse with the namespace to get the correct URL
                return redirect(reverse('customer:login'))
        else:
            messages.error(request, 'Passwords do not match.')
    return render(request, 'signup.html')

def mech_login(request):
    # Add any logic you need for the mechanic login page
    return render(request, 'mech_login.html')

def any_view(request):
    user_id = request.session.get('user_id')
    if user_id:
        # User is logged in, do something
        user = User.objects.get(id=user_id)
        # Example: Access user data or perform actions for logged-in users
        return render(request, 'logged_in_view.html', {'user': user})
    else:
        # User is not logged in
        return render(request, 'not_logged_in_view.html')

def service(request):
    services_list = [
        {'name': 'House Cleaning', 'category': 'House'},
        {'name': 'Plumbing Repair', 'category': 'Plumbing'},
        {'name': 'Car Repair', 'category': 'Vehicle'},
        # Add more services as needed
    ]
    
    # Mapping of category to image URL
    category_images = {
        'House': static('img/house.webp'),
        'Plumbing': static('img/plumbing.webp'),
        'Vehicle': static('img/vehicles.jpg'),
        # Add more mappings as needed
    }
    
    return render(request, 'core/service.html', {'services_list': services_list, 'category_images': category_images})

def service_reg(request):
    return render(request, 'service_reg.html')
