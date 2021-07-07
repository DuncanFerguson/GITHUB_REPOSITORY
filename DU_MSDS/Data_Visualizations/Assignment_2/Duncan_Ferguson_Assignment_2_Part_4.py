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

df = yf.download('DRIP', '2021-01-01', '2021-01-31')

fig, (ax1, ax2) = plt.subplots(2)
# fig.suptitle("DRIP Prices and Volumes in January 2021")

ax1.plot(df['Close'])
ax1.set_title("Drip Closing Price")

ax2.plot(df['Volume'])
ax2.set_title("Drip Volumes")



plt.tight_layout()
plt.show()