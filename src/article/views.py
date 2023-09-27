from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView

from article.models import Article, Category
from article.services.article_service import ArticleService
from article.services.category_service import CategoryService


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
        category_slug = self.kwargs.get('category_slug', None)
        return ArticleService.get_objects(category_slug=category_slug)


class CategoryListView(ListView):
    model = Category
    template_name = 'categories.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return CategoryService.get_objects()
