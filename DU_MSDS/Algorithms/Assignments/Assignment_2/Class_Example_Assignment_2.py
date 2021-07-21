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
    sns.heatmap(data.isnull(), cbar=False, cmap='viridis')
    plt.title("Heatmap of the null values for all numeric columns")
    plt.tight_layout()
    plt.show()

# Week Four Slides
def MSS1(A):
    best = 0
    n = len(A)
    for i in range(n):
        for j in range(i, n):
            sum = 0
            for k in range(i, j+1):
                sum = sum +A[k]
            if sum > best:
                best = sum
    return best

# Second Algorithm. Faster
def MMS2(A):
    best, ffrom, to = 0, 0, -1
    n = len(A)
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum = sum + A[j]
            if sum > best:
                best, ffrom, to = sum, i, j
    return best

# Divide and Conquer Algorithm
def MSSDAC(A, low=0, high=None):
    # A is the price change between the day and the previous dat
    # They are passing in the change of prices
    # print(A)
    # print(max(A['close'])-min(A['close']))
    # if high == None:
    #     high =
    if high == None:
        high = len(A) - 1
    # Base Case
    if low == high:
        if A[low] > 0:
            return A[low]
        else:
            return 0

    # Divide
    mid = (low+high)//2

    # Conquer
    maxLeft = MSSDAC(A, low, mid)
    maxRight = MSSDAC(A, mid+1, high)

    # Combine
    maxLeft2Center = left2Center = 0
    for i in range(mid, low-1, -1):
        left2Center += A[i]
        maxLeft2Center = max(left2Center, maxLeft2Center)
    maxRight2Center = right2Center = 0
    for i in range(mid+1, high+1):
        right2Center += A[i]
        maxRight2Center = max(right2Center, maxRight2Center)
    return max(maxLeft, maxRight, maxLeft2Center+maxRight2Center)

def calcCanges(prices):
    changes = []
    for i in range(len(prices)-1):
        delta = round(prices[i+1] - prices[i], 3)
        changes.append(delta)
    return changes


def find_stock(file, symbol):
    stock = file[file['symbol'] == symbol]
    stock = stock[['date', 'close']]
    stock = stock['close'].tolist()
    stock = calcCanges(stock)
    print(MSSDAC(stock, low=0, high=None))


def main():
    """Running the main code"""
    psa = pd.read_csv("prices-split-adjusted.csv")
    find_stock(psa, 'AAPL')


if __name__ == '__main__':
    main()