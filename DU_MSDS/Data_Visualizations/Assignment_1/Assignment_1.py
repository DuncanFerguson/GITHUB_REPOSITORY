# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4433
# Assignment: Assignment 1
# Date 6/24/2021


"""Assignment 1 (due by midnight MST the day prior to Live Session 2)

• Assignment 1, Part 1: Construct a CSV file with the first eight elements of the
periodic table. Include columns for name, symbol, and atomic number. Read that
into a pandas DataFrame. Inside the program, add a ninth and 10th element, and
then add a column with the atomic weights rounded to the nearest integer.

• Assignment 1, Part 2: Make a list of strings for nine Greek letters, for example
‘alpha’. Make that list such that the strings are not in alphabetic order. Make two
9-element numpy arrays of random floating-point numbers with an estimated
mean of 10 and a standard deviation of 1.5. Make another array of nine elements
ranging from zero to two times pi. Name it ‘angle’. Make another array holding
the cosine of that ‘angle’ array. Construct a dictionary from all of the above. Form
a DataFrame from that dictionary, and print it out. Sort the DataFrame ascending
on the Greek letters, drop two columns of your choice, drop one of the rows, and
print that out.

• Assignment 1, Part 3: Write a program in Python to create and print out the first
12 Fibonacci numbers. Then iterate over the last five numbers to build another
list with the ratio of each number to its predecessor. What do you observe about
this latter list?

• Assignment 1, Part 4: Provide a function that converts temperature in Kelvin to
Rankine. Make a list of five Kelvin temperatures, and print out their values in
Rankine. Repeat using a lambda function.

"""

import pandas as pd
import random
import numpy as np

# Reading in CSV file for periodic table
df = pd.read_csv("Periodic_Table.csv")

# Adding in 9th Element
df = df.append({'Name': 'Fluorine', 'Symbol':'F', 'Atomic Number': '9'}, ignore_index=True)

# Adding in 10th Element
df = df.append({'Name': 'Neon', 'Symbol': 'Ne', 'Atomic Number': '10'}, ignore_index=True)

# Adding in Column with Atomic Weights Rounded to the nearest Integer
Atomic_Weights = [1.008, 4.002602, 6.941, 9.012182, 10.8, 12.011, 14.007, 15.999, 18.998403, 20.1797]
df['Atomic Weights'] = Atomic_Weights
df['Atomic Weights'] = df['Atomic Weights'].round(decimals=0).astype(int)
print(df)


 # Make another array holding
# the cosine of that ‘angle’ array. Construct a dictionary from all of the above. Form
# a DataFrame from that dictionary, and print it out. Sort the DataFrame ascending
# on the Greek letters, drop two columns of your choice, drop one of the rows, and
# print that out.

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




# Construct a dictionary from all of the above.