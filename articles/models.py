from django.conf import settings
from django.db import models
from django.urls import reverse

# Create your models here.
#


class Article(models.Model):
    """
    Model representing an article or post in the application.
    """

    title = models.CharField(
        max_length=255,
        help_text="The title of the article (up to 255 characters).",
    )
    body = models.TextField(
        help_text="The main content of the article",
    )
    date = models.DateTimeField(
        auto_now_add=True,
        help_text="The date and time when the article was created. This field is set automatically.",
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Use the AUTH_USER_MODEL defined in settings.py.
        on_delete=models.CASCADE,
        help_text="The user who authored the article. Deleting the user will also delete their articles.",
    )

    def __str__(self):  # type: ignore
        """
        Returns a human-readable representation of the model.
        Here we use the title of the article.
        """
        return self.title

    def get_absolute_url(self):
        """
        Returns the URL to access a detailed view of the article.
        This is useful for redirecting after creating or editing an article.
        """
        return reverse("article_detail", kwargs={"pk": self.pk})
