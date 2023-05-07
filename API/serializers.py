from rest_framework import serializers
from Daily.models import ForexData_Daily
from IntraDay.models import ForexData
from Weekly.models import ForexData_Weekly
from Monthly.models import ForexData_Monthly


class IntraDaySerializer(serializers.ModelSerializer):
    class Meta:
        model=ForexData
        fields=['timestamp','symbol','bid_price','ask_price','exchange_rate']

class DailySerializer(serializers.ModelSerializer):
    class Meta:
        model=ForexData_Daily
        fields= ['timestamp','symbol','open_price','high_price','low_price','close_price']

class WeeklySerializer(serializers.ModelSerializer):
    class Meta:
        model=ForexData_Weekly
        fields= ['timestamp','symbol','open_price','high_price','low_price','close_price']

class MonthlySerializer(serializers.ModelSerializer):
    class Meta:
        model=ForexData_Monthly
        fields= ['timestamp','symbol','open_price','high_price','low_price','close_price']