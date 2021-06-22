# Duncan Ferguson
# Class: COMP-3005-2
# Assignment 2: senntinel

def suminput():
    '''This sums the 5 different numbers that the user enters'''
    print("This program will sum all the numbers you enter. Enter -1 to Exit")
    sum_string = 0
    input_string = 0
    while input_string != "-1":
        print ("Current Sum is: ", sum_string)
        input_string = input("Enter a number: ")
        sum_string += int(input_string)
    print("Sum =", sum_string+1)

suminput()