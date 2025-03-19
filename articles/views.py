from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Article

# Create your views here.
#


class ArticleCreateView(CreateView):
    """
    Create a new article
    """

    model = Article
    template_name = "article_new.html"
    fields = (
        "title",
        "body",
        # "author",  # this commented out to make author is the logged in user.
    )

    def form_valid(self, form):
        """
        Assign the logged -in user as the author and save the article.

        This method is invoked when the submitted form is valid. It automatically
        sets the 'author' field of the Article instance (available as form.instance)
        to the current user (self.request.user). This ensures that the article is
        properly associated with the user who created it without requiring manual
        input for the author field.
        Finally, it delegates the rest of the form processing (saving the instance and redirecting)
        to the parent class's form_valid method.

        :param form: A valid form instance containing the data for the new article.
        :type form: django.forms.ModelForm
        :return: An HTTP redirect response after the article is successfully saved.
        :rtype: django.http.HttpResponse
        """

        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleListView(ListView):
    """
    List all articles created
    """

    model = Article
    template_name = "article_list.html"


class ArticleDetailView(DetailView):
    """
    Present an article
    """

    model = Article
    template_name = "article_detail.html"


class ArticleUpdateView(UpdateView):
    """
    Update/edit an article
    """

    model = Article
    fields = (
        "title",
        "body",
    )
    template_name = "article_edit.html"


class ArticleDeleteView(DeleteView):
    """
    Delete an article
    """

    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list")
