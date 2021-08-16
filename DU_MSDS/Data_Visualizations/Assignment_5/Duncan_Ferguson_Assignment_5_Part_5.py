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

output_file('histo.html')
np.random.seed(51)
x = 100 + 15*np.random.randn(500)
xx, edges = np.histogram(x, bins=15, range=[x.min(), x.max()])

df = pd.DataFrame({'xx':xx, 'left': edges[:-1], 'right': edges[1:]})

print(df.head(12))

p = figure(plot_width=1200, plot_height=500)
p.quad(bottom=0, top=df['xx'], left=df['left'], right=df['right'], fill_color='blue', line_color='black')

show(p)

