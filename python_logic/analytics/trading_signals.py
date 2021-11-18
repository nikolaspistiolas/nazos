import pymongo
from datetime import datetime

client = pymongo.MongoClient('mongodb://%s:%s@134.209.255.171' % ('nikolas', 'gwlGwl1q'))
db = client['production']
upcol = db['signals']
prices_col = db['stockdata']
algovariables_col = db['algotradevariables']
linear_results_col = db['linearresults']
active_stocks = [i['symbol'] for i in db['stocklists'].find({'active':True})]

variables = algovariables_col.find_one({})

up = {'Date':datetime.today()}

for stock in active_stocks:
    up_tmp = {'signal': 'stable'}
    try:
        last_price = prices_col.find({'symbol': stock}).sort('Date',direction=pymongo.DESCENDING).next()['Close']
        linear_result = linear_results_col.find({'symbol': stock}).sort('Date', pymongo.DESCENDING).next()
    except StopIteration:
        continue

    if linear_result['small_pred'] - variables['buy_sd'] * linear_result['small_sd'] >= last_price and \
        linear_result['medium_pred'] - variables['buy_sd'] * linear_result['medium_sd'] >= last_price and \
            linear_result['big_pred'] - variables['buy_sd'] * linear_result['big_sd'] >= last_price:
        up_tmp['signal'] = 'buy'
    if linear_result['small_pred'] + variables['sell_sd'] * linear_result['small_sd'] <= last_price and \
        linear_result['medium_pred'] + variables['sell_sd'] * linear_result['medium_sd'] <= last_price and \
            linear_result['big_pred'] + variables['sell_sd'] * linear_result['big_sd'] <= last_price:
        up_tmp['signal'] = 'sell'
    up_tmp['buy_price'] = min([linear_result['small_pred'] - variables['buy_sd'] * linear_result['small_sd'],
                               linear_result['medium_pred'] - variables['buy_sd'] * linear_result['medium_sd'],
                               linear_result['big_pred'] - variables['buy_sd'] * linear_result['big_sd']])
    up_tmp['sell_price'] = max([linear_result['small_pred'] + variables['sell_sd'] * linear_result['small_sd'],
                                linear_result['medium_pred'] + variables['sell_sd'] * linear_result['medium_sd'],
                                linear_result['big_pred'] + variables['sell_sd'] * linear_result['big_sd']])

    up[stock] = up_tmp
print(up)
upcol.insert_one(up)
