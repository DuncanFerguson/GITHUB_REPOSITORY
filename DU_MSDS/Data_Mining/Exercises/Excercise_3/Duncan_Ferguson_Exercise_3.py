import numpy as np
from csv import reader

# def getMonth(inDate):
#     """Get Month Function"""
#     return(int(inDate[5:7]))
#
# def getCatIndex(inCat):
#     count = 0
#     itemCategories  = 0
#     while (itemCategories[count] != inCat) and (count < len(itemCategories)-1):
#         count += 1
#     return (count)

def main():
    """Main Function to run everything"""
    columns = ["transactionID", "num_items_purchased", "total_price_of_item", "date", "store", "category"]

    location = ['SouthGlenn', 'Tamarac', 'HighlandsRanch', 'ColoradoBlvd', 'WashingtonPark', 'CherryCreek',
                'GovernorsRanch', 'UnionStation', 'CastleRock']

    itemCategories = ['produce', 'meat', 'bakery', 'freezer', 'dairy', 'deli', 'snack', 'softdrinks', 'beer',
                      'household']

    numLocations = len(location)
    numItemCategories = len(itemCategories)

    with open('ds_ex3.txt', 'r') as read_obj:
        csv_reader = reader(read_obj)

    print(csv_reader)



    # fout = open("ds_ex3.txt", 'wb')
    # TODO get the proper integer for the two below
    # numLocations = 0
    # numItemCategories = 0
    # cube = np.zeros((12,numLocations,numItemCategories))






if __name__ == '__main__':
    main()
