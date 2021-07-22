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

"""https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-s095-programming-for-the-puzzled-january-iap-2018/puzzle-11-memory-serves-you-well/MIT6_S095IAP18_Puzzle_11.pdf"""
""""https://www.programmersought.com/article/90697579491/"""

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


def count_no_of_ways(coins, n):
    """Number of ways"""
    # TODO Testing CODE
    table = [0 for _ in range(n+1)]
    table[0] = 1
    for coin in coins:
        for i in range(coin, n+1):
            table[i] += table[i-coin]
            # print(table)  # Nice Print to see the table
    return table[n]




# Algorithm 2: Dynamic Programming with Traceback
def DPcoins(coins, amount):
    """Dynamic Programming with Traceback"""
    # Create the initial tables
    minCoins = [inf for _ in range(amount+1)]
    traceBack = [inf for _ in range(amount+1)]

    # Setting the first values to zero
    minCoins[0] = 0
    traceBack[0] = 0

    print('initial minCoins:', minCoins)
    print('initial traceBack:', traceBack)

    # i is going to loop from 1 to the amount of change
    # currentcoin is going to iterate through all the coin values [1, 5, 10, 12, 25]
    # when assigning to mincoin, make sure the current value is >= mincoins[i].
    # Don't overwrite mincoins with a higher value

    # TODO Change up
    # for i in range(1, len(coins)+1):
    #     for r in range(1, amount+1):
    #         # print(r)
    #         if coins[i-1] == r:
    #             minCoins[i] = 1
    #             print(minCoins)
    #         elif coins[i-1] > r:
    #             minCoins[i] = minCoins[i-r]
    #             print(minCoins)
    #         #     print("minCoins: ", minCoins)
    #         #     print("traceBack: ", traceBack)

    #         # if i >= currentCoin:
    #         #     minCoins[i] = minCoins[i - currentCoin] + 1
    #         #     print("2 minCoins: ", minCoins)
    #         #     traceBack[i] = currentCoin
    #         #     print("2 traceBack: ", traceBack)
    #         # else:
    #         #     traceBack[i] = traceBack[i]
    #         #     print("3 minCoins: ", minCoins)
    #         #     print("3 traceBack: ", traceBack)
    # print("\nfinal tracback: ", traceBack)
    # print("final minCoins: ", minCoins)

    # # Switch Up
    for i in range(1, amount+1):
        for currentCoin in enumerate(coins):
            print("\ni: ", i, "Current Coin", currentCoin[1])
            if i == coins[currentCoin[0]]:
                minCoins[i] = minCoins[i - currentCoin[1]] + 1
                traceBack[i] = currentCoin[1]
                # print('If')
                # print("minCoins2: ", minCoins)
                # print("traceBack2: ", traceBack)
            elif i > coins[currentCoin[0]]:
                minCoins[i] = minCoins[i - currentCoin[1]] + 1
                traceBack[i] = 1
                # print("elif")
                # print("minCoins2: ", minCoins)
                # print("traceBack2: ", traceBack)
            else:
                traceBack[i] = traceBack[i]
                # print("Else")
                # print("minCoins3: ", minCoins)
                # print("traceBack3: ", traceBack)
            print("minCoins: ", minCoins)
            print("traceBack: ", traceBack)

    print("\nfinal tracback: ", traceBack)
    print("final minCoins: ", minCoins)



    # # TODO This is close
    # for i in range(1, amount+1):
    #     for currentCoin in coins:
    #         print("i: ", i, "Current Coin", currentCoin)
    #         if i >= currentCoin:
    #             minCoins[i] = minCoins[i - currentCoin] + 1
    #             print("2 minCoins: ", minCoins)
    #             traceBack[i] = currentCoin
    #             print("2 traceBack: ", traceBack)
    #         else:
    #             traceBack[i] = traceBack[i]
    #             print("3 minCoins: ", minCoins)
    #             print("3 traceBack: ", traceBack)
    # print("\nfinal tracback: ", traceBack)
    # print("final minCoins: ", minCoins)


    return -1  # return optimal number of coins



def main():
    """Main Program To run the testing.txt code?"""
    C = [1, 5, 10, 12, 25] # coin denominations (must include a penny)
    # A = int(input('Enter desired amount of change: '))
    A = 6
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