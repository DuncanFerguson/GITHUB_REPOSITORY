# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4431-1
# Assignment: Exercise 4
# Date: 10/7/2021 <br>
# Group: Name: Broken Toe <br>
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
    min_confidence = .5

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

    # Filling out the confidence matrix
    for row in df_confidence.index:
        for c_index in df_confidence.keys():
            perm = [''.join(l) for i in range(len(c_index)) for l in combinations(c_index, i + 1)]
            if row in perm:
                df_confidence.loc[row, c_index] = int(df.at[str(c_index), 'Values']) / int(df.at[str(row), 'Values'])

    # Adding the the two data frames together
    df_confidence.insert(0, "Values", df["Values"])
    df_confidence.insert(1, "min_sup", df["min_support"])


    print(df_confidence)





    # # Create associations and test if they satisfy the confidence threshold.
    # df = df.reindex(columns=df.columns.tolist() + list(itemSetCount.keys()))
    #
    # # Adding in the confidence
    # for row in df.index:
    #     print(row)


    # print(df)


    # print(itemSetCount)

    # df = pd.DataFrame({'Keys': list(itemSetCount.keys()), 'Values': list(itemSetCount.values())})
    # df.set_index('Keys', inplace=True)
    # df['min_sup'] = df['Values']/NUMTRANS
    # df = df[df.min_sup >= minSupCount]
    #
    # # Sorting the Pandas
    # df['Key'] = df.index
    # df['Key_Length'] = df['Key'].str.len()
    # df.sort_values(by=["Key_Length", 'Values', 'Key'], ascending=True, inplace=True)
    # del df['Key_Length']
    #
    # columns = list(df['Key'])
    # del df['Key']
    # index_i = columns.copy()
    #
    # df_confidence = pd.DataFrame(columns=columns, index=index_i)
    # df_confidence =df_confidence.fillna(0)
    # df_lift = df_confidence.copy()
    #
    # for row in df_confidence.index:
    #     for c_index in df_confidence.keys():
    #         perm = [''.join(l) for i in range(len(c_index)) for l in combinations(c_index, i + 1)]
    #         if row in perm:
    #             df_confidence.loc[row, c_index] = int(df.at[str(c_index), 'Values']) / int(df.at[str(row), 'Values'])
    #
    # df["Prob"] = df["Values"] / NUMTRANS
    #
    # df_confidence.insert(0, "Values", df["Values"])
    # df_confidence.insert(1, "min_sup", df["min_sup"])
    # df_confidence.insert(2, "Prob", df["Prob"])
    #
    # print("D=>B confidence=", df_confidence.at["D", "BD"], "Lift:", df_confidence.at["BD", "Prob"] / (df_confidence.at["D", "Prob"]*df_confidence.at["B", "Prob"]))
    # print("E=>F confidence=", df_confidence.at["E", "EF"], "Lift:", df_confidence.at["EF", "Prob"] / (df_confidence.at["E", "Prob"]*df_confidence.at["F", "Prob"]))
    # print("CG=>H confidence=", df_confidence.at["CG", "CGH"], "Lift:", df_confidence.at["CGH", "Prob"] / (df_confidence.at["CG", "Prob"]*df_confidence.at["H", "Prob"]))

if __name__ == '__main__':
    main()