from django.urls import path
from Daily.views import update_forex_data

urlpatterns = [
    path('Daily/', update_forex_data, name='Daily'),
]