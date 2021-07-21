



n = 6
coins = [1, 5, 10, 12, 25]

def count_no_of_ways(coins, n):
    """Number of ways"""
    table = [0 for _ in range(n+1)]
    table[0] = 1
    for coin in coins:
        for i in range(coin, n+1):
            table[i] += table[i-coin]
            print(table)
    return table[n]

print(count_no_of_ways(coins, n))


# Algorithm 2: Dynamic Programming with Traceback
# def DPcoins(coins, amount):
#     # Fill in the base case(s)
#     if amount == 0: # A Base Case
#         return 0
#     else:
#         # TODO Create the initial tables
#         table = [[0 for t in range(amount+1)] for t in range(len(coins)+1)]
#         for i in range(amount+1):
#             table[0][i] = i
#         print(table)
#         return table

# TODO watch the youtube vid
#
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

