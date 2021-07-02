# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4581
# Assignment: Lab 4
# Date 7/6/2021

import sys
import random
from time import time
global lowest_min
lowest_min = sys.maxsize


def cPairDist(points):
    """This Finds the minimum Distance between a list of points using brute force"""
    global lowest_min
    # print("cPairDist", points)
    for i in range(len(points)-1):
        temp = int(abs(points[i+1]-points[i]))
        if temp < lowest_min:
            lowest_min = temp
    return lowest_min


def recCPairDist(points):
    """This function takes in a sorted list of points and performs the divide/ conquer combine steps
    Returns the min distance it finds."""
    global lowest_min
    n = len(points)
    if n <= 3:
        lowest_min = cPairDist(points)
        return lowest_min

    left = points[:n//2]
    # print("Left", left)
    right = points[n//2:]
    # print("Right", right)
    mid = [left[-1], right[0]]
    # print("Mid", mid)

    recCPairDist(left)
    recCPairDist(right)
    recCPairDist(mid)
    return lowest_min

def main():
    """Main Function to run the code"""
    A = [7, 4, 12, 14, 2, 10, 16, 6]
    B = [7, 18, 12, 84, 2, 10, 16, 5]
    C = [14, 8, 2, 6, 3, 10, 12]
    Test_it = random.sample(range(100000000000), 1000000)
    Test_it.sort()
    A.sort()
    B.sort()
    C.sort()

    Test_it2 = random.sample(range(100000000000), 1000000)
    Test_it2.sort()

    # print(recCPairDist(A))
    # print(recCPairDist(B))
    # print(recCPairDist(C))
    t1 = time()
    print(recCPairDist(Test_it))
    t2 = time()
    print((t2-t1)*1000)

    t3 = time()
    print(cPairDist(Test_it2))
    t4 = time()
    print((t4-t3)*1000)

if __name__ == '__main__':
    main()

