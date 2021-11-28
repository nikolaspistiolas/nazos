import yfinance as yf
import pymongo
from datetime import datetime, timedelta
from mongo_url import url

client = pymongo.MongoClient(f'{url}:27017',username='nikolas',password='gwlGwl1q')
col = client['production']['stockdata']

date = datetime.today() - timedelta(days = 1)
date = date.replace(hour=0,minute=0,second=0,microsecond=0)
print(date)



for symbol in client['Nazos']['stock_list'].find():
    symbol = symbol['symbol']
    data = yf.Ticker('AAPL').history(start=date-timedelta(days=2), end=date)
    print(data)
    data = data.drop(['Dividends', 'Stock Splits'],axis=1)
    data = data.to_dict('records')[0]
    data['Date'] = date
    col.insert_one(data)

