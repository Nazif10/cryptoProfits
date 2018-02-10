#!/usr/bin/python3

import requests
import datetime
import json
#import pandas as pd
#import matplotlib.pyplot as plt

def price(symbol, comparison_symbols=['USD'], exchange=''):
    url = 'https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}'\
            .format(symbol.upper(), ','.join(comparison_symbols).upper())
    if exchange:
        url += '&e={}'.format(exchange)
    page = requests.get(url)
    data = page.json()
    return data

def calcGainz(int investment,):
	ret = price('ltc',exchange='Poloniex')
	print(ret)

	gainz = 1000/int(ret['USD'])
	print(gainz)