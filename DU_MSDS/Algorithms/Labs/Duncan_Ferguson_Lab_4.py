# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4581
# Assignment: Lab 4
# Date 7/6/2021

import sys
global min_distance

def cPairDist(points):
    """This Finds the minimum Distance between a list of points using brute force"""
    min_distance = sys.maxsize
    for i in range(len(points)-1):
        temp = int(abs(points[i+1]-points[i]))
        if temp < min_distance:
            min_distance = temp
    return min_distance


def recCPairDist(points):
    """This function takes in a sorted list of points and performs the divide/ conquer combine steps
    Returns the min distance it finds."""
    n = len(points)

    # Base Case
    if n <= 3:
        temp = cPairDist(points)

    # Divide
    left = points[:n//2]
    right = points[n//2:]
    print("Left", left)
    print("Right", right)
    recCPairDist(left)
    recCPairDist(right)


def main():
    """Main Function to run the code"""
    A = [7, 4, 12, 14, 2, 10, 16, 6]
    B = [7, 4, 12, 14, 2, 10, 16, 5]
    C = [14, 8, 2, 6, 3, 10, 12]
    A.sort()
    recCPairDist(A)


if __name__ == '__main__':
    main()

