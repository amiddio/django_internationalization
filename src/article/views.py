from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView

from article.models import Article
from article.services.article_service import ArticleService


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = 'article'

    def get_object(self, queryset=None):
        slug = self.kwargs['slug']
        return get_object_or_404(ArticleService.get_objects(), translations__slug=slug)


class ArticleListView(ListView):
    model = Article
    template_name = 'articles.html'
    context_object_name = 'articles'
    paginate_by = ArticleService.PAGE_LIMIT

    def get_queryset(self):
        return ArticleService.get_objects()
