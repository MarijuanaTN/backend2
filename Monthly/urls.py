from django.urls import path
from Monthly.views import update_forex_data

urlpatterns = [
    path('Monthly/', update_forex_data, name='Monthly'),
]