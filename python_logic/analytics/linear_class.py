from sklearn.linear_model import LinearRegression
import numpy as np
import pymongo
import pandas as pd

url = '134.209.255.171'

class ComputeLinearRegression:
    def __init__(self, symbol, big, medium, small):
        self.symbol = symbol
        self.big = big
        self.medium = medium
        self.small = small
        client = pymongo.MongoClient(f'{url}:27017',username='nikolas',password='gwlGwl1q')
        db = client['production']
        self.col = db['stockdata']

    def get_data(self):
        data = [i for i in self.col.find({'symbol': self.symbol})]
        df = pd.DataFrame.from_records(data)
        return df.iloc[-1].index, df['Close'].to_numpy()[-self.big :]

    def linear_reg_sd(self, x, y, line: LinearRegression):
        if len(x) != len(y):
            print('Not same len')
            raise ValueError
        sumi = 0
        predicted = line.predict(y)
        for i in range(len(y)):
            sumi += (predicted[i][0] - x[i][0]) ** 2

        sumi /= len(y)
        return sumi ** 0.5

    def multiple_regressions(self, x):
        y = np.arange(stop=self.big).reshape(-1, 1)
        big_x = x[-self.big:].reshape(-1, 1)
        med_x = x[-self.medium:].reshape(-1, 1)
        small_x = x[-self.small:].reshape(-1, 1)
        small_reg = LinearRegression(copy_X=True, fit_intercept=True, n_jobs=-1, normalize=False)
        med_reg = LinearRegression(copy_X=True, fit_intercept=True, n_jobs=-1, normalize=False)
        big_reg = LinearRegression(copy_X=True, fit_intercept=True, n_jobs=-1, normalize=False)
        small_reg.fit(y[:self.small], small_x)
        med_reg.fit(y[:self.medium], med_x)
        big_reg.fit(y, big_x)
        small_sd = self.linear_reg_sd(small_x, y[:self.small], small_reg)
        med_sd = self.linear_reg_sd(med_x, y[:self.medium], med_reg)
        big_sd = self.linear_reg_sd(big_x, y, big_reg)
        return small_reg.predict([[self.small]]), small_sd, med_reg.predict([[self.medium]]), med_sd, \
               big_reg.predict([[self.big]]), big_sd

