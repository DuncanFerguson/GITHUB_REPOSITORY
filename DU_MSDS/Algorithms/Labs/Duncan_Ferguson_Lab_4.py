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

def cPairDist(points):
    """This function taks in a list of 1-d points (Integers)
     and returns the distance between the closet pair of points"""
    points.sort()  # Sorting the list
    n = len(points)
    # Dividing Points into mid points
    half_1 = points[:n//2]
    half_2 = points[n//2:]
    print(half_1, "Second", half_2)
    print(points)

    return points

def recCPairDist(points):
    """This function takes in a sorted list of points and performs the divide/conqure/combine steps"""
    return points

A = [7, 4, 12, 14, 2, 10, 16, 6]
B = [7, 4, 12, 14, 2, 10, 16, 5]
C = [14, 8, 2, 6, 3, 10, 12]
cPairDist(C)