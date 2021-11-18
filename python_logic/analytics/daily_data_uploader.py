import yfinance as yf
import pymongo
from datetime import datetime, timedelta

client = pymongo.MongoClient('mongodb://%s:%s@134.209.255.171' % ('nikolas', 'gwlGwl1q'))
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

