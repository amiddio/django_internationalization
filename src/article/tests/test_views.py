from django.test import TestCase
from django.urls import reverse
from django.utils.translation import activate
from parler.managers import TranslatableQuerySet

from article.models import Category, Article
from article.tests.mixins import ArticleTestMixin


class ArticleDetailViewTest(ArticleTestMixin, TestCase):

    @classmethod
    def setUpTestData(cls):
        activate('en')
        cls.create_category()
        category = Category.objects.get(translations__slug='category1_en')
        cls.create_article(category=category)

    def test_en_article_page(self):
        activate('en')
        url = reverse('article:detail', args=('article1_en',))
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertIsInstance(response.context['article'], Article)


class ArticleListViewTest(ArticleTestMixin, TestCase):

    @classmethod
    def setUpTestData(cls):
        activate('en')
        cls.create_category()
        category = Category.objects.get(translations__slug='category1_en')
        cls.create_article(category=category, num=1)
        cls.create_article(category=category, num=2)

    def test_en_articles_page(self):
        activate('en')
        url = reverse('article:list')
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertIsInstance(response.context['articles'], TranslatableQuerySet)
        self.assertTrue(2 == len(response.context['articles']))

    def test_ru_articles_page(self):
        activate('ru')
        url = reverse('article:list')
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertIsInstance(response.context['articles'], TranslatableQuerySet)
        self.assertTrue(2 == len(response.context['articles']))

    def test_es_articles_page(self):
        activate('es')
        url = reverse('article:list')
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertIsInstance(response.context['articles'], TranslatableQuerySet)
        self.assertTrue(2 == len(response.context['articles']))

    def test_articles_filtered_by_category(self):
        activate('en')
        url = reverse('article:list-filtered', args=('category1_en',))
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertIsInstance(response.context['articles'], TranslatableQuerySet)
        self.assertTrue(2 == len(response.context['articles']))

    def test_articles_filtered_by_category_negative(self):
        activate('en')
        url = reverse('article:list-filtered', args=('some-other-category-slug',))
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertIsInstance(response.context['articles'], TranslatableQuerySet)
        self.assertTrue(0 == len(response.context['articles']))


class CategoryListViewTest(ArticleTestMixin, TestCase):

    @classmethod
    def setUpTestData(cls):
        activate('en')
        cls.create_category(num=1)
        cls.create_category(num=2)
        cls.create_category(num=3)

    def test_en_categories_page(self):
        activate('en')
        url = reverse('article:category-list')
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertIsInstance(response.context['categories'], TranslatableQuerySet)
        self.assertTrue(3 == len(response.context['categories']))

    def test_ru_categories_page(self):
        activate('ru')
        url = reverse('article:category-list')
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertIsInstance(response.context['categories'], TranslatableQuerySet)
        self.assertTrue(3 == len(response.context['categories']))

    def test_es_categories_page(self):
        activate('es')
        url = reverse('article:category-list')
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertIsInstance(response.context['categories'], TranslatableQuerySet)
        self.assertTrue(3 == len(response.context['categories']))
