import requests
import os
import datetime
import logging
import pandas as pd

logging.basicConfig(format='[%(levelname)s]: %(message)s', level=logging.DEBUG)

api_key = os.environ['API_KEY']

def generate_dataframe():

    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=3)

    timeframe = []

    while start_date <= end_date:
        timeframe.append(start_date.isoformat())
        start_date += datetime.timedelta(days=1)

    return timeframe

def get_data():
    url = f'https://www.alphavantage.co/query?function=FX_DAILY&from_symbol=EUR&to_symbol=USD&outputsize=full&apikey={api_key}'
    r = requests.get(url)
    data = r.json()
    return data

def create_dataframe(data, timeframe):
    open = []
    close = []
    high = []
    low = []
    dates = []

    for date in timeframe:
        open.append(data['Time Series FX (Daily)'][date]["1. open"])
        high.append(data['Time Series FX (Daily)'][date]["2. high"])
        low.append(data['Time Series FX (Daily)'][date]["3. low"])
        close.append(data['Time Series FX (Daily)'][date]["4. close"])
        dates.append(date)

    market_data_dict = {
        'open': open,
        'high': high,
        'low': low,
        'close': close,
        'date': dates
    }

    market_data_df = pd.DataFrame(
        market_data_dict,
        columns=["open", "high", "low", "close", "date"]
    )

    return market_data_df

timeframe = generate_dataframe()
data = get_data()
dataframe = create_dataframe(data, timeframe)

'''
TODO:
Wrzucanie danych do bazy
'''