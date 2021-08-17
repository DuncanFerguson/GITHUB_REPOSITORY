# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4433
# Assignment: Assignment 5 Part 5
# Date 8/23/2021

"""Generate 500 points from the random exponential distribution
Choose your own parameters for that use Bokeh to plot a histogram of that distribution such
that there are at least 15 bins with counts greater than zero"""

import numpy as np
from bokeh.plotting import figure, show, output_file

np.random.seed(50)

# Setting up 500 points from the random exponential distribution
n = 500  # Number of Points
scale = 100
x = np.random.exponential(scale=scale, size=n)

# Setting up numpy histo
hist, edges = np.histogram(x, density=True, bins=15, range=[x.min(), x.max()])
p = figure(title="500 points from the random exponential distribution in 15 bins",
           x_axis_label="Sample Size",
           y_axis_label="Sample Distribution")
p.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:], line_color='White')

# Showing and saving histo
show(p)
output_file('histo_Duncan_Ferguson_Assignment_5_Part_5.html')



