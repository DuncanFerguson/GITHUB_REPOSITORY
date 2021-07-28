# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4581
# Assignment: Assignment 2
# Date 8/6/2021

# Use Divide Conquere
import pandas as pd
# import numpy as np

# Divide and Conquer Algorithm
def MSSDAC(A, low=0, high=None):
    if high == None:  # Turning the high into the length of list
        high = len(A) - 1

    # Base Case If there is only one element
    if low == high:
        return 0, A[low], A[high]

    # Divide
    mid = (low+high)//2

    # Conquer
    maxLeft, maxLeftLow, maxLeftHigh = MSSDAC(A, low, mid)
    maxRight, maxRightLow, maxRightHigh = MSSDAC(A, mid+1, high)

    # Combine
    maxCenterLow = maxLeft2Center = left2Center = 0
    for i in range(mid, low-1, -1):
        left2Center += A[i]
        if left2Center > maxLeft2Center:
            maxLeft2Center = left2Center
            maxCenterLow = i

    maxRight2Center = right2Center = 0
    maxCenterHigh = mid
    for i in range(mid+1, high+1):
        right2Center += A[i]
        if right2Center > maxRight2Center:
            maxRight2Center = right2Center
            maxCenterHigh = i

    maxCenter = maxLeft2Center + maxRight2Center

    if maxLeft > maxRight and maxLeft > maxCenter:
        return maxLeft, maxLeftLow, maxLeftHigh
    elif maxRight > maxLeft and maxRight > maxCenter:
        return maxRight, maxRightLow, maxRightHigh
    else:
        return maxCenter, maxCenterLow, maxCenterHigh

def calcCanges(prices):
    """This Function calculates the daily gains or losses.
    It is also adding a day index. Mostly from the class example put into one line"""
    changes = [round(prices[row + 1][0] - prices[row][0], 3) for row in range(len(prices)-1)]
    return changes


def find_stock(file, symbol):
    stock = file[file['symbol'] == symbol]
    stock = stock.reset_index()[['close', 'date']].values.tolist()

    # Still want two rows coming out though
    stock2 = calcCanges(stock)
    maxProfit, maxLow, maxHigh = MSSDAC(stock2)

    # Converting into dates
    maxLow = stock[maxLow][1]
    maxHigh = stock[maxHigh][1]

    return maxProfit, maxLow, maxHigh


def main():
    """Running the main code"""
    psa = pd.read_csv("prices-split-adjusted.csv")
    # psa = pd.read_csv("prices-split-adjusted_short_shorts.csv")
    # https://www.roelpeters.be/solved-dtypewarning-columns-have-mixed-types-specify-dtype-option-on-import-or-set-low-memory-in-pandas/
    # psa = pd.read_csv("prices-split-adjusted_v2.csv")
    # tickers = psa['symbol'].unique()
    # tickers = ["MMM", "ABT", "ATVI", "AAPL", "PCLN"]
    # tickers = ["MMM", "ABT", "ATVI", "AAPL"]
    tickers = ["MMM"]
    # tickers = ["WLTW"]

    bestProfit = 0

    for ticker in tickers:
        profit, buyDate, sellDate = find_stock(psa, ticker)
        if profit > bestProfit:
            bestName = ticker
            bestProfit = profit
            bestBuyDate = buyDate
            bestSellDate = sellDate

    sfile = pd.read_csv("securities.csv")

    add_info = sfile[sfile['Ticker symbol'] == bestName]
    print("Best stock to buy:", add_info["Security"].values[0], " on ", bestBuyDate, "\n and sell on ", bestSellDate,
          " with a profit of ", bestProfit)


if __name__ == '__main__':
    main()