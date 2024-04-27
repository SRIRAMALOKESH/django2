# models.py
from django.db import models

class ServiceRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    description = models.TextField()
    pincode = models.CharField(max_length=20)  # Add pincode field


    def __str__(self):
        return self.name  # Or any other representation you prefer

class CustomerSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    # Add more fields as needed

    def __str__(self):
        return self.name  # Or any other representation you prefer