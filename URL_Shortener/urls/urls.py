from django.urls import path
from .views import get_original_url, get_url_analytics, shorten

urlpatterns = [
        path('shorten/', shorten, name='shorten'),
    path('<str:short_url>/', get_original_url, name='get_original_url'),
    path('analytics/<str:short_url>/', get_url_analytics, name='get_url_analytics'),



]
