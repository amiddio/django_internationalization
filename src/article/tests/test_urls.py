from django.test import TestCase
from django.urls import resolve
from django.utils.translation import activate

from article.views import ArticleDetailView, ArticleListView, CategoryListView


class UrlsTest(TestCase):

    def test_en_article_detail_url_resolves(self):
        activate('en')
        resolver = resolve('/en/article/some-article-slug/')
        self.assertEqual('article:detail', resolver.view_name)
        self.assertEqual(ArticleDetailView, resolver.func.view_class)

    def test_ru_article_detail_url_resolves(self):
        activate('ru')
        resolver = resolve('/ru/article/some-article-slug/')
        self.assertEqual('article:detail', resolver.view_name)
        self.assertEqual(ArticleDetailView, resolver.func.view_class)

    def test_es_article_detail_url_resolves(self):
        activate('es')
        resolver = resolve('/es/article/some-article-slug/')
        self.assertEqual('article:detail', resolver.view_name)
        self.assertEqual(ArticleDetailView, resolver.func.view_class)

    def test_en_articles_url_resolves(self):
        activate('en')
        resolver = resolve('/en/articles/')
        self.assertEqual('article:list', resolver.view_name)
        self.assertEqual(ArticleListView, resolver.func.view_class)

    def test_ru_articles_url_resolves(self):
        activate('ru')
        resolver = resolve('/ru/articles/')
        self.assertEqual('article:list', resolver.view_name)
        self.assertEqual(ArticleListView, resolver.func.view_class)

    def test_es_articles_url_resolves(self):
        activate('es')
        resolver = resolve('/es/articles/')
        self.assertEqual('article:list', resolver.view_name)
        self.assertEqual(ArticleListView, resolver.func.view_class)

    def test_en_articles_category_filtered_url_resolves(self):
        activate('en')
        resolver = resolve('/en/articles/some-category-slug/')
        self.assertEqual('article:list-filtered', resolver.view_name)
        self.assertEqual(ArticleListView, resolver.func.view_class)

    def test_ru_articles_category_filtered_url_resolves(self):
        activate('ru')
        resolver = resolve('/ru/articles/some-category-slug/')
        self.assertEqual('article:list-filtered', resolver.view_name)
        self.assertEqual(ArticleListView, resolver.func.view_class)

    def test_es_articles_category_filtered_url_resolves(self):
        activate('es')
        resolver = resolve('/es/articles/some-category-slug/')
        self.assertEqual('article:list-filtered', resolver.view_name)
        self.assertEqual(ArticleListView, resolver.func.view_class)

    def test_en_categories_url_resolves(self):
        activate('en')
        resolver = resolve('/en/categories/')
        self.assertEqual('article:category-list', resolver.view_name)
        self.assertEqual(CategoryListView, resolver.func.view_class)

    def test_ru_categories_url_resolves(self):
        activate('ru')
        resolver = resolve('/ru/categories/')
        self.assertEqual('article:category-list', resolver.view_name)
        self.assertEqual(CategoryListView, resolver.func.view_class)

    def test_es_categories_url_resolves(self):
        activate('es')
        resolver = resolve('/es/categories/')
        self.assertEqual('article:category-list', resolver.view_name)
        self.assertEqual(CategoryListView, resolver.func.view_class)
