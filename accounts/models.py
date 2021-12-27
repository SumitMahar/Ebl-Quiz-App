from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # The first element in each tuple is the actual value to be stored, 
    # and the second element is the human-readable name.
    CHOICES = [
        ('1', 'Yes'),
        ('0', 'No'),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    