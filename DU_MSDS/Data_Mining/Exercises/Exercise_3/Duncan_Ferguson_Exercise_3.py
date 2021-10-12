# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4431-1
# Assignment: Excercise 3
# Date: 9/30/2021
# Group: Name: Broken Toe
# Group Members: Emma Bright, Mike Santoro

import numpy as np
import pandas as pd

def getCatIndex(inCat):
    count = 0
    while (itemCategories[count] != inCat) and (count < len(itemCategories)-1):
        count += 1
    return (count)

def getlocIndex(inLoc):
    count = 0
    while (locations[count] != inCat) and (count < len(locations)-1):
        count += 1
    return(count)

def getMonth(inDate):
    return(int(inDate[5:7]))




def main():
    """Main File to run the code"""
    locations = ['SouthGlenn', 'Tamarac', 'HighlandsRanch', 'ColoradoBlvd', 'WashingtonPark', 'CherryCreek',
                 'UnionStation', 'CastleRock']

    itemCategories = ['produce', 'meat', 'bakery', 'freezer', 'dairy', 'deli', 'snack', 'softdrinks', 'beer',
                      'household']
    numLocations = len(locations)
    numItemCategories = len(itemCategories)

# Loading in file
data = np.loadtxt("ds_ex3.txt", dtype='str')
data
df = pd.DataFrame(data, columns=["transactionid", "num_items_purchase",
                       "total_price","date", "store","category"])
df["month"] = df["date"].str[5:7]
df
# df["category_index"] = df.apply(lambda row: getCatIndex(row['category']), axis=1)
# df["store_index"] = df.apply(lambda row: getlocIndex(row['store']), axis=1)
# df
#

#
# # month = getMonth(data[:,3])
# for row in data:
#     row[3] = getMonth(row[3])
#     # row[4] = getlocIndex(row[4])
#     # row[5] = getCatIndex(row[5])



#%%

# Creating a 3D numpy Array
cube_item = np.zeros((12, numLocations, numItemCategories))
cube_price = np.zeros((12, numLocations, numItemCategories))
cube_item

#%%
cube_price

#%% md

What to turn in:
-In the textbox write up what you found to be "interesting" in the data
-In the text box below the "interesting description, print out the contents of your Month vs ItemCategory 2D cub
- Attach Code


