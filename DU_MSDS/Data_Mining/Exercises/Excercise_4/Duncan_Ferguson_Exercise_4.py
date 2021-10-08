from csv import reader
import collections
from itertools import combinations
import pandas as pd
import numpy as np

# https://github.com/vinay-k-pisharody/Apriori-Implementation/blob/master/Apriori.py
# https://towardsdatascience.com/apriori-association-rule-mining-explanation-and-python-implementation-290b42afdfc6

NUMTRANS = 0
minSupCount = .03


itemSetCount = collections.defaultdict(int)
# with open("inputExercise4.csv", 'r') as read_obj:
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
df = df[df.min_sup >= minSupCount]

# Sorting the Pandas
df['Key'] = df.index
df['Key_Length'] = df['Key'].str.len()
df.sort_values(by=["Key_Length", 'Values', 'Key'], ascending=True, inplace=True)
del df['Key_Length']

# print(df)

#%%

columns = list(df['Key'])
del df['Key']
index_i = columns.copy()

df_2 = pd.DataFrame(columns=columns, index=index_i)
df_2 =df_2.fillna(0)

for row in df_2.index:
    for c_index in df_2.keys():
        perm = [''.join(l) for i in range(len(c_index)) for l in combinations(c_index, i + 1)]
        if row in perm:
            df_2.loc[row, c_index] = int(df.at[str(c_index), 'Values']) / int(df.at[str(row), 'Values'])

# df_2.insert(0, "Sum", df_2.sum(axis=1))
df_2.insert(0, "Values", df["Values"])
df_2.insert(1, "min_sup", df["min_sup"])

# print(df_2.at["D", "BD"])

print(df_2)