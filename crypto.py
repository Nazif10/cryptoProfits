#!/usr/bin/python3

import requests
import datetime
import json
#import pandas as pd
#import matplotlib.pyplot as plt


def price(symbol, comparison_symbols=['USD','AUD'], exchange=''):
    url = 'https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}'\
            .format(symbol.upper(),','.join(comparison_symbols).upper())
    # if exchange:
    #     url += '&e={}'.format(exchange)
    page = requests.get(url)
    data = page.json()
    print(data)
    return data


# price('eth')

def historical(symbol,comparison_symbols=['USD'],time_stamp=1452680400):

    url = 'https://min-api.cryptocompare.com/data/pricehistorical?fsym={}&tsyms={}&ts={}'\
            .format((symbol.upper()),','.join(comparison_symbols).upper(),time_stamp)
    page = requests.get(url)
    data = page.json()
    print(data)

historical('ETH')
# def calcGainz(int investment,):
# 	ret = price('ltc',exchange='Poloniex')
# 	print(ret)

# 	gainz = 1000/int(ret['USD'])
# 	print(gainz)