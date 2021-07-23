import sys
from math import inf as inf

# n is size of coins array (number of
# different coins)
def DPcoins(coins, amount):
    # minCoins[i] will be storing the minimum
    # number of coins required for i value.
    # So minCoins[amount] will have result
    n = len(coins)
    minCoins = [inf for _ in range(amount + 1)]
    traceBack = [inf for _ in range(amount + 1)]

    # Base case (If given value amount is 0)
    minCoins[0] = 0
    traceBack[0] = 0

    # Compute minimum coins required
    # for all values from 1 to amount
    for i in range(1, amount + 1):
        # Go through all coins smaller than i
        for j in range(n):
            print("\ni: ", i, "current coin", coins[j])
            if coins[j] <= i:
                traceBack[i] = minCoins[i - coins[j]]
                if traceBack[i] != inf and traceBack[i] + 1 < minCoins[i]:
                    minCoins[i] = traceBack[i] + 1
                    traceBack[i] = coins[j]
            print("minCoins", minCoins)
            print("traceBack", traceBack)

    if minCoins[amount] == inf:
        return -1

    print("\nfinal mincoins:", minCoins)
    print("final traceBack:", traceBack)
    return minCoins[amount]


# Driver Code
if __name__ == "__main__":
    coins = [1, 5, 10, 12, 25]
    n = len(coins)
    amount = 6
    print("Minimum coins required is ", DPcoins(coins, amount))