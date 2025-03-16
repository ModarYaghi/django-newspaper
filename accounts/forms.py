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
        # Take built-in fields and adding "age" to them.
        # fields = UserCreationForm.Meta.fields + ("age",)

        # Explicitly define fields as a new tuple, replacing any defaults
        # that might have been set in the parent form. This method gives
        # full control over the order and content of the fields.
        fields = (
            "username",
            "email",
            "age",
        )


class CustomUserChangeForm(UserChangeForm):
    """
    A form that updates an existing user, extending Django's default
    UserChangeForm without additional fields.
    """

    class Meta:  # type: ignore
        model = CustomUser
        # fields = UserChangeForm.Meta.fields
        #
        fields = (
            "username",
            "email",
            "age",
        )
