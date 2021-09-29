import numpy as np
import pandas as pd

def getMonth(inDate):
    """Get Month Function"""

    return(int(inDate[5:7]))

def getCatIndex(inCat):
    count = 0
    itemCategories  = 0
    while (itemCategories[count] != inCat) and (count < len(itemCategories)-1):
        count += 1
    return (count)

def main():
    """Main Function to run everything"""
    columns = ["transactionID",
               "num_items_purchased",
               "total_price_of_item",
               "date",
               "store",
               "category"]

    df_ex3 = pd.read_csv("ds_ex3.txt", sep="\t", names=columns)

    # fout = open("ds_ex3.txt", 'wb')
    # TODO get the proper integer for the two below
    # numLocations = 0
    # numItemCategories = 0
    # cube = np.zeros((12,numLocations,numItemCategories))

    print(df_ex3)





if __name__ == '__main__':
    main()
