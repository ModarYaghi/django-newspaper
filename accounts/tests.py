"""
This module contains tests for verifying the behavior of the
custom user model, ensuring that user creation and superuser
creation operate as expected.
"""

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

# Create your tests here.
#


class UsersManagersTests(TestCase):
    """
    A test suite for checking the custom user model's manager methods.
    Verifies both normal user creation and superuser creation.
    """

    def test_create_uer(self):
        """
        Ensure that a normal uer can be created with the required fields.
        """

        # Get the currently active user model (in case it's a custom one)
        User = get_user_model()

        # Create a standard user (non-superuser, non-staff)
        user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpass1234",
        )

        # Check that the user data matches what we expect.
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@example.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        """
        Ensure that a superuser can be created with the required fields.
        """

        # Get the currently active user model again.
        User = get_user_model()

        # Create a superuser (has all permissions, staff status).
        admin_user = User.objects.create_superuser(
            username="testsuperuser",
            email="testsuperuser@example.com",
            password="testpass1234",
        )

        # Check that the superuser data matches what we expect.
        self.assertEqual(admin_user.username, "testsuperuser")
        self.assertEqual(admin_user.email, "testsuperuser@example.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class SignUpPageTest(TestCase):

    def test_url_exists_at_correct_location_signupview(self):
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)  # type: ignore

    def test_signup_view_name(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)  # type: ignore
        self.assertTemplateUsed(response, "registration/signup.html")

    def test_signup_form(self):
        response = self.client.post(
            reverse("signup"),
            {
                "username": "testuser",
                "email": "testuser@email.com",
                "password1": "testpass123",
                "password2": "testpass123",
            },
        )
        self.assertEqual(response.status_code, 302)  # type: ignore
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, "testuser")
        self.assertEqual(get_user_model().objects.all()[0].email, "testuser@email.com")
