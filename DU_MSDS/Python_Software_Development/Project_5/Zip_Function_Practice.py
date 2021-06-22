# Student: Duncan Ferguson
# Student ID: 871-641-260
# Class: COMP-3006-2; Project 5: Zip_Function
# Date: 3/11/2021
# Teacher: dalton.crutchfield@du.edu
# TA: sunny.shrestha@du.edu

"""This Program takes in suits and values as lists. It then makes a Suite for each value and adds it to
zip_suits. Then There is a value created for each suit and added to zip_values. The two lists of equal length are then
easy to zip together. A list of the zipped tuples is then printed"""

suits = ["Diamond", "Heart", "Spade", "Club"]
values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
zip_suits = []  # Blank List to create corresponding suits to values
zip_values = []  # Blank list to create corresponding values to suits

for suit in suits:  # For every suit in suits create enough suits in a row to match the length of the values
    for value in values:
        zip_suits.append(suit)
        zip_values.append(value)

deck = list(zip(zip_suits, zip_values))


print(deck)