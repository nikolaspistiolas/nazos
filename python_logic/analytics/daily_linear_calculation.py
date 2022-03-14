from linear_class import ComputeLinearRegression
import pymongo
from datetime import datetime

url = 'localhost'

client = pymongo.MongoClient(f'{url}:27017',username='nikolas',password='gwlGwl1q')
db = client['production']
symbols = db['stocklists'].find()

linear_params = db['linearvariables'].find_one({})

upload_col = db['linearresults']

for i in symbols:
    tmp_class = ComputeLinearRegression(i['symbol'], linear_params['big'], linear_params['medium'], linear_params['small'])
    date, data = tmp_class.get_data()

    res = tmp_class.multiple_regressions(data)
    up = {'symbol': i['symbol'],
          'Date': datetime.today(),
          'small': linear_params['small'],
          'medium': linear_params['medium'],
          'big': linear_params['big'],
          'small_pred': res[0][0][0],
          'small_sd': res[1],
          'medium_pred': res[2][0][0],
          'medium_sd': res[3],
          'big_pred': res[4][0][0],
          'big_sd': res[5]
          }
    upload_col.insert_one(up)
