# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4433
# Assignment: Assignment 2
# Date 7/22/2021

"""Assignment 3, Part 1: Using the built-in Seaborn dataset mpg, provide a heatmap of the
correlation of all the numeric columns and provide a pairplot of the same."""

"""Useful Linkes
https://www.youtube.com/watch?v=UgtjatBt3vY
"""

# TODO look into this on displaying the data differently for the pair plot
# TODO maybe look at filtering out the objects

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('mpg')
print(df.head())
df.info()

sns.heatmap(df.corr(), cmap='coolwarm')
plt.tight_layout()
plt.show()

sns.pairplot(df)
plt.tight_layout()
plt.show()

