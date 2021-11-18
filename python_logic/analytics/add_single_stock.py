import sys
import pymongo
import yfinance as yf

stock_name = sys.argv[1]

client = pymongo.MongoClient('mongodb://%s:%s@127.0.0.1' % ('nikolas', 'gwlGwl1q'))
db = client['Nazos']
col = db['stockdata']
stock_list = db['stocklists']

data = yf.Ticker(stock_name).history(start='2010-01-01')
data = data.drop(['Dividends', 'Stock Splits'], axis=1)
data['Date'] = data.index
data = data.to_dict('records')
for i in (data):
    i['symbol'] = stock_name
    col.insert_one(i)
stock_list.insert_one({'symbol': stock_name,
                           'active': True})