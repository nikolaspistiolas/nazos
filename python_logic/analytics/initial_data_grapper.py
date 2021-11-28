import pymongo
import yfinance as yf
import pandas as pd
import numpy as np
from mongo_url import url

client = pymongo.MongoClient(f'{url}:27017',username='nikolas',password='gwlGwl1q')
db = client['production']
col = db['stockdata']
stock_list = db['stocklists']

data = pd.read_excel('./initialdata/grid1_ilviqful.xlsx',usecols=['Securities'])
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
for s in symbols:
    try:
        print(s)
        data = yf.Ticker(s).history(start='2010-01-01')
        data = data.drop(['Dividends', 'Stock Splits'],axis=1)
        data['Date'] = data.index
        data = data.to_dict('records')
        for i in (data):
            i['symbol'] = s
            col.insert_one(i)
        stock_list.insert_one({'symbol': s,
                               'active': True})
    except:
        print('In Exception')