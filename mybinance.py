#!/usr/bin/python3

import sys
from binance.client import Client
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
client = Client('api_key',
                'secret_key', {"verify": False, "timeout": 200000})

class Binance():
    """Binance Object

    Returns:
        object -- contains binance's data
    """

    def __init__(self):
        self.client = client
        self.mybalances = None

    def balances(self):
        """Get all balances
        """

        self.mybalances = self.client.get_account()

        for balance in self.mybalances['balances']:
            if float(balance['locked']) > 0 or float(balance['free']) > 0:
                print('%s: %s' % (balance['asset'], balance['free']))

    def balance(self, asset="BTC"):
        """Get a specific balance

        Keyword Arguments:
            asset {str} -- the coin's pair corresponding to your balance (default: {"BTC"})
        """

        balances = self.client.get_account()
        balances['balances'] = {item['asset']
            : item for item in balances['balances']}
        print(balances['balances'][asset]['free'])

    def orders(self, symbol, limit):

        orders = self.client.get_open_orders()
        print(orders)

    def tickers(self):
        return self.client.get_all_tickers()

    def server_time(self):
        return self.client.get_server_time()

    def openorders(self):
        return self.client.get_open_orders()

    def profits(self, asset='BTC'):

        coins = self.client.get_products()

        for coin in coins['data']:

            if coin['quoteAsset'] == asset:

                orders = self.client.get_order_book()
                lastBid = float(orders['bids'][0][0])  # last buy price (bid)
                lastAsk = float(orders['asks'][0][0])  # last sell price (ask)

                profit = (lastAsk - lastBid) / lastBid * 100

                print('%.2f%% profit : %s (bid:%.8f-ask%.8f)' %
                      (profit, coin['symbol'], lastBid, lastAsk))

    def historical_data(self, symbole):
        """Get the 500 last values for a specific symbole

        Arguments:
            symbole {str} -- coin's pair
        """

        info = self.client.get_klines(
            symbol=symbole, interval=self.client.KLINE_INTERVAL_1MINUTE)
        csvFile = open(symbole + ".csv", 'wb')
        csvFile.write(
            "Time,Open,High,Low,Close,Volume,Close time,Quote asset volume,Nb of trades,Buy base asset Vol,Buy quote asset Vol,Ignore\n".encode())
        for row in info:
            var = ','.join(str(e) for e in row)
            var = var[:-2]
            csvFile.write(str(var + "\n").encode())
        csvFile.close()

    def last_data(self, symbole):
        """get the last value for a specific symbole

        Arguments:
            symbole {str} -- coin's pair
        """

        info = self.client.get_klines(
            symbol=symbole, interval=self.client.KLINE_INTERVAL_1MINUTE, limit=1)
        csvFile = open(symbole + ".csv", 'a')
        for row in info:
            var = ','.join(str(e) for e in row)
            var = var[:-2]
            csvFile.write(str(var + "\n"))
        csvFile.close()
