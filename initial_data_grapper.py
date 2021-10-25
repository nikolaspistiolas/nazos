import pymongo
import yfinance as yf
import pandas as pd
import numpy as np

client = pymongo.MongoClient('mongodb://%s:%s@127.0.0.1' % ('nikolas', 'gwlGwl1q'))
db = client['Nazos']
col = db['daily_stocks']
stock_list = db['stock_list']

data = pd.read_excel('./grid1_ilviqful.xlsx',usecols=['Securities'])
data = data.to_numpy()
symbols = []
names = []
for i in data:
    i = i[0]
    if i is not None and i is not np.nan:
        symbols.append(i.split(' ')[0])

for i in symbols:
    stock_list.insert_one({'symbol': i, 'active': True})


print(symbols)
input('END???')
for s in symbols:
    stock_list.insert_one({'symbol': s,
                           'active': True})
    data = yf.Ticker(s).history(start='2010-01-01')
    data = data.drop(['Dividends', 'Stock Splits'],axis=1)
    data['Date'] = data.index
    data = data.to_dict('records')
    for i in (data):
        i['symbol'] = s
        col.insert_one(i)
