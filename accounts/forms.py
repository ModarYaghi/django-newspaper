"""
Forms used for creating and updating CustomUser instances.
"""

from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """
    A form that creates a new user, extending Django's default
    UserCreationForm by adding an 'aga' field.
    """

    class Meta:  # type: ignore
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("age",)


class CustomUserChangeForm(UserChangeForm):
    """
    A form that updates an existing user, extending Django's default
    UserChangeForm without additional fields.
    """

    class Meta:  # type: ignore
        model = CustomUser
        fields = UserChangeForm.Meta.fields
