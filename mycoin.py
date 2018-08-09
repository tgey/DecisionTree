#!/usr/bin/python3

from mybinance import Binance
from myindicators import Indicators


class Coin():
    """Coin's data class

    Returns:
        object -- contains coin's name, wallet
                    and indicators such as MACD, bollinger bands, ect..
    """

    def __init__(self, name, wallet):
        self.__name = name
        self.__coins = wallet
        self.indicators = None


    def __del__(self):
        """Class's destructor
        """

        print("%s: %.8f" % (self.__name, self.__coins))


    def __str__(self):
        """Overriding str's method

        Returns:
            str --
        """

        return "%s: %.8f coin(s)" % (self.__name, self.__coins)


    def get_name(self):
        """Name's getter

        Returns:
            str -- name of the coin
        """

        return (self.__name)


    def get_coin(self):
        """Wallet's getter

        Returns:
            int -- Wallet of a coin
        """

        return (self.__coins)


    def set_coins(self, coins):
        """Wallet's setter

        Arguments:
            coins {int} -- Wallet of a coin
        """

        self.__coins = coins


    def set_indicators(self, data):
        """Init indicators's class
            Run the class for the first time

        Arguments:
            data {Dataframe} -- Coin's data
        """

        self.indicators = Indicators(self.__name, data)
        self.indicators.run()


    def update_indicators(self, data):
        """ Update indicators's class with new data

        Arguments:
            data {Dataframe} -- Coin's data
        """

        self.indicators.data = data
        self.indicators.run()
