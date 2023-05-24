from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from Daily.models import ForexData_Daily
from Weekly.models import ForexData_Weekly
from Monthly.models import ForexData_Monthly
from IntraDay.models import ForexData
from API.serializers import DailySerializer,IntraDaySerializer,WeeklySerializer,MonthlySerializer,ExchangeSerializer

import numpy as np # linear algebra
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle,os

def make_prediction(date):
    file_path = os.path.abspath('API/model_predict')
    with open(file_path,'rb') as f:
        model=pickle.load(f)
    v=pd.DataFrame(date,index=[0])
    pr=model.predict(v)
    print(pr)
    return pr

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


class PredictView(APIView):
    serializer_class=ExchangeSerializer
    def post(self,request,format=None):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            json_data=serializer.data
            day=serializer.validated_data['date'].day
            month=serializer.validated_data['date'].month
            year=serializer.validated_data['date'].year
            input_data=pd.DataFrame([json_data])
            input_date={'day':day,'month':month,'year':year}
            pr=make_prediction(input_date)
            print(pr)
            if serializer.validated_data['mode']=='predictfx':
                return Response({'prediction': pr})
            else:
                strike=serializer.validated_data['strike']
                premium=serializer.validated_data['premium']
                type=serializer.validated_data['type']
                optionprice=10000*(strike+premium)
                fxprice=10000*pr
                diff=optionprice-fxprice
                if diff>0:
                    if type=='call':
                        message='We predict that by buying a call option you probably can loose'
                    if type=='put':
                        message='We predict that by buying a put option you probably can win'
                else:
                    if type=='call':
                        message='We predict that by buying a call option you probably can win'
                    if type=='put':
                        message='We predict that by buying a put option you probably can loose'
                return Response({'message':message,'optionprice':optionprice,'predictedfxprice':fxprice})
        return Response(serializer.errors, status=400)

