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
    # print(A)

    # Base Case If there is only one element
    if low == high:
        # return max(low, high, A[low])
        # TODO There was additional code ehre from the class example
        if A[low] > 0:
            # print("LowLeft?", A[low], "Low Date:", 0, "Date High", high)
            return A[low], 0, high
        else:
            # print("HighRight?", A[high], "Low Dat:", 0, "HIgh Date", high)
            return 0, 0, high

    # Divide
    mid = (low+high)//2

    # Conquer
    maxLeft = MSSDAC(A, low, mid)
    maxRight = MSSDAC(A, mid+1, high)

    # TODO This is where I could be passing through the lows and highs
    maxLeft = maxLeft[0]
    # maxLeftLow = maxLeft[1]
    # maxLeftHigh = maxLeft[2]

    maxRight = maxRight[0]
    # maxRightLow = maxRight[1]
    # maxRightHigh = maxRight[2]

    # Combine
    maxLeft2Center = left2Center = 0
    maxLeftLow = maxCenterLow = 0
    maxLeftHigh = mid
    for i in range(mid, low-1, -1):
        maxLeftLow = i
        left2Center += A[i]
        if left2Center > maxLeft2Center:
            maxLeft2Center = left2Center
            maxCenterLow = i


    maxRight2Center = right2Center = 0
    maxRightHigh = maxCenterHigh = mid
    maxRightLow = mid
    for i in range(mid+1, high+1):
        maxRightHigh = i
        right2Center += A[i]
        if right2Center > maxRight2Center:
            maxRight2Center = right2Center
            maxCenterHigh = i

    maxCenter = maxLeft2Center + maxRight2Center

    if maxLeft > maxRight and maxLeft > maxCenter:
        # print("Left Hit", maxLeft, maxLeftLow, maxLeftHigh)
        return maxLeft, maxLeftLow, maxLeftHigh
    elif maxRight > maxLeft and maxRight > maxCenter:
        # print("Right Hit", maxRight, maxRightLow, maxRightHigh)
        return maxRight, maxRightLow, maxRightHigh
    else:
        # print("Center Hit!", maxCenter, maxCenterLow, maxCenterHigh)
        return maxCenter, maxCenterLow, maxCenterHigh

def calcCanges(prices):
    """This Function calculates the daily gains or losses.
    It is also adding a day index."""
    changes = [round(prices[row + 1][0] - prices[row][0], 3) for row in range(len(prices)-1)]
    # changes = []
    # for row in range(len(prices)-1):
        # delta = round(prices[row + 1][0] - prices[row][0], 3)
        # changes.append(delta)
    return changes


def find_stock(file, symbol):
    stock = file[file['symbol'] == symbol]
    stock = stock.reset_index()[['close', 'date']].values.tolist()

    # This is to pull down the sheet so that it can be looked at
    # my_df = pd.DataFrame(stock)
    # my_df.to_csv('AAPL.csv', index=False, header=False)  # For Saving the data an looking at

    # Still want two rows coming out though
    stock = calcCanges(stock)

    maxProfit, maxLow, maxHigh= MSSDAC(stock)
    maxLow = file['date'][maxLow]
    maxHigh =file['date'][maxHigh]

    return maxProfit, maxLow, maxHigh
    # print(maxProfit, maxLow, maxHigh)
    #
    # # maxProfit, maxLow, maxHigh = MSSDAC(stock)
    # print(symbol, "-->: ", maxProfit, "\n", " buy on day: ", maxLow, file['date'][maxLow],"\n",
    #                                 "sell on day: ", maxHigh, file['date'][maxHigh])
    # # TODO Make The translations
    # # print(file['date'][maxLow])
    # sfile = pd.read_csv("securities.csv")
    # print(sfile.columns)
    # add_info = sfile[sfile['Ticker symbol'] == symbol]
    # print(add_info)

def main():
    """Running the main code"""
    psa = pd.read_csv("prices-split-adjusted.csv")
    # print(psa.columns)
    tickers = psa['symbol'].unique()
    # print(tickers)

    bestProfit = 0

    for ticker in tickers:
        # print(ticker)
        profit, buyDate, sellDate = find_stock(psa, ticker)
        if profit > bestProfit:
            bestName = ticker
            bestProfit = profit
            bestBuyDate = buyDate
            bestSellDate = sellDate

    # find_stock(psa, 'MMM')
    # find_stock(psa, 'ABT')
    # find_stock(psa, 'ATVI')
    # find_stock(psa, "PCLN")

    sfile = pd.read_csv("securities.csv")
    # print(sfile.columns)
    add_info = sfile[sfile['Ticker symbol'] == bestName]
    print("Best stock to buy:", add_info["Security"].values[0], " on ", bestBuyDate, "\n and sell on ", bestSellDate,
          " with a profit of ", bestProfit)


if __name__ == '__main__':
    main()