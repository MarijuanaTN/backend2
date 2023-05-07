from Weekly.views import update_forex_data
from django.urls import path

urlpatterns = [
    path('Weekly/', update_forex_data, name='Weekly'),
]