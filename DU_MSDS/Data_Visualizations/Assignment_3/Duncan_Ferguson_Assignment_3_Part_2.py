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

diamonds = sns.load_dataset('diamonds')
diamonds.info()

# Stripping out Colors D and E and any cut Fair
# TODO will want to look back through this
diamonds = diamonds[(~diamonds.color.isin(["D", "E"])) & (diamonds.cut!='Fair')]
diamonds["color"] = diamonds["color"].cat.remove_unused_categories()
diamonds["cut"] = diamonds["cut"].cat.remove_unused_categories()
diamonds.info()

sns.set_style('darkgrid')
g = sns.FacetGrid(diamonds, col='cut', row='color')
g = g.map(plt.scatter, 'price', 'carat')
plt.show()