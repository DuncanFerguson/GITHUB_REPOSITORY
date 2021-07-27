# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4581
# Assignment: Lab 8
# Date 8/3/2021

# Chained Matrix Multiplication DP
import math


def parenStr():
    """This will return a string representation of the matrices with parentheses"""
    # TODO make this function recursive
    # TODO make sure to get the chain matrix working better
    traceback = []
    return traceback

def printMatrix(m):
    for row in m:
        print(row)

def chainMatrix(dims):
    # Create the empty 2-D table
    n = len(dims)-1
    m = [[None for i in range(n)] for j in range(n)]


    # Fill in the base case values zero diagonal
    for i in range(n):
        m[i][i] = 0  # Filling in the diagonal zero's

        # Fill in the rest of the table diagonal by diagonals
    # printMatrix(m)
    for chainLength in range(2, n+1):
        for i in range(n+1-chainLength):
            j = i + chainLength - 1
            # Fill in m[i][j] with the best of the recursive options
            m[i][j] = math.inf
            for k in range(i, j):
                # Two previous table values plus
                # what it cost to multiply the resulting matrices
                q = m[i][k] + m[k+1][j] + dims[i] * dims[k+1] * dims[j+1]
                if q < m[i][j]:
                    m[i][j] = q
    printMatrix(m)




def main():
    """Main Function to run the testing code"""
    dims = [30, 35, 15, 5, 10, 20, 25]
    print(chainMatrix(dims))


if __name__ == '__main__':
    main()
