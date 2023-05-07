from django.urls import path
from IntraDay.views import update_forex_data

urlpatterns = [
    path('Intra_Day/', update_forex_data, name='forex_data'),
]