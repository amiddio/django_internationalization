from django.test import TestCase
from django.urls import resolve
from django.utils.translation import activate

from page.views import HomeView


class UrlsTest(TestCase):

    def test_en_home_page_url_resolves(self):
        activate('en')
        resolver = resolve('/en/')
        self.assertEqual('page:home', resolver.view_name)
        self.assertEqual(HomeView, resolver.func.view_class)

    def test_ru_home_page_url_resolves(self):
        activate('ru')
        resolver = resolve('/ru/')
        self.assertEqual('page:home', resolver.view_name)
        self.assertEqual(HomeView, resolver.func.view_class)

    def test_es_home_page_url_resolves(self):
        activate('es')
        resolver = resolve('/es/')
        self.assertEqual('page:home', resolver.view_name)
        self.assertEqual(HomeView, resolver.func.view_class)
