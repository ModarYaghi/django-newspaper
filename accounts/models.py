from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
#


class CustomUser(AbstractUser):
    """
    A custom user model that extends Django's AbstractUser
    by adding an optional 'age' field.
    """

    # The user's age in years (optional).
    age = models.PositiveIntegerField(null=True, blank=True)
