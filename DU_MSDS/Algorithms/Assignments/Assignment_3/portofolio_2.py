
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
    optimalTable = [[None for _ in range(cash + 1)] for _ in range(len(investments)+1)]
    traceback = [[None for _ in range(cash+1)] for _ in range(len(investments)+1)]
    # print(len(investments))
    #
    # print("\nOptimal Start\n")
    # printMatrix(optimalTable)
    # print("\nTracback Start\n")
    # printMatrix(traceback)

    # for c in range(cash+1):
    #     optimalTable[0][c] = 0
    #     traceback[0][c] = False

    # Build table optimalTable[][] in bottom up manner
    for i in range(len(investments) + 1):
        # name, cost, ereturn = investments[i - 1]
        for w in range(cash + 1):
            if i == 0 or w == 0:
                optimalTable[i][w] = 0
                traceback[i][w] = False
            elif investments[i - 1][1] <= w:
                optimalTable[i][w] = max(investments[i - 1][2] + optimalTable[i - 1][w - investments[i - 1][1]],
                                         optimalTable[i - 1][w])
                traceback[i][w] = True
                if optimalTable[i][w] == investments[i - 1][2] + optimalTable[i - 1][w - investments[i - 1][1]]:
                    print("Here")
                elif optimalTable[i][w] == optimalTable[i - 1][w]:
                    print(investments[i-1][0])

            else:
                optimalTable[i][w] = optimalTable[i - 1][w]
                traceback[i][w] = False

    print("\nOptimal Start\n")
    printMatrix(optimalTable)
    print("\nTracback Start\n")
    printMatrix(traceback)

    return optimalTable[len(investments)][cash]


def main():
    """This function runs the main code"""
    file = 'zhvi-short.csv'
    # file = 'state_zhvi_summary_allhomes.csv'
    investments = loadZillow(file)
    # print(investments)
    investment_amount = 15
    # investment_amount = 1000000

    # len(investments) = len(investments)
    print(optimizeInvestments(investments, investment_amount))
    # print('\n\nerturn:\n', ereturn)
    # print('\n\npicked:\n', picked)


if __name__ == '__main__':
    main()