class TradingClientInterface:
    def open_market_order(self, symbol, amount, stop_loss):
        pass

    def open_limit_order(self, symbol, amount, stop_loss, price):
        pass

    def close_order(self, symbol):
        pass

    def get_active_orders(self):
        pass

    def close_all_orders(self):
        pass

    def get_order_history(self, symbol = None):
        pass

    def get_balance(self):
        pass

    def get_portfolio_status(self):
        pass