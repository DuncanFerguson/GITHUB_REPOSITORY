
def loadZillow(filename):
    investments = [] # [name(2), cost(4), return([4] * [9])]  # investments[2] list is the cost times the estimated return
    f = open(filename, "r")
    # Skip the first line since it is header info and USA info
    f.readline()
    f.readline()
    for investmentLine in f:
        investmentLine = investmentLine.split(",")
        # investments is a list of lists.  Each sublist is name, initial cost, and estimated 10 year return
        print(investmentLine[2], investmentLine[4], investmentLine[9])
        investments.append([investmentLine[2], int(investmentLine[4]), int(investmentLine[4])*float(investmentLine[9])])
    print("\nInvestments list:\len(investments)", investments,"\len(investments)")
    f.close()
    return investments

def printMatrix(m):
    for row in m:
        print(row)


def optimizeInvestments(investments, cash):
    optimizeTable = [0 for i in range(cash + 1)]  # Making the optimizeTable array
    traceback = [0 for i in range(cash + 1)]

    for i in range(1, len(investments) + 1):  # taking first i elements
        for w in range(cash, 0, -1):  # starting from back,so that we also have data of
            # previous computation when taking i-1 items
            if investments[i - 1][1] <= w:
                # finding the maximum value
                optimizeTable[w] = max(optimizeTable[w], optimizeTable[w - investments[i - 1][1]] + investments[i - 1][2])

    return optimizeTable[cash]  # returning the maximum value of knapsack


def main():
    """This function runs the main code"""
    file = 'zhvi-short.csv'
    # file = 'state_zhvi_summary_allhomes.csv'
    investments = loadZillow(file)
    # print(investments)
    investment_amount = 15

    # len(investments) = len(investments)
    print(optimizeInvestments(investments, investment_amount))
    # print('\n\nerturn:\n', ereturn)
    # print('\n\npicked:\n', picked)


if __name__ == '__main__':
    main()