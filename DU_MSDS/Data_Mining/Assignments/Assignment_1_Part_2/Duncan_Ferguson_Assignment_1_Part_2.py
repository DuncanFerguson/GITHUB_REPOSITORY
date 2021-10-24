# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4431-1
# Assignment: Assignment 1 part 1
# Date: 10/19/2021
# Group Members from Assignment 4: Emma Bright, Mike Santoro

from csv import reader
import collections
from itertools import combinations
import pandas as pd


def printAssociations(association_list, df, conf_level):
    """This function goes through and prints out the proper format for the associations
    It also calculates the lift"""
    for item in association_list:
        # Casting the string into a individual character list
        list1, list2 = [char for char in item[0]], [char for char in item[1]]
        for element in list1:
            if element in list2:
                list2.remove(element)  # Removing the similar letters from the list
        lift = df.at[str(item[1]), "min_support"] / (df.at[item[0], "min_support"]*df.at["".join(list2), "min_support"])
        meaningful = ""
        strong_conf = ""
        # Assigning value if the lift is meaningful and if confidence is strong
        if lift > 1.0:
            meaningful = " (Meaningful)"
        if item[2] >= conf_level:
            strong_conf = "STRONG"
        print(item[0], "=>", "".join(list2),",", strong_conf, "confidence = ", item[2],
              ", Lift = ", lift, meaningful)


def main():
    """Initializing a dictionary, number of transaction counts, and the minimum support threshold"""
    itemSetCount = collections.defaultdict(int)  # Creating blank default dict
    NUMTRANS = 0

    # Scanning through the file and creating a list of each itemset present and their counts
    with open("Assignment_1_part_1_data.csv", 'r') as read_obj:
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
    df = df[df.min_support >= float(2/17)]  # Filtering out anything that doesn't meet the min support threshold of .04

    # Sorting the dataframe to make it easier to read
    df['Key'] = df.index  # Creating a key column to be better able to count length
    df['Key_Length'] = df['Key'].str.len()
    df.sort_values(by=["Key_Length", 'Values', 'Key'], ascending=True, inplace=True)
    del df['Key_Length']  # Removing columns used for sorts
    del df['Key']  # Removing columns used for sorts

    # Creating a confidence matrix
    df_confidence = pd.DataFrame(columns=df.index, index=df.index).fillna(0)

    # Creating list that contain associations that we are looking for
    minsup_4_minconf_60, minsup_4_minconf_50, all_rules = [], [], []

    # Filling out the confidence matrix
    for row in df_confidence.index:
        for c_index in df_confidence.keys():
            perm = [''.join(l) for i in range(len(c_index)) for l in combinations(c_index, i + 1)]
            if row in perm:
                df_confidence.loc[row, c_index] = int(df.at[str(c_index), 'Values']) / int(df.at[str(row), 'Values'])

                # Appending minimum confidence intervals to the correct corresponding list
                if df_confidence.at[row, c_index] >= .5 and row != c_index:
                    minsup_4_minconf_50.append([row, c_index, df_confidence.at[row, c_index]])
                if df_confidence.at[row, c_index] >= .6 and row != c_index:
                    minsup_4_minconf_60.append([row, c_index, df_confidence.at[row, c_index]])
                if row != c_index:
                    all_rules.append([row, c_index, df_confidence.at[row, c_index]])

    df = df.sort_values("Values", ascending=False)
    print(df)
    print("\nFor min confidence greater than 60%: number of rules:", len(minsup_4_minconf_60))
    printAssociations(minsup_4_minconf_60, df, .6)

    print("\nFor min confidence greater than 50%: number of rules:", len(minsup_4_minconf_50))
    printAssociations(minsup_4_minconf_50, df, .5)

    print("\n All of the Rules with a support above 2: number of rules (Strong Conf >.5):", len(all_rules))
    printAssociations(all_rules, df, .5)

if __name__ == '__main__':
    main()
