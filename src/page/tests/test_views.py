from django.test import TestCase
from django.utils.translation import get_language


class HomeViewTest(TestCase):

    def test_view_home_page_is_exists(self):
        response = self.client.get(f'/{get_language()}/')
        self.assertEqual(200, response.status_code)

    def test_redirect_to_current_lang_page(self):
        response = self.client.get('/')
        self.assertEqual(302, response.status_code)
        self.assertEqual(f'/{get_language()}/', response.url)
