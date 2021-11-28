import pymongo
from apis import alpaca_class
from datetime import datetime
from mongo_url import url


class TradingClass:
    def __init__(self):
        self.trade = alpaca_class.AlpacaTradingInterface()
        client = pymongo.MongoClient(f'{url}:27017',username='nikolas',password='gwlGwl1q')
        self.db = client['production']
        self.stocks = set([i['symbol'] for i in self.db['stocklists'].find({'active': True})])
        self.prices = []
        for i in self.stocks:
            self.prices.append(self.db['stockdata'].find({'symbol':i}).sort('Date', pymongo.DESCENDING).next()['Close'])
        self.signals = self.db['signals'].find().sort('Date', pymongo.DESCENDING).next()
        self.stop_loss = self.db['algotradevariables'].find().next()['stop_loss']

    def close_orders(self):
        open_symbols = self.get_open_orders_symbols()
        print(open_symbols)
        for i in open_symbols:

            if self.signals[i]['signal'] == 'sell':
                self.trade.close_order(i)
        return

    def open_order_with_signal(self):
        open_symbols = self.get_open_orders_symbols()
        for i in self.stocks:
            if i not in open_symbols and self.signals[i]['signal'] == 'buy':
                qty = self.get_quantity_for_symbol(i)
                self.trade.open_limit_order(i,qty,self.stop_loss, self.get_price_for_symbol(i))
        return

    def open_order_at_price(self):
        open_symbols = self.get_open_orders_symbols()
        will_open = []
        counter = len(open_symbols)
        for s,p in zip(self.stocks,self.prices):
            if s not in open_symbols and self.signals[s]['signal'] == 'buy':
                counter += 1
            if s not in open_symbols and self.signals[s]['signal'] == 'stable':
                will_open.append({'symbol': s,
                                  'power': abs( (self.signals[s]['buy_price'] - p)/(self.signals[s]['buy_price'] - self.signals[s]['sell_price']) ),
                                  'buy_price': self.signals[s]['buy_price']})
        will_open.sort(key=lambda x: x["power"])
        if counter >= 10:
            return -1
        will_open = will_open[:10-counter]
        for i in will_open:
            qty = self.get_specific_quantity_for_symbol(i['symbol'])
            self.trade.open_limit_order(i['symbol'], qty, self.stop_loss, i['buy_price'])

    def close_order_at_price(self):
        open_symbols = self.get_open_orders_symbols()
        for i in open_symbols:
            if self.signals[i]['signal'] == 'stable':
                sell_price = self.signals[i]['sell_price']
                qty = self.trade.get_active_orders()[i]['quantity']
                self.trade.open_limit_order(i,qty,None,sell_price)

    def get_open_orders_symbols(self):
        orders = self.trade.get_active_orders()
        return orders.keys()

    def get_value_to_open_order(self):
        cash = self.trade.get_cash_value()
        open_orders_count = len(self.get_open_orders_symbols())
        return cash / (10 - open_orders_count)

    def get_quantity_for_symbol(self,symbol):
        cash_for_symbol = self.get_value_to_open_order()
        last_close_price = self.db['stockdata'].find({'symbol' : symbol}).sort('Date', pymongo.DESCENDING).next()['Close']
        return int(cash_for_symbol/last_close_price)

    def get_specific_quantity_for_symbol(self, at_price):
        cash_for_symbol = self.get_value_to_open_order()
        return int(cash_for_symbol/at_price)

    def get_price_for_symbol(self, symbol):
        price = self.db['stockdata'].find({'symbol': symbol}).sort('Date',pymongo.DESCENDING).next()['Close']
        return 0.999 * price

    def begining_of_day(self):
        self.close_orders()
        self.close_order_at_price()
        self.open_order_at_price()
        self.open_order_with_signal()
        return

    def end_of_day(self):
        self.trade.cancel_orders()

    def get_all_orders(self):
        up = {}
        orders = self.trade.alpaca.list_orders(
            status='all',
            limit=500,
        )
        for i in orders:

            if i.canceled_at is None:
                if i.side == 'sell':
                    pass

    def get_account_info(self):
        up ={}
        up['Date'] = datetime.today()
        up['cash'] = self.trade.account.cash
        up['portfolio_value'] = self.trade.account.portfolio_value
        self.db['account_info'].insert_one(up)
        return




print(TradingClass().open_order_at_price())
