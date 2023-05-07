import requests
import json
import mysql.connector
from datetime import datetime
from django.http import HttpResponse

def update_forex_data(request):
    # Connect to MySQL database
   # mydb = mysql.connector.connect(
    #    host="pcdserver.mysql.database.azure.com",
     #   user="kson",
      #  password="Mohamed54427746",
       # database="api"
    #)
    mydb = mysql.connector.connect(user="kson", password="Mohamed54427746", host="pcdserver.mysql.database.azure.com", port=3306, database="api",)

    # Open a cursor to execute SQL commands
    mycursor = mydb.cursor()

    # API parameters
    symbol = 'EURUSD'  # Replace with the symbol you want to retrieve data for
    apikey = 'R1MDSQ8MKWE7ROUI'  # Replace with your Alpha Vantage API key
    url = 'https://www.alphavantage.co/query?function=FX_MONTHLY&from_symbol=EUR&to_symbol=USD&apikey=R1MDSQ8MKWE7ROUI'

    # Retrieve data from API
    response = requests.get(url)
    data = json.loads(response.text)

    # Extract data from the API response and insert it into the MySQL table
    for date, values in data['Time Series FX (Monthly)'].items():
        timestamp = datetime.strptime(date, '%Y-%m-%d')
        open_price = float(values['1. open'])
        high_price = float(values['2. high'])
        low_price = float(values['3. low'])
        close_price = float(values['4. close'])

        # Check if the row already exists in the table
        sql = f"SELECT COUNT(*) FROM api_forexdata_Monthly WHERE timestamp = '{timestamp}' AND symbol = '{symbol}' AND open_price = {open_price} AND high_price = {high_price} AND low_price = {low_price} AND close_price = {close_price}"
        mycursor.execute(sql)
        result = mycursor.fetchone()

        # Insert the row if it doesn't already exist in the table
        if result[0] == 0:
            sql = f"INSERT INTO api_forexdata_Monthly (timestamp, symbol, open_price, high_price, low_price, close_price) VALUES ('{timestamp}', '{symbol}', {open_price}, {high_price}, {low_price}, {close_price})"
            mycursor.execute(sql)
            mydb.commit()

    return HttpResponse('Forex data updated successfully!')
