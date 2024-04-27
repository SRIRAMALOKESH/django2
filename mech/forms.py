# mech/forms.py
from django import forms
from .models import ServiceRequest, CustomerSubmission

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['name', 'address', 'description']  # Remove 'pincode' from fields if not in model

class CustomerSubmissionForm(forms.ModelForm):
    class Meta:
        model = CustomerSubmission
        fields = ['name', 'email']  # Add more fields as needed
