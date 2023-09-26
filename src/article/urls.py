from django.urls import path, include

from article.views import ArticleDetailView, ArticleListView

app_name = 'article'

urlpatterns = [
    path('article/<slug:slug>/', ArticleDetailView.as_view(), name='detail'),
    path('articles/', ArticleListView.as_view(), name='list'),
]
