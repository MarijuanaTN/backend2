from rest_framework import generics
from Daily.models import ForexData_Daily
from Weekly.models import ForexData_Weekly
from Monthly.models import ForexData_Monthly
from IntraDay.models import ForexData
from API.serializers import DailySerializer,IntraDaySerializer,WeeklySerializer,MonthlySerializer


class IntraDayViewSet(generics.ListAPIView):
    queryset=ForexData.objects.all()
    serializer_class=IntraDaySerializer

class DailyDataViewSet(generics.ListAPIView):
    queryset=ForexData_Daily.objects.all()
    serializer_class=DailySerializer

class WeeklyDataViewSet(generics.ListAPIView):
    queryset=ForexData_Weekly.objects.all()
    serializer_class=WeeklySerializer

class MonthlyDataViewSet(generics.ListAPIView):
    queryset=ForexData_Monthly.objects.all()
    serializer_class=MonthlySerializer


