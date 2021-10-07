from csv import reader
import collections
from itertools import combinations
import pandas as pd
import numpy as np

# https://github.com/vinay-k-pisharody/Apriori-Implementation/blob/master/Apriori.py
# https://towardsdatascience.com/apriori-association-rule-mining-explanation-and-python-implementation-290b42afdfc6


NUMTRANS = 0
minSupCount = 3

itemSetCount = collections.defaultdict(int)
with open('smallinput.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        NUMTRANS += 1
        string = "".join(row)
        perms = [''.join(l) for i in range(len(string)) for l in combinations(string, i + 1)]
        for i in perms:
            itemSetCount[i] += 1

df = pd.DataFrame({'Keys': list(itemSetCount.keys()), 'Values': list(itemSetCount.values())})
df.set_index('Keys', inplace=True)
# df['min_sup'] = df['Values']/NUMTRANS * 100
df['min_sup'] = df['Values']/NUMTRANS

# Sorting the Pandas
df['Key'] = df.index
df['Key_Length'] = df['Key'].str.len()
df.sort_values(by=["Key_Length", 'Values', 'Key'], ascending=True, inplace=True)
del df['Key_Length']

print(df)

#%%

columns = list(df['Key'])
# del df['Key']
index_i = columns.copy()

df_2 = pd.DataFrame(columns=columns, index=index_i)
df_2 =df_2.fillna(0)

for row in df_2.index:
    for c_index in df_2.keys():
        if row in c_index:
            df_2.at[row, c_index] = 1
df_2['Sum'] = df_2.sum(axis=1)

print(df_2)
#%%

# TODO This equation is most likely wrong
df["Appearance"] = df_2["Sum"]
print(df)
# print(df_2)
# df_2.to_csv("Testing.csv")