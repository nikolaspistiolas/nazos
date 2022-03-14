import alpaca_trade_api as tradeapi
import pymongo

url = 'localhost'

class AlpacaTradingInterface:
    def __init__(self, apikey = 'PKH7WOBDRB1991IKV3TW',
                 secretkey = 'dz6MQwUsRhRFomIec8t8QcENC4zC2kDWjdkxGQMJ'):
        self.alpaca = tradeapi.REST(apikey,secretkey, 'https://paper-api.alpaca.markets', api_version='v2')

        self.account = self.alpaca.get_account()
        client = pymongo.MongoClient(f'{url}:27017', username='nikolas', password='gwlGwl1q')
        self.db = client['production']
        self.stockdata = self.db['stockdata']

    # OPENS A MARKET ORDER
    def open_market_order(self, symbol, amount):
        self.alpaca.submit_order(symbol=symbol, qty=amount, side='buy', type='market', extended_hours=False)

    # OPENS A LIMIT ORDER AT PRICE WITH STOPLOSS
    def open_limit_order(self, symbol, amount, stop_loss, at_price):
        second_price = self.alpaca.get_last_quote(symbol).bidprice
        if at_price < second_price:
            stop_loss = (1-stop_loss) * at_price
        else:
            stop_loss = (1 - stop_loss) * second_price
        self.alpaca.submit_order(symbol=symbol, qty=amount, side='buy', type='limit', order_class='braket',
                                 limit_price=at_price, extended_hours=False, stop_loss=dict(stop_price=str(stop_loss)))
        print(symbol, stop_loss)
        return

    def close_limit_order(self, symbol, at_price, amount):
        self.alpaca.submit_order(symbol=symbol, qty=amount, side='sell', type='limit', limit_price=at_price )
        return

    # CLOSES ALL ORDERS
    def close_order(self, symbol):
        self.alpaca.close_position(symbol)
        return

    # GET ALL ACTIVE ORDERS
    def get_active_orders(self):
        ret = {}
        for i in self.alpaca.list_positions():
            ret[i.symbol] ={
                'quantity': i.qty,
                'entry_price': i.avg_entry_price,
                'current_price': i.current_price
            }
        return ret


    # CLOSE ALL POSITIONS
    def close_all_orders(self):
        print('Closing Positions')
        self.alpaca.close_all_positions()
        return

    # CANCEL PENDING ORDERS
    def cancel_orders(self):
        self.alpaca.cancel_all_orders()
        return

    # GET ORDER HISTORY FOR SINGLE STOCK
    def get_order_history(self, symbol):
        return self.alpaca.get_latest_trades([symbol])

    # GET THE PORTFOLIO VALUE
    def get_portfolio_value(self):
        cash = float(self.account.cash)
        stocks_value = 0
        for i in self.get_active_orders():
            stocks_value += float(i['gty']) * float(i['current_price'])
        return cash + stocks_value

    def get_cash_value(self):
        return float(self.account.cash)

    def get_current_price(self, symbol):
        price = self.stockdata.find({'symbol':symbol}).sort('Date', pymongo.DESCENDING).next()['Close']
        return float(price)

tryclass = AlpacaTradingInterface()