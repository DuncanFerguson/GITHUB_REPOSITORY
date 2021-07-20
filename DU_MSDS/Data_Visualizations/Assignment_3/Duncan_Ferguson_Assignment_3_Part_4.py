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

# TODO take out the outliers on the box charts

iris = sns.load_dataset('iris')
iris.info()
print(iris.head())

# Setting Up subplots
fig, ax = plt.subplots(2, 2, sharey=True)
fig.suptitle("Seaborn Iris Data")

# Box Plot 1
sns.boxplot(ax=ax[0][0], x='sepal_length', y='species', data=iris)
ax[0][0].set_title("sepal_length")

# Box Plot 2
sns.boxplot(ax=ax[0][1], x='sepal_width', y='species', data=iris)
ax[0][1].set_title("sepal_width")

# Box Plot 3
sns.boxplot(ax=ax[1][0], x='petal_length', y='species', data=iris)
ax[1][0].set_title("petal_length")

# Box Plot 4
sns.boxplot(ax=ax[1][1], x='petal_width', y='species', data=iris)
ax[1][1].set_title("petal_width")

plt.tight_layout()
plt.show()
