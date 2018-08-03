#!/usr/bin/python3

import sys
import os
import time
import datetime
import numpy as np
from docopt import docopt
from myHelp import bothelp
from loadData import LoadDatas
from mybinance import Binance
from mycoin import Coin
from charts import display_indica

coin = None

def main(argv, interval=60):
    global coin
    exchange = Binance()
    docopt(bothelp)
    pair = argv[1]
    chart = np.full(33, np.nan)
    print(" --- Venom's Bot ---\nBeginning of the session..\n")
    exchange.balances()

    ###
    coins = []
    for balance in exchange.mybalances['balances']:
        if float(balance['locked']) > 0 or float(balance['free']) > 0:
            coins.append(Coin(balance['asset'] + 'USDT', float(balance['free'])))
    ###

    start_time = time.time()
    print("\nLoading the last 500 candles...")
    exchange.historical_data(pair)
    data = LoadDatas(pair)
    print("500: OK | Temps d'execution: %.2f secondes\n" %
          float(time.time() - start_time))
    if len(sys.argv) > 2:
        interval = int(argv[2])
    coin = Coin(pair, 0)
    coin.set_indicators(data)
    coin.indicators.init_tree_config()
    while True:
        start_time = time.time()
        now = str(datetime.datetime.now())[:-7]
        time.sleep(interval)
        exchange.last_data(pair)
        data = LoadDatas(pair)
        coin.update_indicators(data)
        coin.indicators.predicted = np.concatenate([chart, coin.indicators.tree.predict(coin.indicators.dataset)])
        print("%s ---> %s = %.2f$ | futur prediction = %.2f$ | Temps d\'execution: %.2f secondes |" % (now, pair, float(
                coin.indicators.data['Close'].tail(1)), coin.indicators.predicted[-1:], float(time.time() - start_time - interval)))
    return (0)


if __name__ == "__main__":
    Start_time = time.time()
    try:
        main(sys.argv)
    except KeyboardInterrupt:
        display_indica(coin)
        print("   --- Arret du programme. Duree d\'execution: %i heures %i minutes %.2f secondes ---\n" %
              (((float(time.time() - Start_time)) / 3600), (((float(time.time() - Start_time)) % 3600) / 60), ((float(time.time() - Start_time)) % 60)))
