# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4433
# Assignment: Assignment 2
# Date 7/8/2021

""" Assignment 2, Part 4: Pull from Yahoo! Finance the closing prices and volumes of the
stock of your choice over the trading days of one month, and plot the prices and volumes
on a canvas in two separate panels, one above the other, with the dates aligned.
"""

import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.cbook as cbook

df = yf.download(tickers='DRIP', start='2021-01-01', end='2021-01-31')

fig, ax = plt.subplots(nrows=2, ncols=1)

# Setting Up Close Price Graph
ax[0].plot(df['Close'], color='r')
ax[0].set_title("Drip Closing Price")
ax[0].xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))

# Setting Up Volumes Graph
ax[1].plot(df['Volume'])
ax[1].set_title("Drip Volumes")
ax[1].xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))

plt.tight_layout()
plt.show()