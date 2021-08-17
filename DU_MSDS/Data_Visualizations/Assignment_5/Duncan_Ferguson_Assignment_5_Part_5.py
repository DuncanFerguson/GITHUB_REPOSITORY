# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4433
# Assignment: Assignment 5 Part 5
# Date 8/23/2021

"""Generate 500 points from the random exponential distribution
Choose your own parameters for that use Bokeh to plot a histogram of that distribution such
that there are at least 15 bins with counts greater than zero"""

# TODO figure out random exponential distribution

import numpy as np
import pandas as pd
from bokeh.plotting import figure, show, output_file

output_file('histo_Duncan_Ferguson_Assignment_5_Part_5.html')
np.random.seed(51)

n = 500  # Number of Points
scale = 100

x = np.random.exponential(n, scale)
xx, edges = np.histogram(x, bins=15, range=[x.min(), x.max()])

df = pd.DataFrame({'xx':xx, 'left': edges[:-1], 'right': edges[1:]})
print(df.head(12))
p = figure(plot_width=1200, plot_height=500)
p.quad(bottom=0, top=df['xx'], left=df['left'], right=df['right'], fill_color='blue', line_color='black')

show(p)

