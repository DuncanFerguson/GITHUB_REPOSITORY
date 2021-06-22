# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4581
# Assignment: Lab 1
# Date 6/10/2021

def printMatrix(m):
    for row in m:
        print(row)

def matrixMult(A, B):
    """This Functions first checks if you can multiply two matrices
    If you you can it then creates a blank matrix. Then fills out that matrix"""
    print("Matrix A Dimensions = ", len(A), "x", len(A[0]))
    print("Matrix B Dimensions = ", len(B), "x", len(B[0]))

    # Number of columns in the first matrix must equal the number of rows of the second matrix
    # In General (m x n)x(n x p) = m x p
    if len(A[0]) == len(B):
        datalist = [0, ] * len(A) * len(B[0])  # Creating a list of the number of entries
        C = []  # creating a blank list C
        for i in range(len(A)):
            rowList = []  # Resetting Row List
            for j in range(len(B[0])):
                rowList.append(datalist[len(A) * i + j])
            C.append(rowList)

        # Going Back through my blank_matrix C and filling it out
        for i in range(len(A)):  # Looping through Matrix A Rows
            for j in range(len(B[0])):  # Iterating through Matrix B Columns
                for k in range(len(B)):
                    C[i][j] += A[i][k] * B[k][j]  # Summing up index positions
        return C
    else:
        print("Number of Columns in the first matrix\n"
              "Do Not Equal the rows in the Second Matrix\n"
              "Try Again")
        return None


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

# Test2
A = [[ 2, -3, 3, 0],
    [-2, 6, 5, 1],
    [ 4, 7, 8, 2]]
B = [[-1, 9, 1],
    [ 0, 6, 5],
    [ 3, 4, 7]]


C = matrixMult(A, B)

if not C == None:
    printMatrix(C)

# Test3
A = [[2, -3, 3, 5],
     [-2, 6, 5, -2]]

B = [[-1, 9, 1],
     [0, 6, 5],
     [3, 4, 7],
     [1, 2, 3]]

C = matrixMult(A, B)

if not C == None:
    printMatrix(C)
