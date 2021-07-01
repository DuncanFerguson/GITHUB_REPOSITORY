# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4581
# Assignment: Lab 4
# Date 7/6/2021

# Step 2
# Conquer: Recursively find the closet pair distance in each sublist (obtains distances 1 and 2 from above

# Step 3 Combine: C
# Compute the remaing distance (3 from above), and combine them by taking the minimum of the tree

import sys

def brute(points):
    """Brute Force for finding the min distance between an array of points in a list that has a been presorted"""
    min = sys.maxsize
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
    print("Left: ", left, "\n",
          "Right: ", right, "\n",
          "Mid: ", mid)
    left_min = brute(left)
    right_min = brute(right)
    mid_min = brute(mid)
    combo = [left_min, right_min, mid_min]
    combo.sort()
    min = brute(combo)
    return min


def main():
    """Main Function to run the code"""
    A = [7, 4, 12, 14, 2, 10, 16, 6]
    # A = [1, 4, 9, 15]
    # B = [7, 4, 12, 14, 2, 10, 16, 5]
    # C = [14, 8, 2, 6, 3, 10, 12]
    A.sort()
    print(recCPairDist(A))


if __name__ == '__main__':
    main()

