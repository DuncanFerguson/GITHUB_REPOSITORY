# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4433
# Assignment: Assignment 2
# Date 7/8/2021

"""Assignment 2, Part 2: Read into a DataFrame the file py_ide2.csv, and provide both a
horizontal bar chart and a vertical bar chart, complete with all labels. Be sure to rotate
the IDE names so that they are readable."""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("py_ide2.csv")
print(df)
