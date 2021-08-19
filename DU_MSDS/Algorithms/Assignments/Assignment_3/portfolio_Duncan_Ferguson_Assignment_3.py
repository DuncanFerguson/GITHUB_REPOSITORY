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

# TODO multiples of 1k dollars

import pandas as pd

# Load in the investment data from State_Zhvi_Summary_AllHomes.csv

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
    """This function takes the list of possible investments along with the cash of money available to spend
    This function returns both the optimal return on investment cash as well as the actual investments selected
    to achieve this optimal return, implement this function using dynamic programming
    """

    # Setting up the tables
    optimalTable = [[None for _ in range(cash + 1)] for _ in range(len(investments)+1)]
    traceback = [[None for _ in range(cash+1)] for _ in range(len(investments)+1)]
    for c in range(cash+1):
        optimalTable[0][c] = 0
        traceback[0][c] = False

    print("\noptimal table Start:\n")
    printMatrix(optimalTable)
    print("\ntraceback table Start:\n")
    printMatrix(traceback)

    for i in range(1, len(investments) + 1):

        name, cost, ereturn = investments[i-1]

        for c in range(cash + 1):

            if cost > c:
                optimalTable[i][c] = optimalTable[i-1][c]
                # optimalTable[i][c] = investments[i][2]
                traceback[i][c] = False
            else:
                # TODO Line below needs editing
                # print("Opt here", optimalTable[i-1])
                # If we have enough cash then we can either not include it or include it
                # We take the best of these two options
                # Recall that if we include it we need to remove cash of cash and increase our expectedReturn
                if (optimalTable[i-1][c] > optimalTable[i-1][c-cost]):
                    print("Here")
                    optimalTable[i][c] = optimalTable[i-1][c]
                    traceback[i][c] = False
                else:
                    # optimalTable[i][c] = investments[i][2]
                    optimalTable[i][c] = optimalTable[i-1][c-cost]
                    traceback[i][c] = True
                    print("\noptimal table Update:\n")
                    printMatrix(optimalTable)

    print("\noptimal table:\n")
    printMatrix(optimalTable)
    print("\ntraceback table:\n")
    printMatrix(traceback)

    results = []
    c = cash
    for i in range(len(investments), 0, -1):
        if traceback[i][c]:
            name, cost, ereturn = investments[i-1]
            results.append(investments[i-1][0])
            c -= cost

    return optimalTable[len(investments)][c], results



def main():
    """This function runs the main code"""
    file = 'zhvi-short.csv'
    # file = 'state_zhvi_summary_allhomes.csv'
    investments = loadZillow(file)
    # print(investments)
    investment_amount = 15

    # len(investments) = len(investments)
    ereturn, picked = optimizeInvestments(investments, investment_amount)
    print('\n\nerturn:\n', ereturn)
    print('\n\npicked:\n', picked)


if __name__ == '__main__':
    main()