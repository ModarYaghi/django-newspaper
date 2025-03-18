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
        "author",
    )


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
