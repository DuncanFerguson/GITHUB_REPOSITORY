# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4433
# Assignment: Assignment 1
# Date 6/24/2021

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

import pandas as pd
import random
import numpy as np

# List of strings for nine Greek letters
nine_greek_letters = ['Alpha', 'Beta', 'Gamma',
                      'Delta', 'Epsilon', 'Zeta',
                      'Eta', 'Theta', 'Iota']

# Shuffling greek letters list so that they are not in alphabetic order
random.shuffle(nine_greek_letters)

# Make two 9-element numpy arrays of random floating-point numbers
# with an estimated mean of 10 and a standard deviation of 1.5.
mu = 10
sigma = 1.5
n = 9

array_1 = np.random.default_rng().normal(mu, sigma, n)
array_2 = np.random.default_rng().normal(mu, sigma, n)
print(array_1)

# Array of nine elements ranging from zero to two times pi. Name it ‘angle’.
angle = np.random.uniform(low=0, high=2*np.math.pi, size=n)

# Make another array holding the cosine of that ‘angle’ array.
cosine_angle = np.cos(angle)

# Construct a dictionary from all of the above.
greek_dict = dict(zip(nine_greek_letters, zip(*[array_1, array_2, angle, cosine_angle])))

# Form a DataFrame from that dictionary, and print it out.
df = pd.DataFrame.from_dict(greek_dict, orient='index',
                            columns=["Array_1", "Array_2", "Angle", "Cosine_Angle"])
print(df)

# Sort the DataFrame ascending on the Greek letters,
# drop two columns of your choice, drop one of the rows, and print that out.
df_sorted = df.sort_index()
df_sorted = df_sorted.drop(columns=["Array_1", "Array_2"], index="Zeta")
print(df_sorted)

