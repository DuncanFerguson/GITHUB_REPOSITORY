# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4431-1
# Assignment: Week 5 Reading Code
# Date: 10/12/2021
# Group Members from Assignment 4: Emma Bright, Mike Santoro

import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import apriori, association_rules
import matplotlib.pyplot as plt
import seaborn as sns

def import_file():
    """This function imports our Data Set"""

    # TODO get rid of the NaNs
    df = pd.read_csv("retail_dataset.csv", sep=",", na_filter=False)
    print(df.head())

    items = set()
    for col in df:
        items.update(df[col].unique())

    # Looking at the unique values and count that are in the data set
    items.remove("")
    print("Count of Items", len(items))
    print("Items", items)

    # Taking a sneak peak of the NaNs
    # sns.heatmap(df.isnull(), cbar=False)
    # plt.show()


    return df, items

def data_Preprocessing(df, items):
    """This function is for the Data Preprocessing"""
    itemset = set(items)
    encoded_vals = []
    for index, row in df.iterrows():
        rowset = set(row)
        labels = {}
        uncommons = list(itemset-rowset)
        commons = list(itemset.intersection(rowset))
        for uc in uncommons:
            labels[uc] = 0
        for com in commons:
            labels[com] = 1
        encoded_vals.append(labels)
    print(encoded_vals[0])
    ohe_df = pd.DataFrame(encoded_vals)
    print(ohe_df.head())
    return ohe_df

def apply_apriori(ohe_df):
    """Applying the Apriori Algorithm"""
    freq_items = apriori(ohe_df, min_support=0.2, use_colnames=True, verbose=1)
    print(freq_items.head(8))
    rules = association_rules(freq_items, metric="confidence", min_threshold=0.6)
    print(rules.head())
    return rules

def viz_data(rules):
    """This Function shows the vizualization rules"""

    # Support v Confidence
    plt.scatter(rules['support'], rules['confidence'], alpha=0.5)
    plt.xlabel("support")
    plt.ylabel("confidence")
    plt.title("Support vs Confidence")
    plt.show()

    # Support v lift
    plt.scatter(rules['support'], rules['lift'], alpha=0.5)
    plt.xlabel('support')
    plt.ylabel('lift')
    plt.title('Support vs Lift')
    plt.show()

    # Lift vs confidence
    fit = np.polyfit(rules['lift'], rules['confidence'], 1)
    fit_fn = np.poly1d(fit)
    plt.plot(rules['lift'], rules['confidence'], 'yo', rules['lift'], fit_fn(rules['lift']))
    plt.show()

def main():
    """This Is the main function for running the code"""
    df, items = import_file()  # Importing the file
    ohe_df = data_Preprocessing(df, items)  # Preprocessing the data
    rules = apply_apriori(ohe_df)
    viz_data(rules)

if __name__ == '__main__':
    main()

