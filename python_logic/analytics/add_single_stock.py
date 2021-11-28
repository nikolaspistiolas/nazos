import pymongo
import yfinance as yf
from mongo_url import url

client = pymongo.MongoClient(f'{url}:27017',username='nikolas',password='gwlGwl1q')
db = client['production']
col = db['stockdata']
stock_list = db['stocklists']


for stock_name in stock_list:
    if col.find({'symbol':stock_name}).count() == 0:
        data = yf.Ticker(stock_name).history(start='2010-01-01')
        data = data.drop(['Dividends', 'Stock Splits'], axis=1)
        data['Date'] = data.index
        data = data.to_dict('records')
        for i in data:
            i['symbol'] = stock_name
            col.insert_one(i)
        stock_list.insert_one({'symbol': stock_name, 'active': True})