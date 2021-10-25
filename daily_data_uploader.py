import yfinance as yf
import pymongo
from datetime import datetime, timedelta

client = pymongo.MongoClient('mongodb://%s:%s@127.0.0.1' % ('nikolas', 'gwlGwl1q'))
col = client['Nazos']['daily_stocks']

date = datetime.today() - timedelta(days = 1)
date = date.replace(hour=0,minute=0,second=0,microsecond=0)
print(date)



for symbol in client['Nazos']['stock_list'].find({'active':True}):
    symbol = symbol['symbol']
    data = yf.Ticker('AAPL').history(start=date, end=date)
    data = data.drop(['Dividends', 'Stock Splits'],axis=1)
    data = data.to_dict('records')[0]
    data['Date'] = date
    col.insert_one(data)

