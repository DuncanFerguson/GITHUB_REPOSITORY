
def num_coins():
    coins = [25, 10, 5, 1]
    # coins = [1, 5, 10, 12, 25]
    amount = 32
    count = 0
    for coin in coins:
        while amount >= coin:
            amount = amount - coin
            count += 1
    return count

# print(num_coins())

def _change_matrix(coin_set, change_amount):
    matrix = [[0 for m in range(change_amount+1)] for m in range(len(coin_set)+ 1)]
    for i in range(change_amount+1):
        matrix[0][i] = i
    return matrix

def change_making(coins, change):
    matrix = _change_matrix(coins, change)
    for c in range(1, len(coins) + 1):
        for r in range(1, change + 1):
            if coins[c-1] == r:
                matrix[c][r] = 1
            elif coins[c-1] > r:
                matrix[c][r] = matrix[c-1][r]
            else:
                matrix[c][r] = min(matrix[c-1][r], 1+matrix[c][r - coins[c-1]])
    print(matrix)
    return matrix[-1][-1]



# coins = [25, 10, 5, 1]
coins = [1, 5, 10, 12, 25]
amount = 6
# amount = 2

print(change_making(coins, amount))