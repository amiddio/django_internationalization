from django.urls import path

from page.views import HomeView

app_name = 'page'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]
