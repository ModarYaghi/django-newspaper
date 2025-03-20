from django.contrib import admin

from .models import Article, Comment

# Register your models here.
#

# Inline admin configuration for Comment.
# # This will allow comment to be edited directly on the Article admin page.

# class CommentInline(admin.StackedInline):
#     model = Comment
#     extra = 0
#


class CommentInline(admin.TabularInline):
    """
    Display comments in a tabular (compact) format within the Article admin.

    Attributes:
        - model (Comment): Specifies the Comment model for this inline.
        - extra (int): The number of extra empty forms to display. Set to 0 to not show any extra forms.
    """

    model = Comment
    extra = 0


# Admin configuration for the Article model.
class ArticleAdmin(admin.ModelAdmin):
    """
    Customize the admin interface for the Article model.

    Attributes:
        - inlines (list): A list of linline admin configurations; here, it includes comments.
        - list_display (list): Fields to display in the list view of Articles.
    """

    inlines = [
        CommentInline,  # Inline display of associated Comment instances.
    ]

    list_display = [
        "title",  # Display the title of the article.
        "body",  # Display the article body.
        "author",  # Display the author of the article.
    ]


# Register the models with their custom admin configurations.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
