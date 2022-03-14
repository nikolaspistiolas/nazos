import yfinance as yf
import pymongo
from datetime import datetime, timedelta

url = '134.209.255.171'

client = pymongo.MongoClient(f'{url}:27017',username='nikolas',password='gwlGwl1q')
col = client['production']['stockdata']

date = datetime.today() - timedelta(days=1)
date = date.replace(hour=0, minute=0, second=0, microsecond=0)
print(date)



for symbol in client['production']['stocklists'].find():

    symbol = symbol['symbol']
    data = yf.Ticker('AAPL').history(start=date-timedelta(days=2), end=date)

    data = data.drop(['Dividends', 'Stock Splits'],axis=1)
    data = data.to_dict('records')[0]
    data['Date'] = date
    print(data)
    col.insert_one(data)

