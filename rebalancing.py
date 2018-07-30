#!/usr/bin/python3

def get_better_symbole(exchange):
    data = exchange.client.get_exchange_info()['symbols']
    volume = 0.0
    coin = ""
    print (len(data))
    for i in data:
        print (i['symbol'])
        info = exchange.client.get_klines(symbol=i['symbol'], interval=exchange.client.KLINE_INTERVAL_1DAY, limit=1)
        if volume < float(info[0][4]):
            volume = float(info[0][4])
            coin = i['symbol']
    print (coin)
