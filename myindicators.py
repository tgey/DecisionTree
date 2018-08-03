#!/usr/bin/python3

import talib
import numpy as np
import pandas as pd
import loadData as ld

from sklearn.metrics import mean_absolute_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split


class Indicators():
    def __init__(self, symbol, data):

        ### Historical data ###
        self.data = data

        ### Machine Learning ###
        self.tree = RandomForestRegressor(max_leaf_nodes=28)
        self.predicted = None
        self.dataset = None

        ### Moving Average ###
        self.ma9 = []

        ### MACD ###
        self.macd = []
        self.macdsignal = []
        self.macdhist = []

        ### Bollinger bands ###
        self.bollup = []
        self.bollmid = []
        self.bolllow = []

        ### RSI ###
        self.rsi = []
        self.stochrsi = []

        ### stochastiques ###
        self.slowd = []
        self.slowk = []

        self.cci = []
        self.mfi = []

    def set_ma9(self):
        self.ma9 = talib.SMA(np.array(self.data['Close'], dtype='f8'), 9)

    def set_macd(self):
        self.macd, self.macdsignal, self.macdhist = talib.MACD(
            np.array(self.data['Close'], dtype='f8'),
            fastperiod=12, slowperiod=26, signalperiod=9)

    def set_bbands(self):
        self.bollup, self.bollmid, self.bolllow = talib.BBANDS(
            np.array(self.data['Close'], dtype='f8'), timeperiod=14)

    def set_rsi(self):
        self.rsi = talib.RSI(np.array(self.data['Close'], dtype='f8'), timeperiod=14)

    def set_stoch(self):
        self.slowk, self.slowd = talib.STOCH(np.array(self.data['High'], dtype='f8'),
                                             np.array(self.data['Low'], dtype='f8'),
                                             np.array(self.data['Close'], dtype='f8'),
                                             fastk_period=5, slowk_period=3, slowd_period=3)

    def set_cci(self):
        self.cci = talib.CCI(np.array(self.data['High'], dtype='f8'),
                             np.array(self.data['Low'], dtype='f8'),
                             np.array(self.data['Close'], dtype='f8'),
                             timeperiod=14)

    def set_mfi(self):
        self.mfi = talib.MFI(np.array(self.data['High'], dtype='f8'),
                             np.array(self.data['Low'], dtype='f8'),
                             np.array(self.data['Close'], dtype='f8'),
                             np.array(self.data['Volume'], dtype='f8'),
                             timeperiod=14)

    def init_tree_config(self):
        train_X, val_X, train_y, val_y = train_test_split(self.dataset, self.data['Close'][34:],random_state = 0)
        x = 100.0
        leaf = 0
        for max_leaf_nodes in range(2, 1000):
            model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
            model.fit(train_X, train_y)
            preds_val = model.predict(val_X)
            my_mae = mean_absolute_error(val_y, preds_val)
            if my_mae < x:
                x = float(my_mae)
                leaf = max_leaf_nodes
        print("Max leaf nodes: %d  \t\t Mean Absolute Error:  %.2f" % (leaf, x))
        self.tree = DecisionTreeRegressor(max_leaf_nodes=leaf)
        self.tree.fit(train_X, train_y)

    def run(self):
        self.set_ma9()
        self.set_macd()
        self.set_bbands()
        self.set_rsi()
        self.set_stoch()
        self.set_cci()
        self.set_mfi()
        self.dataset = pd.DataFrame({
                'ma9': self.ma9[33:len(self.data) - 1],
                'macd': self.macd[33:len(self.data) - 1],
                'rsi': self.rsi[33:len(self.data) - 1],
                'bollup': self.bollup[33:len(self.data) - 1],
                'bollmid': self.bollmid[33:len(self.data) - 1],
                'bolllow': self.bolllow[33:len(self.data) - 1]
                })
