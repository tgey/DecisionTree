#!/usr/bin/python3

from mybinance import Binance
from myindicators import Indicators


class Coin():
    def __init__(self, name, wallet):
        self.__name = name
        self.__coins = wallet
        self.indicators = None

    def __del__(self):
        print("%s: %.8f" % (self.__name, self.__coins))

    def __str__(self):
        return "%s: %.8f coin(s)" % (self.__name, self.__coins)

    def get_name(self):
        return (self.__name)

    def get_coin(self):
        return (self.__coins)

    def set_coins(self, coins):
        self.__coins = coins

    def set_indicators(self, data):
        self.indicators = Indicators(self.__name, data)
        self.indicators.run()

    def update_indicators(self, data):
        self.indicators.data = data
        self.indicators.run()
