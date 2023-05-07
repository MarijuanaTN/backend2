from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
import mysql.connector
# Create your views here.


def update_forex_data(request):
    # Connect to MySQL database
    mydb = mysql.connector.connect(
        host="pcdserver.mysql.database.azure.com",
        user="kson",
        password="Mohamed54427746",
        port=3306,
        database="api",
        
    )

    # Open a cursor to execute SQL commands
    mycursor = mydb.cursor()

    # API parameters
    symbol = 'EURUSD'  # Replace with the symbol you want to retrieve data for
    apikey = 'R1MDSQ8MKWE7ROUI'  # Replace with your Alpha Vantage API key
    url ='https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=EUR&to_currency=USD&apikey=R1MDSQ8MKWE7ROUI  '

    # Retrieve data from API
    response = requests.get(url)
    data = json.loads(response.text)
    exchange_rate = float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])
    date = data['Realtime Currency Exchange Rate']['6. Last Refreshed']
    bid_price = float(data['Realtime Currency Exchange Rate']['8. Bid Price'])
    ask_price = float(data['Realtime Currency Exchange Rate']['9. Ask Price'])

    # Insert data into the MySQL table
    sql = f"SELECT COUNT(*) FROM intraday_forexdata WHERE timestamp = '{date}' AND symbol = '{symbol}' AND bid_price = {bid_price} AND ask_price = {ask_price} AND exchange_rate = {exchange_rate}"
    mycursor.execute(sql)
    result = mycursor.fetchone()
    if result[0] == 0:
        sql = f"INSERT INTO intraday_forexdata (timestamp, symbol, bid_price, ask_price, exchange_rate) VALUES ('{date}', '{symbol}', {bid_price}, {ask_price}, {exchange_rate})"
        mycursor.execute(sql)
        mydb.commit()
        return HttpResponse('Forex data updated successfully!')
    else:
        return HttpResponse('Forex data already exists in database')
    

    
    
    

   