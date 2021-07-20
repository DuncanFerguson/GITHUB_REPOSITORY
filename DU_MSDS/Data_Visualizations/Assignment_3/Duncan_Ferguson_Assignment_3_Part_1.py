# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4433
# Assignment: Assignment 2
# Date 7/22/2021

"""Assignment 3, Part 1: Using the built-in Seaborn dataset mpg, provide a heatmap of the
correlation of all the numeric columns and provide a pairplot of the same."""

# TODO look into this on displaying the data differently for the pair plot

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Loading Data
mpg = sns.load_dataset('mpg')

# Displaying Basic Info
print(mpg.head())  # Printing out the head
mpg.info()  # Getting a sense of the data

# Scrubbing Data to only include numeric values
mpg = mpg.select_dtypes(include='number')
print(mpg.head())

# Heatmap of the correlation of all the numeric columns
sns.heatmap(mpg.corr(), cmap='coolwarm')
plt.title("Heatmap of the correlation of all the numeric columns\nSeaborn 'mpg' data set")
plt.tight_layout()
plt.show()

# Displaying heatmap of null values
sns.heatmap(mpg.isnull(), cbar=False, cmap='coolwarm')
plt.title("Heatmap of the null values for all numeric columns")
plt.tight_layout()
plt.show()

# Pair plot of the all the numeric columns
sns.pairplot(mpg)
plt.tight_layout()
plt.show()

