import pymongo
import yfinance as yf
from sklearn.linear_model import LinearRegression
import numpy as np
from datetime import datetime
from mongo_url import url

class BacktestEnv:
    def __init__(self, stock_symbol, buy_sd=1.2, sell_sd=1.9, big=180, medium=130, small=50,stop_loss = 0.01, capital = 10000):
        self.client = pymongo.MongoClient(f'{url}:27017',username='nikolas',password='gwlGwl1q')
        self.stop_loss = stop_loss
        self.down_limit = buy_sd
        self.upper_limit = sell_sd
        self.big = big
        self.medium = medium
        self.small = small
        self.initial_capital = capital
        self.initial_stocks = 0
        self.data = yf.Ticker(stock_symbol).history(period="1d", start="2010-1-1")['Close'].values
        self.symbol = stock_symbol
        self.buys = [0, 0, 0]
        self.sells = [0, 0, 0]

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
        small_sd = self.linear_reg_sd(small_x, y[-self.small:], small_reg)
        med_sd = self.linear_reg_sd(med_x, y[-self.medium:], med_reg)
        big_sd = self.linear_reg_sd(big_x, y, big_reg)
        return small_reg, small_sd, med_reg, med_sd, big_reg, big_sd

    def trade(self):
        status = {'open_order': False,
                  'open_buy': 0,
                  'capital': self.initial_capital,
                  'stocks': self.initial_stocks,
                  'num_of_trades': 0
                  }
        for i in range(self.big, len(self.data)):
            x = self.data[i - self.big:i]

            small_reg, small_sd, med_reg, med_sd, big_reg, big_sd = self.multiple_regressions(x)
            small_pred = small_reg.predict([[self.small-1]])[0][0]
            medium_pred = med_reg.predict([[self.medium-1]])[0][0]
            big_pred = big_reg.predict([[self.big-1]])[0][0]
            real = x[-1]
            if status['open_order'] is True and (status['open_buy'] - real)/status['open_buy'] > self.stop_loss:
                status['capital'] = status['stocks'] * real
                status['open_order'] = False
                status['stocks'] = 0
                status['open_buy'] = 0
                continue
            if real < big_pred - self.down_limit * big_sd and real < medium_pred - self.down_limit * med_sd \
                    and real < small_pred - self.down_limit * small_sd:
                if status['open_order'] is False:
                    status['stocks'] = status['capital']/real
                    status['open_order'] = True
                    status['open_buy'] = real
                    status['capital'] = 0
                    status['num_of_trades'] +=1
            if real > big_pred + self.upper_limit * big_sd and real > medium_pred + self.upper_limit * med_sd \
                    and real > small_pred + self.upper_limit * small_sd:
                if status['open_order']:
                    status['capital'] = status['stocks'] * real
                    status['open_order'] = False
                    status['stocks'] = 0
                    status['open_buy'] = 0
        status['last_price'] = self.data[-1]
        return status

    def backtest(self):
        results = self.trade()
        results['capital'] += results['stocks'] * results['last_price']
        results['stocks'] = 0
        results['win_coef'] = self.data[-1]/ self.data[0]
        results['symbol'] = self.symbol
        del results['last_price']
        del results['open_buy']
        del results['open_order']
        del results['stocks']
        results['date'] = datetime.today()
        self.client['production']['backtest'].insert_one(results)


