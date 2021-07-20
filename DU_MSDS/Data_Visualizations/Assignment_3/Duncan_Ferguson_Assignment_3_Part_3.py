# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4433
# Assignment: Assignment 2
# Date 7/22/2021

""" Assignment 3, Part 3: Using the built-in Seaborn dataset car_crashes, prepare plots with
a scattergram with the linear model for both the total vs. speeding and the total vs.
alcohol.
"""

import seaborn as sns
import matplotlib.pyplot as plt

# Setting Seaborn Style
sns.set()
sns.set_style('whitegrid')

# Loading Data
car_crashes = sns.load_dataset('car_crashes')
car_crashes.info()
print(car_crashes.head())

# Prepare plots with a scattergram with the linear model for the total vs. speeding
sns.lmplot(x='total', y='speeding', data=car_crashes, scatter=True, fit_reg=True, aspect=2, truncate=False)
plt.title("Total vs Speeding")
plt.tight_layout()
plt.show()

# Plot with a scattergram with the linear model for the total vs. alcohol.
sns.lmplot(x='total', y='alcohol', data=car_crashes, scatter=True, fit_reg=True, aspect=2, truncate=False)
plt.title("Total vs Alcohol")
plt.tight_layout()
plt.show()
