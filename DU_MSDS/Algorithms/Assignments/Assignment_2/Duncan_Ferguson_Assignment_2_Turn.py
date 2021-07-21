# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4581
# Assignment: Assignment 2
# Date 8/6/2021

# Use Divide Conquere
import pandas as pd

# Divide and Conquer Algorithm
def MSSDAC(A, low=0, high=None):
    if high == None:
        high = len(A) - 1

    # print(low, high)
    # Base Case
    if low == high:
        if A[low][0] > 0:
            return A[low]
        else:
            return 0

    # Divide
    mid = (low+high)//2

    # # Conquer
    maxLeft = MSSDAC(A, low, mid)
    maxRight = MSSDAC(A, mid+1, high)
    #
    # # Combine
    maxLeft2Center = [0, "Buy Date", "Sell Date"]
    left2Center = [0, "Buy Date", "Sell Date"]

    for i in range(mid, low-1, -1):
        left2Center[0] += A[i][0]
        # left2Center[1] = "A[i][1]"
        print(A[i])
        print(maxLeft2Center)
        print(left2Center)
        # print(left2Center)
        # print(maxLeft2Center[i])

        # maxLeft2Center[i] = [max(left2Center[i][0], maxLeft2Center[i][0]), left2Center[i][1]]
    # return left2Center[0]
    # maxRight2Center = right2Center = 0
    # for i in range(mid+1, high+1):
    #     right2Center[0] += A[i][0]
    #     maxRight2Center = max(right2Center[0], maxRight2Center[0])
    # return max(maxLeft, maxRight, maxLeft2Center[0]+maxRight2Center[0])

# def calcCanges(prices):
#     changes = []
#     print(prices)
#     for i in range(len(prices)-1):
#         delta = round(prices[i+1] - prices[i], 3)
#         changes.append(delta)
#     return changes

def calcCanges(prices):
    changes = []
    day = 0
    for row in range(len(prices)-1):
        delta = round(prices[row + 1][0] - prices[row][0], 3)
        day += 1
        changes.append([delta, day])  # TODO will want to check on this date
    return changes



def find_stock(file, symbol):
    stock = file[file['symbol'] == symbol]
    # stock = stock[['date', 'close']]
    # stock = stock['close'].tolist()
    # TODO Revert this back. Only need to send one row through
    stock = stock.reset_index()[['close', 'date']].values.tolist()
    # Still want two rows coming out though
    stock = calcCanges(stock)

    sample = [stock[i][0] for i in range(len(stock))]
    # print(sample)
    # print(MSSDAC(sample))

    print(MSSDAC(stock))


def main():
    """Running the main code"""
    psa = pd.read_csv("prices-split-adjusted.csv")
    find_stock(psa, 'AAPL')


if __name__ == '__main__':
    main()