# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest, CustomerSubmission  # Import CustomerSubmission model
from .forms import ServiceRequestForm, CustomerSubmissionForm  # Import CustomerSubmissionForm
from django.core.mail import send_mail
from django.urls import reverse_lazy

def mech_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully logged in!')
            return redirect('mech:mech_home')  # Redirect to mech home page
        else:
            messages.error(request, 'Invalid username or password. If you do not have an account, please sign up.')
    return render(request, 'mech_login.html')

@login_required
def mech_home(request):
    service_requests = ServiceRequest.objects.all()
    return render(request, 'mech_home.html', {'service_requests': service_requests})

def send_login_email(username, email, password):
    subject = 'Your Job Application Login Credentials'
    message = f'Username: {username}\nPassword: {password}'
    sender_email = 'anantakumar0999@gmail.com'  # Update with your email
    send_mail(subject, message, sender_email, [email])

def submit_job_application(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            form.save()
            # Retrieve the submitted data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            # Generate a random password or handle password generation as per your requirement
            password = 'random_generated_password'
            # Send the login email with credentials
            send_login_email(name, email, password)
            # Redirect the user to the confirmation page
            return redirect('confirmation')
    else:
        form = ServiceRequestForm()
    return render(request, 'service_reg.html', {'form': form})

def service_reg(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect the user to the home page after submission
            return redirect('mech:mech_home')
    else:
        form = ServiceRequestForm()

    # Get the current service requests in the database
    service_requests = ServiceRequest.objects.all()
    return render(request, 'service_reg.html', {'form': form, 'service_requests': service_requests})

def mech_signup(request):
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
                return redirect('mech:mech_login')
        else:
            messages.error(request, 'Passwords do not match.')
    return render(request, 'signup.html')

def submit_information(request):
    if request.method == 'POST':
        form = CustomerSubmissionForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect the user to the confirmation page
            return redirect('confirmation')
    else:
        form = CustomerSubmissionForm()
    return render(request, 'submit_information.html', {'form': form})
