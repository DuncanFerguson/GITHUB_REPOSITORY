# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4581
# Assignment: Assignment 3
# Date 8/23/2021

"""In this assignment, you will be using dynamic programming to select a set of investment options that maximize
your return on investment. you will be given a file of investment options along with the estimated return on
investment for eachone. You also have a given cash of money to invest. The specific file of investment options
you will be given will vary, but you will always have the following three pieces of information you can obtain from
 the file

 InvestmentName, InvestmentCost, EstimatedReturnOninvestment """


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
        investments.append([investmentLine[2].strip('"'), int(investmentLine[4]), int(investmentLine[4])*float(investmentLine[9])])
    print("\nInvestments list:\len(investments)", investments,"\len(investments)")
    f.close()
    return investments

def printMatrix(m):
    for row in m:
        print(row)


def optimizeInvestments(investments, cash):
    optimalTable = [[None for _ in range(cash + 1)] for _ in range(len(investments)+1)]
    traceback = [[None for _ in range(cash+1)] for _ in range(len(investments)+1)]

    # Build table optimalTable[][] in bottom up manner
    for i in range(len(investments) + 1):
        for c in range(cash + 1):
            if i == 0 or c == 0:
                optimalTable[i][c] = 0
                traceback[i][c] = False
            elif investments[i - 1][1] <= c:
                optimalTable[i][c] = max(investments[i - 1][2] + optimalTable[i - 1][c - investments[i - 1][1]],
                                         optimalTable[i - 1][c])
                # Adjusting my traceback table to coincide with the max
                if optimalTable[i][c] == investments[i - 1][2] + optimalTable[i - 1][c - investments[i - 1][1]]:
                    traceback[i][c] = True
                elif optimalTable[i][c] == optimalTable[i - 1][c]:
                    traceback[i][c] = False
            else:
                optimalTable[i][c] = optimalTable[i - 1][c]
                traceback[i][c] = False

    # Uncomment below when looking at the short copy only
    # print("\nOptimal Finished\n")
    # printMatrix(optimalTable)
    # print("\nTracback Finished")
    # printMatrix(traceback)

    results = []
    c = cash
    for i in range(len(investments), 0, -1):
        if traceback[i][c]:
            name, cost, ereturn = investments[i-1]
            results.append(investments[i-1][0])
            c -= cost
    return optimalTable[len(investments)][cash], results


def main():
    """This function runs the main code"""
    # file = 'zhvi-short.csv'
    file = 'state_zhvi_summary_allhomes.csv'
    # investment_amount = 15
    investment_amount = 1000000
    investments = loadZillow(file)

    ereturn, picked = optimizeInvestments(investments, investment_amount)
    print('\nereturn:\n', ereturn)
    print('\npicked:\n', picked)


if __name__ == '__main__':
    main()