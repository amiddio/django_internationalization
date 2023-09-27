from django.urls import path

from article.views import *

app_name = 'article'

urlpatterns = [
    path('article/<slug:slug>/', ArticleDetailView.as_view(), name='detail'),
    path('articles/<slug:category_slug>/', ArticleListView.as_view(), name='list-filtered'),
    path('articles/', ArticleListView.as_view(), name='list'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
]
