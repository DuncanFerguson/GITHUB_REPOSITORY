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



def main():
    """Main Function to run the code"""
    # # The following code is set up for the speed test unit testing
    Speed_Test = random.sample(range(1, 10000000000), 10000000)
    Speed_Test2 = random.sample(range(1, 10000000000), 10000000)
    Speed_Test.sort()
    Speed_Test2.sort()
    t1 = time()
    binsearch(Speed_Test, 65465)
    t2 = time()
    print("Time for the Brute = ", int(t2-t1)*10000)
    t3 = time()
    cPairDist(Speed_Test)
    t4 = time()
    print("Time for the Algo = ",  int(t4-t3)*10000)




if __name__ == '__main__':
    main()

