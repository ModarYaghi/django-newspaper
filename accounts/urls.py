from django.urls import path

from .views import SignUpView

urlpatterns = [
    # This URL pattern maps the URL 'singup/' to the SignUpView.
    # When a user visits '/signup/', Django calls SignUpView.as_view() to handle the request.
    # The name "signup" allows to refer to this URL pattern in templates and other parts
    path("signup/", SignUpView.as_view(), name="signup"),
]
