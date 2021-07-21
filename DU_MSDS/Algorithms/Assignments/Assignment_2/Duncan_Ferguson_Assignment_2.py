# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4581
# Assignment: Assignment 2
# Date 8/6/2021

# Use Divide Conquere
# import math
import pandas as pd

# Divide and Conquer Algorithm
def MSSDAC(A, low=0, high=None):
    """DAC: Stock Price"""
    if high == None:
        high = len(A) - 1

    # Base Case
    # print(A[low][0], A[low][1])
    if low == high:
        if A[low][0] > 0:
            return A[low][0], A[low][1]
        else:
            A[low][0] = 0
            return A[low][0], A[low][1]

    # Divide
    mid = (low+high)//2
    # print(mid)

    # Conquer
    maxLeft = MSSDAC(A, low, mid)
    maxRight = MSSDAC(A, mid+1, high)

    # # Combine
    # TODO This is where I Grabe the Dates
    maxLeft2Center = [0, 0]
    left2Center = [0, 0]

    for i in range(mid, low-1, -1):
        left2Center[0] += A[i][0]
        left2Center[1] = A[i][1]
        if left2Center[0] > maxLeft2Center[0]:
            maxLeft2Center = left2Center

    maxRight2Center = [0, 0]
    right2Center = [0, 0]

    for i in range(mid+1, high+1):
        right2Center[0] += A[i][0]
        right2Center[1] = A[i][1]
        if right2Center[0] > maxRight2Center[0]:
            maxRight2Center = right2Center

    if maxLeft > maxRight:
        if maxLeft > maxLeft2Center[0]+maxRight2Center[0]:
            return maxLeft
    # else:
    #     return maxRight

    # return maxRight2Center
    # return maxRight
    # return max(maxLeft[0], maxRight[0], maxLeft2Center[0]+maxRight2Center[0])
    # return max(maxLeft, maxRight, maxLeft2Center+maxRight2Center)


def calcCanges(prices):
    changes = []
    for row in range(len(prices)-1):
        delta = round(prices[row + 1][0] - prices[row][0], 3)
        changes.append([delta, prices[row][1]])  # TODO will want to check on this date
    return changes


def find_stock(file, symbol):
    stock = file[file['symbol'] == symbol]
    # Could probably do this quicker taking only the index values,
    stock = stock.reset_index()[['close', 'date']].values.tolist()
    stock = calcCanges(stock)
    # print(stock)
    print("Final Return", MSSDAC(stock))


def main():
    """Running the main code"""
    psa = pd.read_csv("prices-split-adjusted.csv")
    # print(psa.head())
    # stock = psa['symbol'].unique()
    find_stock(psa, 'AAPL')


if __name__ == '__main__':
    main()

