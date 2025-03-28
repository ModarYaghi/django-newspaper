"""
URL configuration for news_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path

# from django.views.generic.base import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path(
        "accounts/", include("django.contrib.auth.urls")
    ),  # include the built-in authentication URLs under the `accounts/` namespace.
    #
    # the following TemplateView url replaced with pages.urls, since I created a dedicted pages app, for better organization, maintainability and scalability.
    # path(
    # "", TemplateView.as_view(template_name="home.html"), name="home"
    # ),  # define root URL of the site, using the TemplateView since it's a static hompepage.
    #
    path("articles/", include("articles.urls")),
    path("", include("pages.urls")),
]
