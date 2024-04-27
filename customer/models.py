from django.contrib.auth import get_user_model
from django.contrib.auth.signals import user_logged_in
from django.db import models

class UserAccount(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='account'
    )
    # Add other fields as needed for the user account

    def __str__(self):
        return str(self.user)

from django.dispatch import receiver

@receiver(user_logged_in)
def user_logged_in_handler(sender, request, user, **kwargs):
    # Check if UserAccount exists for the logged-in user
    if not hasattr(user, 'account'):
        # Create UserAccount if it doesn't exist
        UserAccount.objects.create(user=user)


class CustomerSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    # Add more fields as needed

    def __str__(self):
        return self.name  # Or any other representation you prefer