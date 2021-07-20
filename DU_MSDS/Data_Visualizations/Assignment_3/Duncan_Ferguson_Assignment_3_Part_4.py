# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4433
# Assignment: Assignment 2
# Date 7/22/2021


""" Assignment 4, Part 4: Using the built-in Seaborn dataset iris, provide a plot with four
subplots wherein the distribution of each of the numeric columns is presented as a set of
boxplots, one for each ‘species’.
"""

import seaborn as sns
import matplotlib.pyplot as plt

# Set Style
sns.set()
sns.set_style('whitegrid')

# Load Data
iris = sns.load_dataset('iris')
iris.info()
print(iris.head())

# Setting Up subplots
fig, ax = plt.subplots(2, 2)
fig.suptitle("Iris Data Boxplots\nDistribution of each numeric columns")

# Box Plot 1
sns.boxplot(ax=ax[0][0], x='species', y='sepal_length', data=iris, showfliers=False)

# Box Plot 2
sns.boxplot(ax=ax[0][1], x='species', y='sepal_width', data=iris, showfliers=False)

# Box Plot 3
sns.boxplot(ax=ax[1][0], x='species', y='petal_length', data=iris, showfliers=False)

# Box Plot 4
sns.boxplot(ax=ax[1][1], x='species', y='petal_width', data=iris, showfliers=False)

plt.tight_layout()
plt.show()
