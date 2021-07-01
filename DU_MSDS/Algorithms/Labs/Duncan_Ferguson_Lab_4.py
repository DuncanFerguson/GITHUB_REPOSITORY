# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4581
# Assignment: Lab 4
# Date 7/6/2021

import sys
import random
from time import time

def cPairDist(points):
    """Brute Force for finding the min distance between an array of points in a list that has a been presorted"""
    min = sys.maxsize  # Creating a hugely maximum list
    for i in range(len(points)-1):
        distance = int(abs(points[i+1]-points[i]))
        if distance < min:
            min = distance
    return min


def recCPairDist(points):
    """This function takes in a sorted list of points and performs the divide/ conquer combine steps
    Returns the min distance it finds."""
    # Dividing the list into two equal pieces
    n = len(points)
    left = points[:n//2]
    right = points[n//2:]
    mid = [left[-1:][0], right[:1][0]]
    mid.sort()
    # print("Left: ", left, "Right: ", right, "Mid: ", mid)
    left_min = cPairDist(left)
    right_min = cPairDist(right)
    mid_min = abs(mid[1]-mid[0])

    # TODO There is something that is going wrong right here that needs some figuring out
    combo = [left_min, right_min, mid_min]
    combo.sort()
    min = cPairDist(combo)
    return min


def main():
    """Main Function to run the code"""
    A = [7, 4, 12, 14, 2, 10, 16, 6]
    B = [7, 4, 12, 14, 2, 10, 16, 5]
    C = [14, 8, 2, 6, 3, 10, 12]


    # # The following code is set up for the speed test unit testing
    Speed_Test = random.sample(range(1, 10000000000), 10000000)
    Speed_Test.sort()
    t1 = time()
    cPairDist(Speed_Test)
    t2 = time()
    print("Time for the Brute = ", int(t2-t1)*10000)
    t3 = time()
    recCPairDist(Speed_Test)
    t4 = time()
    print("Time for the Algo = ",  int(t4-t3)*10000)




if __name__ == '__main__':
    main()

