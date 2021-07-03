# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4581
# Assignment: Lab 4
# Date 7/6/2021

import sys


def cPairDist(points):
    """This Finds the minimum Distance between a list of points using brute force"""
    lowest_min = sys.maxsize
    for i in range(len(points)-1):
        temp = int(abs(points[i+1]-points[i]))
        if temp < lowest_min:
            lowest_min = temp
    return lowest_min


def recCPairDist(points):
    """This function takes in a sorted list of points and performs the divide/ conquer combine steps
    Returns the min distance it finds."""
    n = len(points)

    # Base Case for finding lowest distance between points
    if n <= 3:
        return cPairDist(points)

    # Dividing the points into left right and a middle two
    left = points[:n//2]
    right = points[n//2:]
    mid = [left[-1], right[0]]

    # # Print Statements to check the work
    # print("Left", left)
    # print("Right", right)
    # print("Mid", mid)

    # returning the minimum of a recursive loop for the left, right, mid
    return min(recCPairDist(left), recCPairDist(right), recCPairDist(mid))


def main():
    """Main Function to run the code with the examples that have been given"""
    A = [7, 4, 12, 14, 2, 10, 16, 6]
    B = [7, 4, 12, 14, 2, 10, 16, 5]
    C = [14, 8, 2, 6, 3, 10, 12]

    A.sort()
    B.sort()
    C.sort()

    print(recCPairDist(A))
    print(recCPairDist(B))
    print(recCPairDist(C))


if __name__ == '__main__':
    main()

