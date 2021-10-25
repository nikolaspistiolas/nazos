from linear_class import ComputeLinearRegression
import pymongo

client = pymongo.MongoClient('mongodb://%s:%s@127.0.0.1' % ('nikolas', 'gwlGwl1q'))
db = client['Nazos']
symbols = db['stock_list'].find()

linear_params = db['linear_parameter'].find_one({})

upload_col = db['linear_regression_data']

for i in symbols:
    tmp_class = ComputeLinearRegression(i['symbol'], linear_params['big'], linear_params['medium'], linear_params['small'])
    date, data = tmp_class.get_data()
    res = tmp_class.multiple_regressions(data)
    up = {'symbol': i['symbol'],
          'Date': date,
          'small_pred': res[0],
          'small_sd': res[1],
          'medium_pred': res[2],
          'medium_sd': res[3],
          'big_pred': res[4],
          'big_sd': res[5]
          }
    upload_col.insert_one(up)
