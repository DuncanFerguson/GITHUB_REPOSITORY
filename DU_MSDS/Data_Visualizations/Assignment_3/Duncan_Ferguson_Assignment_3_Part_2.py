# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4433
# Assignment: Assignment 2
# Date 7/22/2021

""" Assignment 3, Part 2: Using the built-in Seaborn dataset diamonds, establish a
FacetGrid based on ‘cut’ and ‘color’. Eliminate colors ‘D’ and ‘E’ as well as the cut ‘Fair’.
Within that grid, plot the scatterplot for ‘price’ vs. ‘carat’.
"""

import seaborn as sns
import matplotlib.pyplot as plt

# Loading Data Set
diamonds = sns.load_dataset('diamonds')

# Eliminate colors ‘D’ and ‘E’ as well as the cut ‘Fair’. They are categorial variables
diamonds = diamonds[(~diamonds.color.isin(["D", "E"])) & (diamonds.cut != 'Fair')]
diamonds["color"] = diamonds["color"].cat.remove_unused_categories()
diamonds["cut"] = diamonds["cut"].cat.remove_unused_categories()

# Establish a FacetGrid based on ‘cut’ and ‘color’ added hue to be clarity
sns.set_style('darkgrid')
g = sns.FacetGrid(diamonds, col='cut', row='color', hue='clarity')

# Within that grid, plot the scatterplot for ‘price’ vs. ‘carat’
g = g.map(plt.scatter, 'price', 'carat', edgecolor='w').add_legend()
plt.show()
