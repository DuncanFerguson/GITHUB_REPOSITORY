# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4581
# Assignment: Lab 5
# Date 7/13/2021

# Below are two algorithms (DAC and DP) to compute the
# minimum number of coins required to produce A cents worth of change
# The DP version also prints out the coins needed to produce this min
from time import time
from math import inf as inf

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
                # print(currentMin)
            # Keep the best
                minCoins = min(minCoins, currentMin)
        return minCoins


# Algorithm 2: Dynamic Programming with Traceback
def DPcoins(coins, amount):
    """Dynamic Programming with Traceback"""
    minCoins = [inf for _ in range(amount+1)]
    traceBack = [inf for _ in range(amount+1)]

    # # Base Case Setting the first values to zero
    minCoins[0] = 0
    traceBack[0] = 0


    for i in range(1, amount+1):
        for j in range(1, len(coins)+1):
            print("i: ", i, "currentcoin", coins[j-1])
            if i >= coins[j-1]:
                numCoins = minCoins[i-coins[j-1]]+1
                if numCoins < minCoins[i]:
                    minCoins[i] = numCoins
                    traceBack[i] = coins[j -1]


            print("minCoins", minCoins)
            print("traceBack", traceBack)


def main():
    """Main Program To run the testing.txt code?"""
    C = [1, 5, 10, 12, 25] # coin denominations (must include a penny)
    # C = [1, 2, 3]


    # A = int(input('Enter desired amount of change: '))
    A = 29
    assert A >= 0
    # print("DAC:")
    # t1 = time()
    # numCoins = DACcoins(C, A)
    # t2 = time()
    # print("optimal:", numCoins, " in time: ", round((t2-t1)*1000, 1), "ms")

    # # TODO Testing Code
    # print("count_number_of_ways: ")
    # t3 = time()
    # numCoins2 = count_no_of_ways(C, A)
    # t4 = time()
    # print("optimal:", numCoins2, " in time: ", round((t4-t3)*1000, 1), "ms")

    # TODO THis is testing of the dynamic programing with Traceback
    print("DP:")
    t1 = time()
    numCoins = DPcoins(C, A)
    t2 = time()
    print("optimal:", numCoins, " in time: ", round((t2-t1)*1000, 1), "ms")


if __name__ == '__main__':
    main()