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
        # return max(low, high, A[low])
    # TODO There was additional code ehre from the class example
        if A[low][0] > 0:
            return A[low][0]
        else:
            return 0

    # Divide
    mid = (low+high)//2
    # print(mid)
    # # # Conquer
    maxLeft = MSSDAC(A, low, mid)
    maxRight = MSSDAC(A, mid+1, high)

    # # # Combine
    maxLeft2Center = [0, "Buy Date", "Sell Date"]
    left2Center = [0, "Buy Date", "Sell Date"]

    #  Center part of conquer
    for i in range(mid, low-1, -1):
        left2Center[0] += A[i][0]
        # print("Left Center", A[i][0])
        maxLeft2Center[0] = max(left2Center[0], maxLeft2Center[0])

    maxRight2Center = [0, "Buy Date", "Sell Date"]
    right2Center = [0, "Buy Date", "Sell Date"]
    for i in range(mid+1, high+1):
        right2Center[0] += A[i][0]
        # print("Right Center", A[i][0])
        maxRight2Center[0] = max(right2Center[0], maxRight2Center[0])

    # print(right2Center)
    print(maxRight2Center[0])
    return max(maxLeft, maxRight, maxLeft2Center[0]+maxRight2Center[0])


def calcCanges(prices):
    """This Function calculates the daily gains or losses.
    It is also adding a day index."""
    changes = []
    day = 0
    for row in range(len(prices)-1):
        delta = round(prices[row + 1][0] - prices[row][0], 3)
        day += 1
        changes.append([delta, day])  # TODO will want to check on this date
    return changes


def find_stock(file, symbol):
    stock = file[file['symbol'] == symbol]
    # stock.round(decimals=0, )


    # THis is to pull the list a bit differently
    # stock = stock[['date', 'close']]
    # stock = stock['close'].tolist()
    # TODO Revert this back. Only need to send one row through
    stock = stock.reset_index()[['close', 'date']].values.tolist()


    # print(stock)
    # Below Code is tester to see csv
    # np.savetxt("Apple_Stock.csv", stock, delimiter=",", fmt='% s')

    # Still want two rows coming out though
    stock = calcCanges(stock)
    # print(stock)

    # print(stock)
    print(MSSDAC(stock))

def main():
    """Running the main code"""
    psa = pd.read_csv("prices-split-adjusted.csv")
    find_stock(psa, 'AAPL')


if __name__ == '__main__':
    main()