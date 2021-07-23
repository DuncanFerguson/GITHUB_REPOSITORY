import sys

import os, sys

def solve_coin_change(coins, value):
    """A dynamic solution to the coin change problem"""

    table = [None for x in range(value + 1)]
    print(table)
    table[0] = [0]
    for i in range(1, value + 1):
        for coin in coins:
            if coin > i:
                continue
            elif not table[i] or len(table[i - coin]) + 1 < len(table[i]):
                if table[i - coin] != None:
                    print(table[i - coin][:])
                    table[i] = table[i - coin][:]
                    table[i].append(coin)
                    # print(table)

    if table[-1] != None:
        print('%d coins: %s' % (len(table[-1]), table[-1]))
    else:
        print('No solution possible')


if __name__ == '__main__':

    # Modify this to alter the denominations of coins
    coins = [1, 5, 10, 12, 25]
    solve_coin_change(coins, 29)


# TODO SHort REcursive solution
# def minimum_coins(coin_list, change):
#     min_coins = change
#     if change in coin_list:
#         return 1, [change]
#     else:
#         cl = []
#         for coin in coin_list:
#             if coin < change:
#                 mt, t = minimum_coins(coin_list, change - coin)
#                 num_coins = 1 + mt
#                 if num_coins < min_coins:
#                     min_coins = num_coins
#                     cl = t + [coin]
#     return min_coins, cl
#
# change = 29
# coin_list = [1, 5, 10, 12, 25]
# min, c = minimum_coins(coin_list, change)
# #print("You need 3 1's, 1 10's, 0 15's, 3 20's") <- I want to implement this option.
# print("Total number of coins required is %s." % min, c) #7


# TODO bad example
# MAX = 100000
#
# # dp array to memoize the results
# dp = [-1] * (MAX + 1)
#
# # List to store the result
# denomination = []
#
#
# # Function to find the minimum number of
# # coins to make the sum equals to X
# def countMinCoins(n, C, m):
#     # Base case
#     if (n == 0):
#         dp[0] = 0
#         return 0
#
#     # If previously computed
#     # subproblem occurred
#     if (dp[n] != -1):
#         return dp[n]
#
#     # Initialize result
#     ret = sys.maxsize
#
#     # Try every coin that has smaller
#     # value than n
#     for i in range(m):
#         if (C[i] <= n):
#             x = countMinCoins(n - C[i], C, m)
#
#             # Check for INT_MAX to avoid
#             # overflow and see if result
#             # . an be minimized
#             if (x != sys.maxsize):
#                 ret = min(ret, 1 + x)
#
#     # Memoizing value of current state
#     dp[n] = ret
#     return ret
#
#
# # Function to find the possible
# # combination of coins to make
# # the sum equal to X
# def findSolution(n, C, m):
#     # Base Case
#     if (n == 0):
#
#         # Print Solutions
#         for it in denomination:
#             print(it, end=" ")
#
#         return
#
#     for i in range(m):
#
#         # Try every coin that has
#         # value smaller than n
#         if (n - C[i] >= 0 and dp[n - C[i]] + 1 == dp[n]):
#             # Add current denominations
#             denomination.append(C[i])
#             # Backtrack
#             findSolution(n - C[i], C, m)
#             break
#
#
# # Function to find the minimum
# # combinations of coins for value X
# def countMinCoinsUtil(X, C, N):
#     # Initialize dp with -1
#     # memset(dp, -1, sizeof(dp))
#
#     # Min coins
#     isPossible = countMinCoins(X, C, N)
#
#     # If no solution exists
#     if (isPossible == sys.maxsize):
#         print("-1")
#
#     # Backtrack to find the solution
#     else:
#         findSolution(X, C, N)
#
#
# # Driver code
# if __name__ == '__main__':
#     X = 29
#
#     # Set of possible denominations
#     arr = [1, 5, 10, 12, 25]
#
#     N = len(arr)
#
#     # Function call
#     countMinCoinsUtil(X, arr, N)


# TODO perfection below

# coins = [1, 5, 10, 12, 25]
# d = {} # stores tuples of the form (# of coins, [coin list])
#
#
# def m(cents):
#     if cents in d.keys():
#         return d[cents]
#     elif cents > 0:
#         choices = [(m(cents - x)[0] + 1, m(cents - x)[1] + [x]) for x in coins if cents >= x]
#         print(choices)
#
#         # given a list of tuples, python's min function
#         # uses the first element of each tuple for comparison
#         d[cents] = min(choices)
#         return d[cents]
#     else:
#         d[0] = (0, [])
#         return d[0]
#
# for x in range(1, 30):
#     val = m(x)
#     print(x, "cents requires", val[0], "coins:", val[1])

