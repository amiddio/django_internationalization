from django.db import IntegrityError
from django.test import TestCase

from article.models import Category, Article
from article.tests.mixins import ArticleTestMixin


class CategoryModelTest(ArticleTestMixin, TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.create_category()

    def test_en_category_created(self):
        category = Category.objects.language('en').first()
        self.assertEqual('category1 en', category.name)
        self.assertEqual('category1_en', category.slug)

    def test_ru_category_created(self):
        category = Category.objects.language('ru').first()
        self.assertEqual('category1 ru', category.name)
        self.assertEqual('category1_ru', category.slug)

    def test_es_category_created(self):
        category = Category.objects.language('es').first()
        self.assertEqual('category1 es', category.name)
        self.assertEqual('category1_es', category.slug)

    def test_slug_is_unique(self):
        with self.assertRaises(IntegrityError):
            Category.objects.create(name='category2 en', slug='category1_en')


class ArticleModelTest(ArticleTestMixin, TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.create_category()
        category = Category.objects.get(translations__slug='category1_en')
        cls.create_article(category=category)

    def test_en_article_created(self):
        article = Article.objects.language('en').first()
        self.assertEqual('article1 en', article.name)
        self.assertEqual('article1_en', article.slug)

    def test_ru_article_created(self):
        article = Article.objects.language('ru').first()
        self.assertEqual('article1 ru', article.name)
        self.assertEqual('article1_ru', article.slug)

    def test_es_article_created(self):
        article = Article.objects.language('es').first()
        self.assertEqual('article1 es', article.name)
        self.assertEqual('article1_es', article.slug)

    def test_slug_is_unique(self):
        with self.assertRaises(IntegrityError):
            Article.objects.create(name='article2 en', slug='article1_en')

    def test_en_absolute_url(self):
        article = Article.objects.language('en').first()
        self.assertEquals('/en/article/article1_en/', article.get_absolute_url())
