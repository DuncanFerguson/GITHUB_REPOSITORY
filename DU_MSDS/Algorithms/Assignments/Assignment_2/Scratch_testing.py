import pandas as pd

def MSSDAC(arr, lhs=0, rhs=None):
    # If the array has just one element, we return that the profit is zero
    # but the minimum and maximum values are just that array value.
    if rhs == None:
        rhs = len(arr)-1
        print(rhs)

    if lhs == rhs:
        return (0, arr[lhs], arr[rhs])

    # Recursively compute the values for the first and latter half of the
    # array.  To do this, we need to split the array in half.  The line
    # below accomplishes this in a way that, if ported to other languages,
    # cannot result in an integer overflow.
    mid = lhs + (rhs - lhs) / 2

    # Perform the recursion.
    (leftProfit, leftMin, leftMax) = MSSDAC(arr, lhs, mid)
    (rightProfit, rightMin, rightMax) = MSSDAC(arr, mid + 1, rhs)

    # Our result is the maximum possible profit, the minimum of the two
    # minima we've found (since the minimum of these two values gives the
    # minimum of the overall array), and the maximum of the two maxima.
    maxProfit = max(leftProfit, rightProfit, rightMax - leftMin)
    return (maxProfit, min(leftMin, rightMin), max(leftMax, rightMax))

def calcCanges(prices):
    """This Function calculates the daily gains or losses.
    It is also adding a day index."""
    changes = [round(prices[row + 1][0] - prices[row][0], 3) for row in range(len(prices)-1)]
    # changes = []
    # for row in range(len(prices)-1):
        # delta = round(prices[row + 1][0] - prices[row][0], 3)
        # changes.append(delta)
    return changes


def find_stock(file, symbol):
    stock = file[file['symbol'] == symbol]
    stock = stock.reset_index()[['close', 'date']].values.tolist()

    # This is to pull down the sheet so that it can be looked at
    # my_df = pd.DataFrame(stock)
    # my_df.to_csv('AAPL.csv', index=False, header=False)  # For Saving the data an looking at

    # Still want two rows coming out though
    stock2 = calcCanges(stock)

    maxProfit, maxLow, maxHigh = MSSDAC(stock2)
    # print("Final Hit", maxProfit, maxLow, maxHigh)
    # Converting into dates
    maxLow = stock[maxLow][1]
    maxHigh = stock[maxHigh][1]

    return maxProfit, maxLow, maxHigh


def main():
    """Running the main code"""
    psa = pd.read_csv("prices-split-adjusted.csv")
    # psa = pd.read_csv("prices-split-adjusted_short_shorts.csv")
    # https://www.roelpeters.be/solved-dtypewarning-columns-have-mixed-types-specify-dtype-option-on-import-or-set-low-memory-in-pandas/
    # psa = pd.read_csv("prices-split-adjusted_v2.csv")
    tickers = psa['symbol'].unique()
    # tickers = ["MMM", "ABT", "ATVI", "AAPL", "PCLN"]
    # tickers = ["MMM", "ABT", "ATVI", "AAPL"]
    # tickers = ["AAPL"]
    # tickers = ["WLTW"]

    bestProfit = 0

    for ticker in tickers:
        profit, buyDate, sellDate = find_stock(psa, ticker)
        if profit > bestProfit:
            bestName = ticker
            bestProfit = profit
            bestBuyDate = buyDate
            bestSellDate = sellDate


    sfile = pd.read_csv("securities.csv")

    # print(sfile.columns)

    add_info = sfile[sfile['Ticker symbol'] == bestName]
    print("Best stock to buy:", add_info["Security"].values[0], " on ", bestBuyDate, "\n and sell on ", bestSellDate,
          " with a profit of ", bestProfit)


if __name__ == '__main__':
    main()