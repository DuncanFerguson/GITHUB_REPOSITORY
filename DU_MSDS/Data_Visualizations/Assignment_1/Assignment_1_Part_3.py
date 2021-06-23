# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4433
# Assignment: Assignment 1
# Date 6/24/2021

"""
• Assignment 1, Part 3: Write a program in Python to create and print out the first
12 Fibonacci numbers. Then iterate over the last five numbers to build another
list with the ratio of each number to its predecessor. What do you observe about
this latter list?
"""

def fib(n):
    """Creating Fibonacci Numbers"""
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

fib_list = []

# Creating the first 12 values of the fibonacci numbers not including 0
for i in range(1,13,1): fib_list.append(fib(i))

# Printing out the first 12 values of the fibonacci numbers
for i in range(len(fib_list)): print(fib_list[i])

ratio_list = []

for i in range(7,12,1):
    ratio_list.append(fib_list[i]/fib_list[i-1])

print(ratio_list)

