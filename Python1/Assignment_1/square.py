# Student: Duncan Ferguson
# Student ID: 871-641-260
# Class: COMP-3005-2; Assignment 1: Square 1
# Date: 9/16/2020

# Square 1
#In a script file named square.py, write a program that initializes a variable to store the length of a square in inches,
# calculates the perimeter and area of the square, and outputs the results.  Make sure you label your outputs so the user
# can tell which is which.  Test it by changing the initial value to different ones.  (4 Points)

# While True adds the element to help input the correct answers
# Source: https://docs.python.org/3/tutorial/errors.html
while True:
    try:
        Length_of_Square = int(input('Please enter the Length of the square in inches: '))
        break
    except ValueError:
        print("Numeric Numbers only! Try it again")

Area_of_Square = Length_of_Square ** 2
Perimeter_of_Square = Length_of_Square * 4
print("Length of Square (Inches): ", Length_of_Square)
print("Perimeter of Square (Inches): ", Perimeter_of_Square)
print("Area of Square: (sq. in.)", Area_of_Square)
