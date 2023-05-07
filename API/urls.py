from django.urls import path
from API.views import DailyDataViewSet,IntraDayViewSet,WeeklyDataViewSet,MonthlyDataViewSet



urlpatterns = [
    path('intradayapi/', IntraDayViewSet.as_view(),name='intraday data'),
    path('dailyapi/', DailyDataViewSet.as_view(),name='daily data'),
    path('weeklyapi/', WeeklyDataViewSet.as_view(),name='weekly data'),
    path('monthlyapi/', MonthlyDataViewSet.as_view(),name='monthly data'),
    
]
