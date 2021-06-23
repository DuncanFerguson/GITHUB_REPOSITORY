# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4433
# Assignment: Assignment 1
# Date 6/24/2021

# Part 2

"""
Assignment 1, Part 2: Make a list of strings for nine Greek letters, for example
‘alpha’. Make that list such that the strings are not in alphabetic order. Make two
9-element numpy arrays of random floating-point numbers with an estimated
mean of 10 and a standard deviation of 1.5. Make another array of nine elements
ranging from zero to two times pi. Name it ‘angle’. Make another array holding
the cosine of that ‘angle’ array. Construct a dictionary from all of the above. Form
a DataFrame from that dictionary, and print it out. Sort the DataFrame ascending
on the Greek letters, drop two columns of your choice, drop one of the rows, and
print that out.
"""

import random
import numpy as np

# String of nine greek letters
nine_greek_letters = ['Alpha', 'Beta', 'Gamma',
                      'Delta', 'Epsilon', 'Zeta',
                      'Eta', 'Theta', 'Iota']

# Shuffling greek letters list
random.shuffle(nine_greek_letters)

# 9-element numpy array of random floating point numbers with an estimated mean of 10 and standard deviation of 1.5
mean = 10
std = 1.5
nine_element_array = np.random.normal(loc=mean, scale=std, size=9)
print(nine_element_array)
print("Mean of Array", np.mean(nine_element_array))

# Array of nine elements ranging from zero to two times pi. Name it ‘angle’.
angle = np.random.uniform(low=0, high=2*np.math.pi, size=9)
print(angle)

# Make another array holding the cosine of that ‘angle’ array.
cosine_angle = np.cos(angle)
print(cosine_angle)