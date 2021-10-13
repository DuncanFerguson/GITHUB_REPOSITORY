# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4431-1
# Assignment: Exercise 5
# Date: 10/16/2021
# Group: Name: Broken Toe
# Group Members: Emma Bright, Mike Santoro


import pandas as pd
import numpy as np
from csv import reader

from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder

theData = []
with open('exercise5b_input.csv.txt', 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        theData.append(row)

# use transaction encoder to transform into an 1-hot boolean encoded numpy arrayk
te = TransactionEncoder()
te_ary = te.fit(theData).transform(theData)
print("\n\nte_ary returned from TransactionEncoder.fit().transform():")
print(te_ary)

# convert into a data frame for convience and to pass into apriori
df2 = pd.DataFrame(te_ary,columns = te.columns_)

print("\n\nDataFrame version:")
print(df2.head(25))



# Call apriori to find frequent itemsets with min_support = 30%
freq_items = apriori(df2, min_support=0.01, use_colnames=True)
print("\n\nfreq_items:")
print(freq_items)


# for index, row in freq_items.iterrows():
# 	print(str(row[0]) + ' ' + str(row[1]) )


# add a column to freq_items that contains the number of items in the itemset
freq_items['length'] = freq_items['itemsets'].apply(lambda x: len(x))
print(type(freq_items))
print(freq_items.columns)
print(freq_items)


# examples of how to filter your itemsets further, for illustration only, not actually used below
# NOTE: Do not assign back to freq_items because may remove rows need by association_rules() function below
reducedFreqItems = freq_items[(((freq_items['length'] == 2) & (freq_items['support'] >= 0.01)) |
	((freq_items['length'] >= 3)&(freq_items['support'] >= 0.01)))]
# reducedFreqItems = freq_items[ (freq_items['length'] >= 2) &  (freq_items['support'] >= 0.35) ]
print("\n\nReduced freq_items (length == 2 & support >= 40%) | (length >=3 & support >= 30%) ")
print(reducedFreqItems)



# now mine the rules by calling association_rules
print("\n\nThe rules:")
rules = association_rules(freq_items, metric="confidence", min_threshold=0.01)
print(type(rules))

# rename columns "antecedents support" to "antsup" and "consequents support" to "consup" so print nicer table
rules.columns = ['antecedents', 'consequents', 'antsup', 'consup', 'support', 'confidence', 'lift', 'leverage', 'conviction']
print(rules.columns)
# print( rules[ ["antecedents","consequents","support","confidence","lift"] ] )
# print( rules[ ["antecedents","antsup","consequents","consup","support","confidence","lift"] ] )
print(rules[["antecedents","consequents","antsup","consup","support","confidence","lift"]])

# print("rules.head(20):")
# print( rules.head(20) )
