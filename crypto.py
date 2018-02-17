#!/usr/bin/python3

import requests
import datetime
from datetime import date
from datetime import timedelta
import json
import time 

def price(symbol, comparison_symbols=['USD'], exchange=''):
    url = 'https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}'\
            .format(symbol.upper(),','.join(comparison_symbols).upper())
    # if exchange:
    #     url += '&e={}'.format(exchange)
    page = requests.get(url)
    data = page.json()
    return data



def historical(symbol,time_stamp,comparison_symbols=['USD']):

    url = 'https://min-api.cryptocompare.com/data/pricehistorical?fsym={}&tsyms={}&ts={}'\
            .format((symbol.upper()),','.join(comparison_symbols).upper(),time_stamp)
    page = requests.get(url)
    data = page.json()
    return data


def dateConverter(year,month,day):
    d = date(year,month,day)
    print(d)
    d = d - date(1970,1,1)
    unix_time = d.total_seconds()
    return unix_time

def profits(investment,currency,date):
    historical_price = historical(currency,date)
    units_bought = investment/historical_price[currency]['USD']
    current_price = price(currency)
    profit = units_bought*current_price['USD']
    return profit

if __name__ == '__main__':

    initial_investment = 1200
    histDate = dateConverter(int(2017),int(4),int(3))
    currency = 'ETH'
    gainz = profits(initial_investment,currency,histDate)
    print(gainz)
