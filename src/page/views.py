from django.views.generic import TemplateView


class HomeView(TemplateView):
    """
    Представление главной страницы
    """

    template_name = 'index.html'
