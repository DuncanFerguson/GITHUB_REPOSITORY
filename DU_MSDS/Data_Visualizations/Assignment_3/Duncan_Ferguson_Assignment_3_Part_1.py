# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4433
# Assignment: Assignment 2
# Date 7/22/2021

"""Assignment 3, Part 1: Using the built-in Seaborn dataset mpg, provide a heatmap of the
correlation of all the numeric columns and provide a pairplot of the same."""

import seaborn as sns
import matplotlib.pyplot as plt

"""Please note that for this assignment I considered model year as a numeric value"""

# Loading Data
mpg = sns.load_dataset('mpg')

# Displaying Basic Info
# print(mpg.head())  # Printing out the head
# mpg.info()  # Getting a sense of the data

# Scrubbing Data to only include numeric values
mpg = mpg.select_dtypes(include='number')

# Scrubbing out year
# mpg = mpg.drop(['model_year'], axis=1)  # Uncomment if you include year as a non numeric value


# Heatmap of the correlation of all the numeric columns
sns.heatmap(mpg.corr(), cmap='coolwarm')
plt.title("Heatmap of the correlation of all the numeric columns\nSeaborn 'mpg' data set")
plt.tight_layout()
plt.show()

# Displaying heatmap of null values
# sns.heatmap(mpg.isnull(), cbar=False, cmap='viridis')
# plt.title("Heatmap of the null values for all numeric columns")
# plt.tight_layout()
# plt.show()

# Pair plot of the all the numeric columns
sns.set_style('whitegrid')
g = sns.pairplot(mpg, hue='model_year')  # Pairplot
g.fig.suptitle("Pairplot of the correlation of all the numeric columns\nSeaborn 'mpg' data set", size=25)
g.fig.subplots_adjust(top=.9)
plt.show()
