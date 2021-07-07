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

df = yf.download(tickers='DRIP', start='2021-01-01', end='2021-01-31')

fig, ax = plt.subplots(nrows=2, ncols=1)

# Setting Up Close Price Graph
ax[0].plot(df['Close'], color='r')
ax[0].set_title("'DRIP' Closing Price January 2021")

# Formatting The dates
ax[0].xaxis.set_major_locator(mdates.MonthLocator())
ax[0].xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
ax[0].xaxis.set_minor_locator(mdates.DayLocator())
ax[0].xaxis.set_minor_formatter(mdates.DateFormatter('%d'))
ax[0].tick_params(axis="x", which='minor', rotation=90)
ax[0].tick_params(which='major', pad=20)
ax[0].set_ylabel("'$' Closing Price")

# Setting Up Volumes Graph
ax[1].plot(df['Volume'], color='b')
ax[1].set_title("'DRIP' Volumes January 2021")

# Formating the Dates
ax[1].xaxis.set_major_locator(mdates.MonthLocator())
ax[1].xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
ax[1].xaxis.set_minor_locator(mdates.DayLocator())
ax[1].xaxis.set_minor_formatter(mdates.DateFormatter('%d'))
ax[1].tick_params(axis="x", which='minor', rotation=90)
ax[1].tick_params(which='major', pad=20)
ax[1].set_ylabel("Volume x 1e6")

plt.tight_layout()
plt.show()