# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4433
# Assignment: Assignment 2
# Date 7/22/2021

""" Assignment 3, Part 3: Using the built-in Seaborn dataset car_crashes, prepare plots with
a scattergram with the linear model for both the total vs. speeding and the total vs.
alcohol.
"""

# TODO is this right? Will want to check further into it

import seaborn as sns
import matplotlib.pyplot as plt

car_crashes = sns.load_dataset('car_crashes')
car_crashes.info()
print(car_crashes.head())

sns.scatterplot(x='total', y='speeding', data=car_crashes)
plt.show()

sns.scatterplot(x='total', y='alcohol', data=car_crashes)
plt.show()