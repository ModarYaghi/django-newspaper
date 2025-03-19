from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Article

# Create your views here.
#


class ArticleCreateView(LoginRequiredMixin, CreateView):
    """
    View to create a new Article.

    This view provides a form to create an article with the specified fields.
    The 'author' field is not included in the form, as it automatically set to
    the currently logged-in user in the form_valid method.
    """

    model = Article
    template_name = "article_new.html"
    fields = (
        "title",
        "body",
        # "author",
    )  # 'author' is set automatically is form_valid.

    def form_valid(self, form):
        """
        Called when a valid form submission is made.

        Automatically sets the 'author' of the Article instance to the logged-in user.
        After setting the author, the parent form_valid method is called to save the object
        and redirect the user.

        :param form: A valid ModelForm instance with cleaned data.
        :type form: django.forms.ModelForm
        :return: An HTTP redirect response after the article is successfully saved.
        :rtype: django.http.HttpResponse
        """

        # Set the article's author to the current user
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleListView(LoginRequiredMixin, ListView):
    """
    View to list all Articles.

    Only authenticated users can view the list of articles.
    The view renders the list using the "article_list.html" template.
    """

    model = Article
    template_name = "article_list.html"


class ArticleDetailView(LoginRequiredMixin, DetailView):
    """
    View to display the details of a single Article.

    Only authenticated user can view article details.
    The view renders the details using the "article-detail.html" template.
    """

    model = Article
    template_name = "article_detail.html"


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    View to update/edit an existign Article.

    Provides a form to update the 'title' and 'body' fields of an article.
    Access is restricted using the test_func method to ensure that only the article's
    author or a superuser can edit the article.
    """

    model = Article
    fields = (
        "title",
        "body",
    )
    template_name = "article_edit.html"

    def test_func(self):
        """
        Test whether the current user has permission to edit the article.

        The article can be edited if:
            - The user is a superuser (has all permissions), or
            - The user is the author of the article.

        :return: True if the user is allowed ot edit, False otherwise.
        :rtype: bool
        """
        obj = self.get_object()
        # To let superuser edit content from template directly.
        return self.request.user.is_superuser or obj.author == self.request.user
        #
        # or, the following will resrict every one on the template.
        # return obj.author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    View to delete an existing Article.

    After deletion, the user is redirected to the article list.
    Access is restricted so that only the article's author or
    a superuser can delete the article.
    """

    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list")

    def test_func(self):
        """
        Test whether the current user has permission to delete the article.

        The article can be deleted if:
            - The user is a superuser, OR
            - The user is the author of the article.

        :return: True if the user is allowed to delete, False otherwise.
        :rtype: bool
        """
        obj = self.get_object()
        # To let superuser edit content from template directly.
        return self.request.user.is_superuser or obj.author == self.request.user
        #
        # or, the following will resrict every one on the template.
        # return obj.author == self.request.user
