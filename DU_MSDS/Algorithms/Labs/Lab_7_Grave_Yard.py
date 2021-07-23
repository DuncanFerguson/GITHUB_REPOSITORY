       #

        #     minCoins[i] = min(minCoins[coins[j-1]], minCoins[i - coins[j]])

            # else:
                # minCoins[i] = minCoins[i - coins[j]] + 1
            # if i - coins[j] >= 0:
            #     print("yes")
            #     minCoins[i] = minCoins[i-coins[j]]+1
            #     traceBack[i] = 1

    # if i >= coin:
    #     minCoins[i] += minCoins[i - ]
    #
    # if amount in coins:
    #     return 1
    # for i in range(1, amount+1):
    #     for curCoin in coins:
    #         print("\ni: ", i, "current coin", curCoin)


            # if amount >= minCoins[i]:
            #     print("yes")
                # minCoins[i] = minCoins[i-coins[j-1]]+1
                # minCoins[i] = coins[j-1]
            # minCoins[i] = minCoins[i - coins[j-1]] + 1

    print("\nfinal mincoins:", minCoins)
    print("final traceBack:", traceBack)



    # for i in range(1, amount+1):
    #     for j in range(len(coins)+1):
    #         print("\ni: ", i, "current coin", coins[j-1])
    #         if coins[j-1] <= i:
    #             print("yes")
    #             if coins[j-1] == i:
    #                 minCoins[i] = minCoins[i-coins[j-1]]+1
    #                 traceBack[i] = 1
    #
    #
    #         # traceBack[i] = minCoins[i - coins[j]]
    #         print("minCoins", minCoins)
    #         print("traceBack", traceBack)
    #
    # print("\nfinal mincoins:", minCoins)
    # print("final traceBack:", traceBack)



# TODO This was good?
    # for i in range(1, amount + 1):
    #     # Go through all coins smaller than i
    #     for j in range(len(coins)):
    #         print("\ni: ", i, "current coin", coins[j])
    #         if coins[j] <= i:
    #             traceBack[i] = minCoins[i - coins[j]]
    #             if traceBack[i] + 1 < minCoins[i]:
    #                 minCoins[i] = minCoins[i-coins[j]] + 1
    #                 traceBack[i] = min(coins[j], 1 + traceBack[i-coins[j]])
    #                 # traceBack[i] = min(coins[j-1], traceBack[j-1]+1)
    #             # else:
    #             #     print("INNER Continue")
    #             #     # TODO this is where the code needs to be written better
    #                 # traceBack[i] = min(coins[j-1], coins[j])
    #             traceBack[i] = traceBack[i]

            # elif coins[j] > i:
            #     print("Continuing through")

    #         print("minCoins", minCoins)
    #         print("traceBack", traceBack)
    #
    # print("\nfinal mincoins:", minCoins)
    # print("final traceBack:", traceBack)
    #
    # change = []
    # for i in traceBack[::-1]:
    #     if sum(change) + i <= amount:
    #         change.append(i)
    #
    # print(change)


    # return minCoins[amount]


    # TODO CODE BELOW DOESNT QUITE GET IT

    # print('initial minCoins:', minCoins)
    # print('initial traceBack:', traceBack)

    # i is going to loop from 1 to the amount of change
    # currentcoin is going to iterate through all the coin values [1, 5, 10, 12, 25]
    # when assigning to mincoin, make sure the current value is >= mincoins[i].
    # Don't overwrite mincoins with a higher value

    # TODO don't mess with this
    # for i in range(1, amount+1):
    #     for currentCoin in enumerate(coins):
    #         print("\ni: ", i, "Current Coin", currentCoin[1])
    #         if i == coins[currentCoin[0]]:
    #             print("IF Statement")
    #             minCoins[i] = minCoins[i - currentCoin[1]] + 1
    #             traceBack[i] = currentCoin[1]
    #         elif i > coins[currentCoin[0]]:
    #             print("Elif Statment")
    #             minCoins[i] = minCoins[i - currentCoin[1]] + 1
    #             traceBack[i] = 1
    #         else:
    #             print("Else Statment")
    #             traceBack[i] = min(traceBack[i], currentCoin[1])
    #         print("minCoins: ", minCoins)
    #         print("traceBack: ", traceBack)
    #
    # print("\nfinal tracback: ", traceBack)
    # print("final minCoins: ", minCoins)

    # print("\nfinal tracback: ", traceBack)
    # print("final minCoins: ", minCoins)
    #
    # return minCoins[-1]  # return optimal number of coins
