
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
    print("\nInvestments list:\n", investments,"\n")
    f.close()
    return investments

def printMatrix(m):
        for row in m:



def optimizeInvestments(investments, amount):
    """This function takes the list of possible investments along with the amount of money available to spend
    This function returns both the optimal return on investment amount as well as the actual investments selected
    to achieve this optimal return, implement this function using dynamic programming"""



        optimalTable[0][c] = 0
        traceBack[0][c] = False

    # Fill in the table row by row
    # We need every potential entry in the previous fille in before
    for i in range(1, len(investments) +1):

        # printMatrix(optimalTable)

        # Fill in the ith row
        # Get the info about the ith investment
        name, cost, ereturn = investments[i-1]

        # fill in every possible amount of cash
        for c in range(cash+1):
            if cost > c:
            # if we don't have enough cash to buy this investment, then we just don't include it
                optimalTable[i][c] = optimalTable[i-1][c]
            traceBack[i][c] = false
        else:
        # If we have enough cash then we can either not include it or include it. We take the best of these two options
            #recall that if we include it we need to remove amount of cash and increase our expectedReturn
            if (optimalTable[i-1][c] > optimalTable[i-1][c-cost]):
                optimalTable[i][c] = optimalTable[i-1][c]
                traceback[i][c] = False

    printMatrix(optimalTable)
    printMatrix(traceback)

    results = []
    c = cash
    for i in range(len(investments), 0, -1):
        if traceback[i][c]:
            name, cost, ereturn = investments[i-1]
            results.append(investments[i-1])
            c -= cost



def main():
    """This function runs the main code"""
    file = 'zhvi-short.csv'
    # file = 'state_zhvi_summary_allhomes.csv'
    investments = loadZillow(file)
    print(investments)
    # investment_amount = 10

    # n = len(investments)
    # print(optimizeInvestments(investments, investment_amount))



if __name__ == '__main__':
    main()