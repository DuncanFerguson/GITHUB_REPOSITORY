import sys
import math

def printMatrix(m):
    for row in m:
        print(row)

# Function to find the most efficient way to multiply
# a given sequence of matrices
def DP_MC(p):
    n = len(dims)-1
    m = [[None for i in range(n)] for j in range(n)]

    # Placing the diagonals
    for i in range(len(p)-1):
        m[i][i] = 0
    printMatrix(m)
    for chainLength in range(2, len(p)-1):
        for i in range(len(p)-chainLength):
            j = i + chainLength - 1
            m[i][j] = math.inf
            for k in range(i, j):
                q = m[i][k] + m[k+1][j]+p[i]*p[k+1]*p[j+1]
                print(q)
                if q < m[i][j]:
                    m[i][j] = q

    printMatrix(m)
    return m[0][len(p)-2]

if __name__ == '__main__':
    # Matrix `M[i]` has dimension `dims[i-1] × dims[i]` for `i = 1…n`
    # input is `10 × 30` matrix, `30 × 5` matrix, `5 × 60` matrix
    # dims = [10, 30, 5, 60]
    dims = [30, 35, 15, 5, 10, 20, 25]

    print("The minimum cost is", DP_MC(dims))


