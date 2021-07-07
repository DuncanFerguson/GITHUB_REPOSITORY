# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4433
# Assignment: Assignment 2
# Date 7/8/2021

""" Assignment 2, Part 3: Construct a list of eight strings that represent days evenly spread
out. Drawing from the random uniform distribution, make an array of eight floats ranging
from 100 to 200 in value. Establish a DataFrame from that list and that array, convert the
dates to pandas datetime objects, and set them to the index. Make two charts in the
same window or canvas as follows: (1) a line plot of the values vs. dates and (2) a bar
chart of the same.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import copy

#  List of eight strings that represent days evenly spread out
dlist = ['01/01/2021', '02/01/2021', '03/01/2021', '04/01/2021',
         '05/01/2021', '06/01/2021', '07/01/2021', '08/01/2021']

# Random uniform distribution, array of eight floats ranging from 100 to 200 value
ulist = np.random.uniform(low=100, high=200, size=(8,))
vlist = copy.deepcopy(ulist)

# Turning dlist and ulist into Dataframe
d = list(zip(dlist, vlist))
df = pd.DataFrame(d, columns=['date', 'values'])
print(df)

# Converting datestring into datetime object
df['date'] = pd.to_datetime(df['date'])

# Setting Date as the index
df = df.set_index('date')

# Make two charts 1) a line plot of the values vs. dates and (2) a bar chart of the same.
fig, ax = plt.subplots(nrows=2, ncols=1, sharey='col', sharex='row', figsize=(14, 8), num=94)

# Making the first plot
ax[0].plot(df.index, df['values'], color='r')
ax[0].tick_params(rotation=45)
ax[0].set_title("Plot of Values v. Dates")
ax[0].set_ylabel("Values")
ax[0].set_axisbelow(True)
ax[0].grid(axis='y')

# Making Histogram Plot
ax[1].bar(df.index, df['values'], width=10)
ax[1].set_title("Bar Chart of Values v. Dates")
ax[1].set_xlabel('Dates')
ax[1].set_ylabel("Values")
ax[1].tick_params(rotation=45)
ax[1].set_axisbelow(True)
ax[1].grid(axis='y')

plt.tight_layout()
plt.show()
