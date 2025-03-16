from django.shortcuts import render
from django.urls import (
    reverse_lazy,
)  # Used for lazily resolving URL names; ideal for class-based views
from django.views.generic import (
    CreateView,
)  # Import the generic CreateView for handling object creation.

from .forms import CustomUserCreationForm  # Import our custom user cration form

# Create your views here.
#


class SignUpView(CreateView):
    """
    Handles user registration by displaying and procesing
    the custom sign-up form.

    This view uses CustomUserCreationFrom to validate
    and create a new user. Upon successful
    registration, it redirects to the login page.
    """

    # Spcify the form to use for user registration.
    form_class = CustomUserCreationForm

    # Define URL to redirect to once the form is successfully
    # submitted. 'reverse_lazy' is used because URL configuration
    # isn't loaded until all modules are ready.
    success_url = reverse_lazy("login")

    # Set the template used to render the sign-up page.
    template_name = "registration/signup.html"
