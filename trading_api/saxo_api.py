import requests
import saxo_openapi
import saxo_openapi.endpoints.accounthistory as ah
import saxo_openapi.endpoints.trading as tr
import saxo_openapi.endpoints.portfolio as port
from interface import TradingClientInterface
import json

token = 'eyJhbGciOiJFUzI1NiIsIng1dCI6IjhGQzE5Qjc0MzFCNjNFNTVCNjc0M0QwQTc5MjMzNjZCREZGOEI4NTAifQ.eyJvYWEiOiI3Nzc3NSIsImlzcyI6Im9hIiwiYWlkIjoiMTA5IiwidWlkIjoiYVNmcFV6TmUtbUNnNW95Nkt6M1F3Zz09IiwiY2lkIjoiYVNmcFV6TmUtbUNnNW95Nkt6M1F3Zz09IiwiaXNhIjoiRmFsc2UiLCJ0aWQiOiIyMDAyIiwic2lkIjoiN2ViNjAwOTY0MWQyNDZkOGFmM2ZhOTQ1MWY2MzJkNTAiLCJkZ2kiOiI4NCIsImV4cCI6IjE2MzU0MTMyNjEiLCJvYWwiOiIxRiJ9.jZHWeW9JiMrehFfv1TIvdmfEfkP23RMK32pT-PCG7fCPZ_2YeTpaeiWPEZbvAzDHsiK49kWyzQsazpGyQx2Dyw'

class SaxoApi(TradingClientInterface):
    def __init__(self, token):
        self.token = token
        self.client = saxo_openapi.API(access_token=self.token)


    def get_data_from_token(self):
        return requests.get('https://gateway.saxobank.com/sim/openapi/port/v1/users/me').json()

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
        r = ah.accountvalues.AccountSummary(ClientKey='aSfpUzNe-mCg5oy6Kz3Qwg==')
        return self.client.request(r)

test = SaxoApi(token)
print(test.get_data_from_token())