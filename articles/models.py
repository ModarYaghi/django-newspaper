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


class Comment(models.Model):
    """
    Represents a user comment on an article.

    Each Comment is linked to an Article and an Author.
    The comment text is limited ot 140 characters.
    """

    # Forign key to the Article model.
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        help_text="Select the article this comment is related to.",
    )

    # A short text comment with a maximum of 140 characters.
    comment = models.CharField(
        max_length=140,
        help_text="Enter your comment (max 140 characters).",
    )

    # Foreign key to the user who authored the comment.
    # Uses the custom user model defined in settings.AUTH_USER_MODEL.
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        help_text="User who authored this comment",
    )

    def __str__(self):  # type: ignore
        """
        Return a string representation of the Comment instance.

        This is typically used in the Django admin or shell for a quick overview.
        Here, it returns the comment text.
        """

        return self.comment

    def get_absolute_url(self):
        """
        Return teh URL to access the article list.

        This method is used to determine the redirection target after a Comment is created or updated.
        """

        return reverse("article_list")
