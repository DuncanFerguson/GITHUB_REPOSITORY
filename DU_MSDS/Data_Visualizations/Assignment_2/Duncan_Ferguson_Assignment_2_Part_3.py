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
from datetime import datetime, date, time, timedelta
import random

#  List of eight strings that represent days evenly spread out
dlist = ['01/01/2021', '02/01/2021', '03/01/2021', '04/01/2021',
         '05/01/2021', '06/01/2021', '07/01/2021', '08/01/2021']

# Random uniform distribution, array of eight floats ranging from 100 to 200 value
ulist = np.random.uniform(low=100, high=200, size=(8,))

# Turning dlist and ulist into Dataframe
dframe = {'date': dlist, 'units': ulist}
dframe = pd.DataFrame(dframe)

# Converting datestring into datetime object
dframe['date'] = pd.to_datetime(dframe['date'])

# Setting Date as the index
dframe = dframe.set_index('date')

print(dframe)

