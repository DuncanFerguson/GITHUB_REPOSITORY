# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4433
# Assignment: Assignment 1
# Date 6/24/2021

"""
Assignment 1, Part 4: Provide a function that converts temperature in Kelvin to
Rankine. Make a list of five Kelvin temperatures, and print out their values in
Rankine. Repeat using a lambda function.
"""

# Function converting kelvin to rakine
def Kelvin_2_Rankine(k):
    """Converting Kelvin to Rankine"""
    return k*1.8

# list of five kelvin temperatures
five_kelvin_temps = [1,2,3,4,5]

print("Function Conversion of Kelvin Temps to Rankine")
for kelvin in five_kelvin_temps:
    print(Kelvin_2_Rankine(kelvin))

# Lambda Function converting kelvin to rankine
k_2_r = lambda k: k*1.8

# printing out conversion with lambda function
print("Lambda Conversion of Kelvin Temps to Rankine")
for k in five_kelvin_temps:
    print(k_2_r(k))