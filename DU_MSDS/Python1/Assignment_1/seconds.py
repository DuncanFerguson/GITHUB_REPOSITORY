# Student: Duncan Ferguson
# Student ID: 871-641-260
# Class: COMP-3005-2; Assignment 1: Square 1
# Date: 9/14/2020

# In a script file named seconds.py, write a program that will initialize a variable that stores a
# number of seconds and  then calculate in different variables, the equivalent number of hours, minutes and seconds.
# For example, 300 seconds is 0 hours,  5 minutes and 0 seconds while 4503 seconds is 1 hour, 15 minutes and 3 seconds.
# Output the  hour, minutes and seconds. (4 Points)

# While True adds the element to only allows user to enter integers
# Source: https://docs.python.org/3/tutorial/errors.html
while True:
    try:
        Seconds_Input = int(input('Please enter a number of seconds: '))
        break
    except ValueError:
        print("Numeric Numbers only! Try it again")

# Calculations for changing input
Num_Hours = Seconds_Input // 3600
Num_Minutes = int((Seconds_Input - (Num_Hours*3600))/60)
Num_Seconds = int(Seconds_Input - (Num_Hours*3600) - (Num_Minutes*60))

print(Num_Hours, "Hours, ", Num_Minutes, " Minutes, ", Num_Seconds, " Seconds")
