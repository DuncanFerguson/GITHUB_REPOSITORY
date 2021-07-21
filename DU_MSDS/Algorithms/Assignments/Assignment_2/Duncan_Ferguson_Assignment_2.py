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
            return [A[low][0], "Start Date"]
        else:
            A[low][0] = 0
            return A[low][0], A[low][1]
            # return 0
    # Divide
    mid = (low+high)//2
    # print(mid)

    # Conquer
    maxLeft = MSSDAC(A, low, mid)
    maxRight = MSSDAC(A, mid+1, high)

    # # Combine
    # TODO max number coming out. Need to capture the date
    maxLeft2Center = left2Center = [0, "Sell Date"]
    for i in range(mid, low - 1, -1):
        left2Center[0] += A[i][0]
        left2Center[1] = A[i][1]
        if left2Center[0] > maxLeft2Center[0]:
            maxLeft2Center = left2Center
        else:
            maxLeft2Center = maxLeft2Center

    maxRight2Center = right2Center = [0, "Sell Date"]
    for i in range(mid, low - 1, -1):
        right2Center[0] += A[i][0]
        right2Center[1] = A[i][1]
        if right2Center[0] > maxRight2Center[0]:
            maxRight2Center = right2Center
        else:
            maxRight2Center = maxRight2Center

    # print("MaxLeft", maxLeft, "maxLeft2Center:", maxLeft2Center)
    rmaxleft = maxLeft
    rmaxright = maxRight

    # TODO Chase the dates in here
    rmaxmid = [maxLeft2Center[0]+maxRight2Center[0], maxRight2Center[1]]
    if rmaxleft[0] > rmaxright[0] and rmaxleft[0] > rmaxmid[0]:
        return rmaxleft
    elif rmaxright[0] > rmaxleft[0] and rmaxright[0] > rmaxmid[0]:
        return rmaxright
    else:
        return rmaxmid
    #
    # print(rmaxleft, rmaxright, rmaxmid[0])


    # if rmaxleft[0] > maxLeft2Center[0]:
    #     if rmaxleft >
    #     return rmaxleft
    # else:
    #     return maxLeft2Center
    #
    # print("MaxLeft", maxRight, "maxLeft2Center:", maxRight2Center)
    #
    # if rmaxright[0] > maxRight2Center[0]:
    #     return rmaxright
    # else:
    #     return maxRight2Center

    # return max(maxLeft, maxLeft2Center)
    # return max(maxLeft, maxRight, maxLeft2Center + maxRight2Center)



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

