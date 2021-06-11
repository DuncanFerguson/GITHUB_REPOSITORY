def printMatrix(m):
    for row in m:
        print(row)


def matrixMult(A, B):
    """ This functin multiplies two matrix's"""
    # Setting up Blank Matrix for 3x3
    C = [[0 for i in range(3)] for j in range(3)]

    print("Matrix A Dimensions = ", len(A), "x", len(A[0]))
    print("Matrix B Dimensions = ", len(B), "x", len(B[0]))

    for i in range(len(A)):  # Looping through Matrix A Rows
        for j in range(len(B[0])):  # Iterating through Matrix A Rows
            for k in range(len(B)):  # Going Through Matrix B Columns
                C[i][j] += A[i][k]*B[k][j]  # Summing up index positions

    return C

# Testing code
# Test1
A = [[ 2, -3, 3],
     [-2, 6, 5],
     [ 4, 7, 8]]
B = [[-1, 9, 1],
     [ 0, 6, 5],
     [ 3, 4, 7]]

C = matrixMult(A, B)

if not C == None:
    printMatrix(C)


# TODO Get test two working
# Test2
# A = [[ 2, -3, 3, 0],
#     [-2, 6, 5, 1],
#     [ 4, 7, 8, 2]]
# B = [[-1, 9, 1],
#     [ 0, 6, 5],
#     [ 3, 4, 7]]
#
#
# C = matrixMult(A, B)
#
# if not C == None:
#     printMatrix(C)

# TODO Get Test Three Working
# # Test3
A = [[ 2, -3, 3, 5],
    [-2, 6, 5, -2]]

B = [[-1, 9, 1],
    [ 0, 6, 5],
    [ 3, 4, 7],
    [ 1, 2, 3]]
C = matrixMult(A, B)

if not C == None:
    printMatrix(C)