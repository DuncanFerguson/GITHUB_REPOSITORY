import sys
from math import inf as inf

# n is size of coins array (number of
# different coins)
# def DPcoins(coins, amount):
#     # minCoins[i] will be storing the minimum
#     # number of coins required for i value.
#     # So minCoins[amount] will have result
#     n = len(coins)
#     minCoins = [inf for _ in range(amount + 1)]
#     traceBack = [inf for _ in range(amount + 1)]
#
#     # Base case (If given value amount is 0)
#     minCoins[0] = 0
#     traceBack[0] = 0
#
#     # Compute minimum coins required
#     # for all values from 1 to amount
#     for i in range(1, amount + 1):
#         # Go through all coins smaller than i
#         for j in range(n):
#             print("\ni: ", i, "current coin", coins[j])
#             if coins[j] <= i:
#                 traceBack[i] = minCoins[i - coins[j]]
#                 if traceBack[i] != inf and traceBack[i] + 1 < minCoins[i]:
#                     minCoins[i] = traceBack[i] + 1
#                     traceBack[i] = coins[j]
#             print("minCoins", minCoins)
#             print("traceBack", traceBack)
#
#     if minCoins[amount] == inf:
#         return -1
#
#     print("\nfinal mincoins:", minCoins)
#     print("final traceBack:", traceBack)
#     return minCoins[amount]

# DP-CHANGE
# find number of coins needed to represent a value and memoize the last coin
def DP_CHANGE(denoms, value):
    num_coins = [0]*(value+1) # store number of coins needed to represent coin values from [0..value]
    last_coin = [float('Inf')]*(value+1) # memoize last coin used to represent coin values from [0..value]
    for d in denoms:
        num_coins[d] = 1
    for i in range(1, value + 1):
        num_denom = min([(num_coins[i-d] + 1, d) for d in denoms if i - d >= 0])
        num_coins[i], last_coin[i] = num_denom[0], num_denom[1]
    return num_coins, last_coin

# TRACE-CHANGE
# back-trace the denominations used
def TRACE_CHANGE(value, last_coin):
    denoms_used = []
    while value > 0:
        denoms_used.append(last_coin[value]);
        value -= last_coin[value]
    return denoms_used

def FIND_CHANGE(value, denoms):
    num_coins, last_coin = DP_CHANGE(denoms, value)
    print('number of coins needed to represent values ' + str(range(value+1)) + ': ' + str(num_coins))
    print('minimum number of coins need to represent the value ' + str(value) + ': ' + str(num_coins[value]))
    print('coins of denominations needed:' + str(TRACE_CHANGE(value, last_coin)))

FIND_CHANGE(6, [1, 5, 10, 12, 25])
# number of coins needed to represent values [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#                                            [0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2]
# minimum number of coins need to represent the value 10: 2
# coins of denominations needed:[5, 5]





# # Driver Code
# if __name__ == "__main__":
#     coins = [1, 5, 10, 12, 25]
#     n = len(coins)
#     amount = 6
#     print("Minimum coins required is ", DPcoins(coins, amount))