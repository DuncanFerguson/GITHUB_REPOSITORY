# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4431-1
# Assignment: Exercise 4
# Date: 10/7/2021
# Group: Name: Broken Toe
# Group Members: Emma Bright, Mike Santoro

from csv import reader
import collections
from itertools import combinations
import pandas as pd

def main():
    """Initializing a dictionary, number of transaction counts, and the minimum support threshold"""
    itemSetCount = collections.defaultdict(int)
    NUMTRANS = 0
    minSupCount = .04

    # Scanning through the file and creating a list of each itemset present and their counts
    with open("inputExercise4.csv", 'r') as read_obj:
    # with open('smallinput.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        for row in csv_reader:
            NUMTRANS += 1
            string = "".join(row)
            perms = [''.join(l) for i in range(len(string)) for l in combinations(string, i + 1)]
            for i in perms:
                itemSetCount[i] += 1

    # Turning the dictionary into a panda and adding in the minimum support
    df = pd.DataFrame({'Keys': list(itemSetCount.keys()), 'Values': list(itemSetCount.values())})
    df["min_support"] = df["Values"] / NUMTRANS  # Adding the minimum support
    df.set_index('Keys', inplace=True)  # Setting the index to be the keys
    df = df[df.min_support >= minSupCount]  # Filtering out anything that doesn't meet the min support threshold

    # Sorting the dataframe to make it easier to read
    df['Key'] = df.index  # Creating a key column to be better able to count length
    df['Key_Length'] = df['Key'].str.len()
    df.sort_values(by=["Key_Length", 'Values', 'Key'], ascending=True, inplace=True)
    del df['Key_Length']  # Removing columns used for sorts
    del df['Key']  # Removing columns used for sorts

    # Creating a confidence matrix
    df_confidence = pd.DataFrame(columns=df.index, index=df.index)
    df_confidence = df_confidence.fillna(0)  # Filling out the the matrix with zeros

    # Creating list that contain associations that we are looking for
    minsup_4_minconf_60 = []
    minsup_4_minconf_50 = []

    # Filling out the confidence matrix
    for row in df_confidence.index:
        for c_index in df_confidence.keys():
            perm = [''.join(l) for i in range(len(c_index)) for l in combinations(c_index, i + 1)]
            if row in perm:
                df_confidence.loc[row, c_index] = int(df.at[str(c_index), 'Values']) / int(df.at[str(row), 'Values'])

                # Appending minimum confidence intervals to a list
                # Adding in First Value compared to Second Value and confidence
                if df_confidence.at[row, c_index] >= .5 and row != c_index:
                    minsup_4_minconf_50.append([row, c_index, df_confidence.at[row, c_index]])
                if df_confidence.at[row, c_index] >= .6 and row != c_index:
                    minsup_4_minconf_60.append([row, c_index, df_confidence.at[row, c_index]])

    print("FOr min confidence 60%")
    for item in minsup_4_minconf_60:
        list1 = [char for char in item[0]]
        list2 = [char for char in item[1]]
        for element in list1:
            if element in list2:
                list2.remove(element)
        print(item[0],"=>","".join(list2), "STRONG, confidence = ", item[2],
              "Lift = ", df.at[str(item[1]),"min_support"] / (df.at[item[0], "min_support"]*df.at["".join(list2), "min_support"]),)



    # print("D=>B confidence=", df_confidence.at["D", "BD"], "Lift:", df.at["BD", "min_support"] /
    #       (df.at["D", "min_support"]*df.at["B", "min_support"]))


if __name__ == '__main__':
    main()