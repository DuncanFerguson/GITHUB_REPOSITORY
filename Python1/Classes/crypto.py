#Import the requests library
import requests
#Import the datetime library
from datetime import datetime

TICKER_API_URL = 'https://api.cryptowat.ch/markets/bitfinex/'
headers = ['Closetime','OpenPrice', 'HighPrice','LowPrice', ]



def get_crypto_data(crypto): # make the api call to the crypto watch API for the passed in crypto

    resp = requests.get(f'{TICKER_API_URL}{crypto}/ohlc')
    doc = resp.json()
    return doc['result']['604800'] #Back to 2013

data = get_crypto_data('btcusd')

#Can get the date like this:
print(datetime.fromtimestamp(data[-1][0]))
