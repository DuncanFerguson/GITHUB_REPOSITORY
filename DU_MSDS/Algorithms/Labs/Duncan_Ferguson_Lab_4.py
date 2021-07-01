# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4581
# Assignment: Lab 4
# Date 7/6/2021

# Use a recursive divide-and-concquer algorithm
# The Algorithm states that the distance between the closet pair of points in a list is a minimum of

# Step 1
# Divide: Split the list into two equal pieces

# Step 2
# Conquer: Recursively find the closet pair distance in each sublist (obtains distances 1 and 2 from above

# Step 3 Combine: C
# Compute the remaing distance (3 from above), and combine them by taking the minimum of the tree

import sys
INF = sys.maxsize  # Creating Infinity

global min
min = INF


def brute(points):
    """Brute Force Testing"""
    min = INF
    points.sort()
    for i in range(len(points)-1):
        if abs(points[i]-points[i+1]) < min:
            min = abs(points[i]-points[i+1])
    print(min)
    return min


def cPairDist(points):
    """This function taks in a list of 1-d points (Integers)
     and returns the distance between the closet pair of points"""
    points.sort()  # Sorting the list
    n = len(points)

    # Dividing Points into two equal lists if they are even. Close to even if they are odd
    left = points[:n//2]
    right = points[n//2:]
    recCPairDist([left, right])

def recCPairDist(points):
    """This function takes in a sorted list of points and performs the divide/ conquer combine steps
    Returns the min distance it finds."""
    for i in range(len(points)):
        if len(points[i]) <= 2:
            min = brute(points[i])
        else:
            cPairDist(points[i])
    # print(points)
    return "This"


A = [7, 4, 12, 14, 2, 10, 16, 6]
B = [7, 4, 12, 14, 2, 10, 16, 5]
C = [14, 8, 2, 6, 3, 10, 12]
cPairDist(C)