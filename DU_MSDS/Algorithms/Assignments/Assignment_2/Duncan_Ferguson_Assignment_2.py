# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4581
# Assignment: Assignment 2
# Date 8/6/2021

# Use Divide Conquere
import math
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def graph_null(data):
    """ Just to give it a look"""
    sns.heatmap(data.isnull(), cbar=False, cmap='viridis')
    plt.title("Heatmap of the null values for all numeric columns")
    plt.tight_layout()
    plt.show()


# Divide and Conquer Algorithm
def MSSDAC(A, low=0, high=None):
    """DAC: Stock Price"""
    if high == None:
        high = len(A) - 1

    # Base Case
    if low == high:
        if A[low][0] > 0:
            return A[low]
        else:
            A[low][0] = 0
            return A[low]

    # Divide
    mid = (low+high)//2
    print(mid)

    # Conquer
    maxLeft = MSSDAC(A, low, mid)
    maxRight = MSSDAC(A, mid+1, high)

    # Combine
    maxLeft2Center = left2Center = 0
    for i in range(mid, low-1, -1):
        left2Center += A[i][0]
        maxLeft2Center = max(left2Center, maxLeft2Center)

    maxRight2Center = right2Center = 0
    for i in range(mid+1, high+1):
        right2Center += A[i][0]
        maxRight2Center = max(right2Center, maxRight2Center)
    return max(maxLeft, maxRight, maxLeft2Center+maxRight2Center)


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
    print("Final Return", MSSDAC(stock, low=0, high=None))


def main():
    """Running the main code"""
    psa = pd.read_csv("prices-split-adjusted.csv")
    # print(psa.head())
    # stock = psa['symbol'].unique()
    find_stock(psa, 'AAPL')


if __name__ == '__main__':
    main()

