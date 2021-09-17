# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4431-1
# Assignment: Assignment 1
# Date 9/16/2021

# Group Members: Duncan Ferguson, Mike Santoro and Emma Bright
# Random thing in Common: We have all broken a toe

import numpy as np

def main():
    """Create list of 15 numbers and return the mean and median.
    Put in the text box at the top your list of numbers, the mean and the median.
    Below that copy your code"""
    np.random.seed(10)
    mu = 15
    sigma = 2
    n = 15
    array_1 = np.random.default_rng().normal(mu, sigma, n)
    array_2 = np.random.default_rng().normal(mu, sigma, n)


    print("Array_1", array_1)
    print("Array_1 Mean", array_1.mean())
    print("Array_1 Median", np.median(array_1),"\n")

    print("Array_2", array_2)
    print("Array_2 Mean", array_2.mean())
    print("Array_2 Median", np.median(array_2))


if __name__ == "__main__":
    main()
