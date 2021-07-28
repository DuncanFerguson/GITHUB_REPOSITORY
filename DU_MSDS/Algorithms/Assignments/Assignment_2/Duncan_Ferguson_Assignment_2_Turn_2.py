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
            # print("LowLeft?", A[low], "Low Date:", low, "Date High", high)
            return A[low]
        else:
            # print("HighRight?", A[high], "Low Dat:", low, "HIgh Date", high)
            return 0

    # Divide
    mid = (low+high)//2
    # maxRightHigh = mid
    # maxRightLow = high
    # maxLeftLow = low
    # maxLeftHigh = mid

    # Conquer
    maxLeft = MSSDAC(A, low, mid)
    maxRight = MSSDAC(A, mid+1, high)

    # Combine
    maxLeft2Center = left2Center = 0
    maxLeftLow = maxCenterLow = 0
    for i in range(mid, low-1, -1):
        maxLeftLow = i
        left2Center += A[i]
        if left2Center > maxLeft2Center:
            maxLeft2Center = left2Center
            maxCenterLow = i

    maxRight2Center = right2Center = 0
    maxRightHigh = maxCenterHigh = mid
    for i in range(mid+1, high+1):
        maxRightHigh = i
        right2Center += A[i]
        if right2Center > maxRight2Center:
            maxRight2Center = right2Center
            maxCenterHigh = i

    maxCenter = maxLeft2Center + maxRight2Center
    print("Max Center", maxCenter)
    print("Max Center Low", maxCenterLow)
    print("Max Center High", maxCenterHigh)

    print("maxLeft", maxLeft)
    print("maxLeft Low", maxLeftLow)
    # print("maxLeft High", maxLeftHigh)

    print("maxRight", maxRight)
    # print("maxRightLow", maxRightLow)
    print("maxRightHigh", maxRightHigh)

    if maxLeft > maxRight and maxLeft > maxCenter:
        print("Left Hit")
    #     # TODO Get This return to rip
    #     return maxLeft, maxLeftLow, maxLeftHigh
        return maxLeft
    elif maxRight > maxLeft and maxRight > maxCenter:
        print("Right Hit")
        # TODO Get This return to rip
        # return maxRight, maxRightLow, maxRightHigh
        return maxRight
    else:
        # TODO Get This Return
        # return maxCenter, maxCenterLow, maxCenterHigh
        print("Center Hit!")
        return maxCenter



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
    my_df = pd.DataFrame(stock)
    # my_df.to_csv('AAPL.csv', index=False, header=False)  # For Saving the data an looking at

    # Still want two rows coming out though
    stock = calcCanges(stock)

    # TODO get the start and end dates for these sales to come through
    print(MSSDAC(stock))

    # maxProfit, maxLow, maxHigh = MSSDAC(stock)
    # print(symbol,"-->: ", maxProfit, " buy on day: ", maxLow, "sell on day: ", maxHigh)

def main():
    """Running the main code"""
    psa = pd.read_csv("prices-split-adjusted.csv")
    find_stock(psa, 'AAPL')


if __name__ == '__main__':
    main()