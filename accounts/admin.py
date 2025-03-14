"""
admin.py:
    Django admin configuraton for our CustomUser model.
    We customize the built-in UserAdmin to incorporate our CustomUser forms and fields.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser

# Register your models here.
#


# Extend UserAdmin to hook in our custom user forms and add an 'age' field.
class CustomUserAdmin(UserAdmin):
    """
    Custom admin class for managing CustomUser instances in the Django admin.
    Inherits from Django's built-in UserAdmin but uses our own forms and includes
    an 'age' field in both creation and update interfaces.
    """

    # The form used to create new CustomUser instances from the admin interface
    add_form = CustomUserCreationForm

    # The form used to change existing CustomUser instances from teh admin interface
    form = CustomUserChangeForm

    # Link this admin configuration to our CustomUser model
    model = CustomUser

    # The fields displayed in the list view of the admin
    list_display = [
        "email",
        "username",
        "age",
        "is_staff",
    ]

    # Extending the default fieldsets to include our 'age' field
    # when editing a user in the admin
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("age",)}),)

    # Extending the default fieldsets to include 'age' when creating a new user
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("age",)}),)


# Register our CustomUser model with the customized admin
admin.site.register(CustomUser, CustomUserAdmin)
