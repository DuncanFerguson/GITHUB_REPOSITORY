# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4581
# Assignment: Lab 5
# Date 7/13/2021

# Below are two algorithms (DAC and DP) to compute the
# minimum number of coins required to produce A cents worth of change
# The DP version also prints out the coins needed to produce this min
from time import time

# Algorithm 1: Divide-and-Conquer
def DACcoins(coins, amount):
    if amount == 0: # The base case
        return 0
    else: # The recursive case
        minCoins = float("inf")
        for currentCoin in coins: # Check all coins
        # If we can give change
            if (amount - currentCoin) >= 0:
            # Calculate the optimal for currentCoin
                currentMin = DACcoins(coins, amount-currentCoin) + 1
            # Keep the best
                minCoins = min(minCoins, currentMin)
                return minCoins

# Algorithm 2: Dynamic Programming with Traceback
def DPcoins(coins, amount):
    # Fill in the base case(s)
    if amount == 0: # A Base Case
        return 0
    else:
        # TODO Create the initial tables
        table = [[0 for t in range(amount+1)] for t in range(len(coins)+1)]
        for i in range(amount+1):
            table[0][i] = i
        print(table)
        return table

# TODO watch the youtube vid
# https://www.youtube.com/watch?v=CVq7puhdlFA
# def change_making(coins, change):
#     matrix = DPcoins(coins, change)
#     for c in range(1, len(coins) + 1):
#         for r in range(1+change+1):
#             if coins[c-1] == r:
#                 matrix[c][r] = 1
#             elif coins[c-1] > r:
#                 matrix[c][r] = matrix[c-1][r]
#             else:
#                 matrix[c][r] = min(matrix[c - 1][r], 1+matrix[c][r - coins[c-1]])
#     return matrix[-1][-1]

    # if amount == 0: # The base case
    #     return 0
    # else: # The recursive Case



    # TODO Fill in the rest of the table
    # TODO Perform the traceback to print result

    # return -1 # return optimal number of coins

def main():
    """Main Program To run the testing.txt code?"""
    C = [1, 5, 10, 12, 25] # coin denominations (must include a penny)
    A = int(input('Enter desired amount of change: '))
    assert A>=0
    # print("DAC:")
    # t1 = time()
    # numCoins = DACcoins(C,A)
    # t2 = time()
    # print("optimal:", numCoins, " in time: ", round((t2-t1)*1000, 1), "ms")
    # print()
    # print("DP:")
    t1 = time()
    numCoins = DPcoins(C, A)
    t2 = time()
    print("optimal:", numCoins, " in time: ", round((t2-t1)*1000, 1), "ms")

if __name__ == '__main__':
    main()