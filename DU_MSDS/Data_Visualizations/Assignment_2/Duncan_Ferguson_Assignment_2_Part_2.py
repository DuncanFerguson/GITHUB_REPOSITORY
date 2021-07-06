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

df = pd.read_csv("py_ide2.csv")  # Reading in the data frame

fig, ax = plt.subplots(1, 2, figsize=(14, 8), num=91)  # Setting up the plot layout

# Horizontal bar Chart
ax[0].barh(df['IDE'], df['Adoption'])

# Setting up the titles for Horizontal bar Chart
ax[0].set_title('IDE Adoption')
ax[0].set_xlabel('Adoption')
ax[0].set_ylabel('Ide')

# Setting up Vertical Bar Chart
plt.xticks(range(len(df)), df['IDE'], rotation=65)  # Rotating IDE names to be readable
ax[1].bar(range(len(df)), df['Adoption'])
ax[1].set_title("IDE Adoption")
ax[1].set_xlabel("IDE")
ax[1].set_ylabel("Adoption")

# Displaying Chart
plt.tight_layout()
plt.show()


